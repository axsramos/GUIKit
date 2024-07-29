from os import path as OSPath
import core.Config as CoreConfig
import core.SecretKey as CoreSecretKey
import json


class LoginModel:
    FILE_REMEMBER_ME = 'remember_me.json'

    def __init__(self) -> None:
        self._sdtLogin = {
            'UsrLgn': '',
            'UsrPwd': '',
            'RememberMe': True
        }

    def getSdtLogin(self):
        return self._sdtLogin

    def setUsrLgn(self, data_content):
        self._sdtLogin['UsrLgn'] = data_content

    def setUsrPwd(self, data_content):
        self._sdtLogin['UsrPwd'] = data_content

    def getRememberMe(self):
        src_file = OSPath.join('data', 'cookie', self.FILE_REMEMBER_ME)

        data_content = {}

        if OSPath.isfile(src_file):
            with open(src_file, mode='r', encoding='utf-8') as file:
                data_content = json.load(file)

            if not self._datastr_isvalid(data_content):
                data_content = self._remember_me_default()
        else:
            data_content = self._remember_me_default()

        return data_content

    def _remember_me_default(self):
        data_content = {
            "username": "",
            "password": "",
            "remember_me": True
        }
        return data_content

    def _datastr_isvalid(self, data_content):
        result = True

        if not 'username' in data_content:
            result = False

        if not 'remember_me' in data_content:
            result = False

        return result

    def setRememberMe(self, remember_me=False):
        csCoreConfig = CoreConfig.Config()
        path = csCoreConfig.get_block_item('DAS', 'path')

        csCoreSecretKey = CoreSecretKey.SecretKey()
        hash_pssw = ''
        if (self._sdtLogin['UsrPwd'] != ''):
            hash_pssw = csCoreSecretKey.generate_secret(self._sdtLogin['UsrPwd'])

        self._sdtLogin['RememberMe'] = remember_me
        src_file = OSPath.join(path,'data', 'cookie', self.FILE_REMEMBER_ME)

        data_content = {
            "username": "{}".format(self._sdtLogin['UsrLgn']),
            "password": "{}".format(hash_pssw),
            "remember_me": remember_me
        }
        try:
            with open(src_file, mode='w', encoding='utf-8') as file:
                json.dump(data_content, file, indent=4)
        except:
            pass
