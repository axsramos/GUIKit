import os.path as OSPath


class FormDesignModel:
    def structured_data(self):
        sd = {
            "FormDesign": self.form_design(),
            "FormSession": self.form_session()
        }
        return sd

    def form_design(self):
        path_icon = OSPath.join(OSPath.abspath(
            ''), 'data', 'image', 'Logo', 'favicon.ico')
        sd = {
            "AppIcon": path_icon,
            "AppTitle": "GUIKit",
            "Title": "Grafic User Interface TKinter",
            "Theme": "litera"
        }
        return sd
    
    def form_session(self):
        sd = {
            "id":"",
            "user":""
        }
        return sd
