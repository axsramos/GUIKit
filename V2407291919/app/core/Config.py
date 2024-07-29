import os.path as OSPath
import core.SecretKey as CoreSecretKey


class Config:
    SRC_FILE_CONFIG_INI = 'config.ini'
    DEFAULT_USER_PASSW = 'admin'

    def __init__(self) -> None:
        self.data_config = []

    def load(self):
        if not OSPath.isfile(self.SRC_FILE_CONFIG_INI):
            self.create_config_ini()

        data_content = []

        with open(self.SRC_FILE_CONFIG_INI, mode='r', encoding='utf-8') as file:
            data_content = file.readlines()

        data_section = []

        for data_item in data_content:
            data_line = data_item.replace('\n', '')
            if ((data_line[0:1] == '[') and (data_line[-1] == ']')):
                if len(data_section) > 0:
                    self.data_config.append({section: data_section})
                section = data_line.replace('[', '').replace(']', '')
                data_section = []
                continue
            s = data_line.split('=')
            if len(s) == 2:
                k = s[0]
                v = s[1]
                data_section.append({k: v})

        if len(data_section) > 0:
            self.data_config.append({section: data_section})

    def get_block(self, block):
        values = []

        for data_item in self.data_config:
            for section in data_item:
                if section == block:
                    values = data_item[section]

        return values
    
    def getall_block(self):
        values = []

        for data_item in self.data_config:
            for section in data_item:
                values.append(section)

        return values

    def get_block_item(self, block, item):
        value = ''

        for data_item in self.data_config:
            for section in data_item:
                if section == block:
                    for itens in data_item[section]:
                        if item in itens.keys():
                            value = itens[item]

        return value

    def create_config_ini(self):
        csCoreSecretKey = CoreSecretKey.SecretKey()
        passwd = csCoreSecretKey.generate_secret(self.DEFAULT_USER_PASSW)

        das_path = OSPath.abspath('')
        path_icon = OSPath.join(
            das_path, 'data', 'image', 'Logo', 'favicon.ico')

        data_content = '[DEFAULT]\n'
        data_content += 'engine=None\n'
        data_content += 'repository=das\n'
        data_content += 'maintenance=yes\n'
        data_content += 'application=.:: GUIKit ::.\n'
        data_content += 'title=Grafic User Interface\n'
        data_content += 'icon={}\n'.format(path_icon)
        data_content += 'theme=litera\n'
        data_content += 'version=1.0\n'
        data_content += 'app_auth=internal\n'
        data_content += 'app_start=yes\n'
        data_content += '\n'

        data_content += '[SERVICE]\n'
        data_content += 'engines=[GUIKit,Calculator,Notes]\n'
        data_content += '\n'

        data_content += '[DAS]\n'
        data_content += 'path={}\n'.format(das_path)
        data_content += '\n'

        data_content += '[NAS]\n'
        data_content += 'address=127.0.0.1\n'
        data_content += 'port=21\n'
        data_content += 'username=root\n'
        data_content += 'password=\n'
        data_content += '\n'

        data_content += '[DBMS]\n'
        data_content += 'drive=mysql\n'
        data_content += 'hostname=localhost\n'
        data_content += 'port=3306\n'
        data_content += 'database=db\n'
        data_content += 'username=root\n'
        data_content += 'password=\n'
        data_content += '\n'

        data_content += '[SESSION]\n'
        data_content += 'login_required=no\n'
        data_content += 'user_name={}\n'.format(self.DEFAULT_USER_PASSW)
        data_content += 'user_password={}\n'.format(passwd)
        data_content += '\n'

        with open(self.SRC_FILE_CONFIG_INI, mode='w', encoding='utf-8') as file:
            file.writelines(data_content)
