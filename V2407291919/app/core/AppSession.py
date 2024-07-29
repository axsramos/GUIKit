import os.path as OSPath
import json
import datetime
import core.Config as CoreConfig
import core.SecretKey as CoreSecretKey


class AppSession:
    def __init__(self) -> None:
        csCoreConfig = CoreConfig.Config()
        csCoreConfig.load()

        self.app_path = csCoreConfig.get_block_item('DAS', 'path')
        self.app_start = csCoreConfig.get_block_item('DEFAULT', 'app_start')
        self.data_config = csCoreConfig.get_block('SESSION')
        self.user_name = csCoreConfig.get_block_item('SESSION', 'user_name')
        self.user_password = csCoreConfig.get_block_item(
            'SESSION', 'user_password')
        self.required = csCoreConfig.get_block_item(
            'SESSION', 'login_required')
        if (self.required.lower() in ('true', 'yes', '1')):
            self.login_required = True
        else:
            self.login_required = False

    def create_id_session(self):
        new_id = str(datetime.datetime.utcnow())
        return new_id.replace('-', '').replace(':', '').replace('.', '').replace(' ', '')

    def create_session_file(self):
        app_start = False

        if (self.app_start.lower() == 'yes' or self.app_start.lower() == 'true'):
            app_start = True

        file_path = OSPath.join(self.app_path, '', 'data',
                                'session', 'app_session.json')

        id = self.create_id_session()
        structured_data = []
        structured_data.append(
            {
                "id": "{}".format(id),
                "user": "{}".format(self.user_name),
                "password": "{}".format(self.user_password),
                "connected": not self.login_required,
                "app_start": app_start
            }
        )

        data_content = structured_data[0]

        with open(file_path, mode="w", encoding="utf-8") as file:
            json.dump(data_content, file, indent=4)

    def get_status_connected(self):
        file_path = OSPath.join(self.app_path, '', 'data',
                                'session', 'app_session.json')

        data_content = ''
        with open(file_path, mode='r', encoding='utf-8') as file:
            data_content = json.load(file)

        status = data_content['connected']

        return status
    
    def get_user_connected(self):
        file_path = OSPath.join(self.app_path, '', 'data',
                                'session', 'app_session.json')

        data_content = ''
        with open(file_path, mode='r', encoding='utf-8') as file:
            data_content = json.load(file)

        status = (data_content['id'], data_content['user'])

        return status

    def get_app_start(self):
        app_start = False
        file_path = OSPath.join(self.app_path, '', 'data',
                                'session', 'app_session.json')

        data_content = ''
        with open(file_path, mode='r', encoding='utf-8') as file:
            data_content = json.load(file)

        app_start = bool(data_content['app_start'])

        return app_start

    def set_status_connected(self, user, password):
        status = True
        file_path = OSPath.join(self.app_path, '', 'data',
                                'session', 'app_session.json')
        data_content = ''
        with open(file_path, mode='r', encoding='utf-8') as file:
            data_content = json.load(file)

        data_content['connected'] = True
        data_content['user'] = user
        data_content['password'] = password

        with open(file_path, mode='w', encoding='utf-8') as file:
            json.dump(data_content, file, indent=4)

        status = data_content['connected']

        return status

    def single_login(self, sdtLogin):
        csCoreSecretKey = CoreSecretKey.SecretKey()

        status_connected = False
        hash_pwd = csCoreSecretKey.generate_secret(sdtLogin['UsrPwd'])

        if (sdtLogin['UsrLgn'] == self.user_name and hash_pwd == self.user_password):
            status_connected = self.set_status_connected(
                self.user_name, self.user_password)

        return status_connected
