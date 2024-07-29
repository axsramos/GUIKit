import hashlib


class SecretKey:
    KEY_ID = '12481632641282565121024204840961'

    def __init__(self) -> None:
        pass

    def generate_secret(self, data=KEY_ID):
        data_secret = hashlib.md5(data.encode())

        return data_secret.hexdigest()
