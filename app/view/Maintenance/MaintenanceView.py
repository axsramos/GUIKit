from tkinter import Frame, Label
import view.UIElements.UIForm as UIForm


class MaintenanceView(UIForm.UIForm):
    BG_COLOR_DEFAULT = "white"
    def __init__(self, root) -> None:
        self.parent = root
        self.data_image = None
        self.data_message = {}

    def create(self):
        self.parent.config(bg=self.BG_COLOR_DEFAULT)

        frm_body = Frame(self.parent, bg=self.BG_COLOR_DEFAULT)
        Label(frm_body, image=self.data_image, bg=self.BG_COLOR_DEFAULT).pack(pady=15)
        Label(frm_body, text=self.data_message['title'], wraplength=600, font=("Tahoma", 22), bg=self.BG_COLOR_DEFAULT).pack(pady=15)
        Label(frm_body, text=self.data_message['message'], wraplength=600, font=("Tahoma", 12), bg=self.BG_COLOR_DEFAULT).pack()
        frm_body.pack()

        self.set_size_medium()
        data_geometry = self.set_geometry()
        self.parent.geometry(data_geometry)
        self.parent.resizable(False,False)
    