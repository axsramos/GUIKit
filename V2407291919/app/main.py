from os import system as OSSystem
from threading import Thread
import core.Config as CoreConfig


class Program:
    def __init__(self) -> None:
        self.csCoreConfig = CoreConfig.Config()
        self.csCoreConfig.load()

        self.load_services()
        self.start_engine()

    def load_services(self):
        service_engines = self.csCoreConfig.get_block_item(
            'SERVICE', 'engines').replace("[", "").replace("]", "")
        engines = service_engines.split(",")

        for engine_item in engines:
            if engine_item != "":
                has_file = False
                src_file = CoreConfig.OSPath.join('service', engine_item)

                if CoreConfig.OSPath.isfile(src_file):
                    has_file = True
                else:
                    if src_file.find(".py") <= 0:
                        src_file = CoreConfig.OSPath.join(
                            'service', engine_item, 'main.py')
                        if CoreConfig.OSPath.isfile(src_file):
                            has_file = True
                if has_file == True:
                    th = Thread(target=self.start_services, args=(src_file,))
                    th.start()
                else:
                    print(
                        format(f"Arquivo de serviço ({engine_item}) não existe."))

    def start_engine(self):
        engine_item = self.csCoreConfig.get_block_item('DEFAULT', 'engine')
        has_file = False

        if (engine_item == '' or str(engine_item).lower() == 'none'):
            return

        if (engine_item == 'main' or engine_item == 'main.py'):
            print("DEFAULT.engine em config.ini é inválido.")
            return

        if CoreConfig.OSPath.isfile(engine_item):
            has_file = True
        else:
            engine_item = engine_item + '.py'
            if CoreConfig.OSPath.isfile(engine_item):
                has_file = True

        if has_file == True:
            th = Thread(target=self.start_services, args=(engine_item,))
            th.start()
        else:
            if engine_item == '.py':
                print(f"DEFAULT.engine não especificado em config.ini")
            else:
                engine = engine_item.replace(".py", "")
                print(
                    format(f"DEFAULT.engine ({engine}) em em config.ini não existe."))

    def start_services(self, src_file):
        OSSystem("python " + src_file)


if __name__ == "__main__":
    Program()
