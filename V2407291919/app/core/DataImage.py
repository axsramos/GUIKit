from os import path as OSPath
import json


class DataImage:
    ONEPIXEL = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAANSURBVBhXYyi6/+8/AAdlA0+U7CoAAAAAAElFTkSuQmCC'

    def __init__(self) -> None:
        pass

    def get_data(self, folder, name):
        src_file = OSPath.join('data', 'image', folder, name)
        src_file = src_file + '.json'
        src_file = src_file

        data_content = []

        if OSPath.isfile(src_file):
            with open(src_file) as file:
                data_content = json.load(file)

        return data_content

    def get(self, folder, name):
        data_content = self.get_data(folder, name)

        img_data = self.ONEPIXEL

        for data_item in data_content:
            if data_item == 'data':
                img_data = data_content['data']

        return img_data
