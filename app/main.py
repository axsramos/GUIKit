from os import system as OSSystem
from threading import Thread
import core.Config as CoreConfig


class Program:
    def __init__(self) -> None:
        csCoreConfig = CoreConfig.Config()
        csCoreConfig.load()
        
        service_engines = csCoreConfig.get_block_item(
            'SERVICE', 'engines').replace("[", "").replace("]", "")
        engines = service_engines.split(",")

        for engine_item in engines:
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
                    format(f"Arquivo de serviço ({engine_item}) não foi localizado."))

    def start_services(self, src_file):
        OSSystem(src_file)


if __name__ == "__main__":
    Program()
