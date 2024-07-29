from os import path as OSPath
import json
import model.UIElements.FormDesign as FormDesign

class MaintenanceModel(FormDesign.FormDesignModel):
    FILE_MESSAGE = 'message.json'
    def __init__(self) -> None:
        self.sd = self.structured_data()
        self.sd["FormDesign"]["Title"] = "Maintenance"

    def get_message(self):
        src_file = OSPath.join('data', 'maintenance', self.FILE_MESSAGE)

        data_content = {}

        if OSPath.isfile(src_file):
            with open(src_file, mode='r', encoding='utf-8') as file:
                data_content = json.load(file)
            
            if not self._datastr_isvalid(data_content):
                data_content = self._message_default()
        else:
            data_content = self._message_default()
        
        return data_content

    def _message_default(self):
        data_content = {
            "title":"Desculpe, estamos em manuteção...",
            "message":"Infelizmente, no momento o app está fora do ar para manutenção.\nMas estamos fazendo o nosso melhor para recuperar as coisas."
        }

        return data_content

    def _datastr_isvalid(self, data_content):
        result = True

        if not 'title' in data_content:
            result = False

        if not 'message' in data_content:
            result = False
        
        return result