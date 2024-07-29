import view.UIElements.UIForm as UIForm
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class MaintenanceView(UIForm.UIForm):
    def __init__(self, root) -> None:
        self.parent = root
        self.data_image = None
        self.data_message = {}
    
    def set_controller(self, controller, data_content={}):
        self.controller = controller
        self.data_content = data_content

    def create(self):
        frame_body = ttk.Frame(self.parent, bootstyle=DEFAULT)
        ttk.Label(frame_body, image=self.data_image,
                  bootstyle=DARK).pack(pady=15)
        ttk.Label(frame_body, text=self.data_message['title'], wraplength=600, font=(
            "Tahoma", 22), bootstyle=DARK).pack(pady=15)
        ttk.Label(frame_body, text=self.data_message['message'], wraplength=600, font=(
            "Tahoma", 12), bootstyle=DARK).pack()
        frame_body.pack()

        self.set_size_medium()
        data_geometry = self.set_geometry()
        self.parent.geometry(data_geometry)
        self.parent.resizable(False, False)
