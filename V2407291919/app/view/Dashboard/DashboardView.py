import view.UIElements.UIForm as UIForm
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from time import time, strftime
from functools import partial


class DashboardView(UIForm.UIForm):
    def __init__(self, root) -> None:
        self.parent = root
        self.controller = None

    def set_controller(self, controller, data_content={}):
        self.controller = controller
        self.data_content = data_content

    def create(self):
        self.set_size_extreme_small()
        data_geometry = self.set_geometry()
        self.parent.geometry(data_geometry)
        self.parent.resizable(False, False)

        self.wall_clock()
        self.app_icon()

    def getTime(self):
        time()
        time_now = strftime('%H:%M:%S %p')

        self.label_wall_clock.config(text=time_now)
        self.label_wall_clock.after(1000, self.getTime)

    def wall_clock(self):
        self.label_wall_clock = ttk.Label(self.parent, font=(
            'Helvetica', 40, 'bold'), bootstyle=ttk.DEFAULT)
        self.label_wall_clock.pack(pady=20)
        self.getTime()

    def app_icon(self):
        apps = self.controller.get_apps()
        if len(apps) > 3:
            pad_y = 5
        else:
            pad_y = 35
        frame = ttk.Frame(self.parent)
        itens = 0
        for app in apps:
            itens += 1
            title_app = str(app).replace("[", "").replace("]", "").strip()

            if title_app == "GUIKit":
                title_app = "CONFIG"
            
            ttk.Button(frame,
                        text=title_app,
                        padding=5,
                        width=12,
                        bootstyle="dark-outline",
                        command=partial(
                            self.controller._runProgram, title_app)
                        ).pack(side=ttk.LEFT, padx=6, pady=2)
            
            if itens == 3:
                frame.pack(pady=pad_y)
                frame = ttk.Frame(self.parent)
                itens = 0
        
        if itens > 0:
            frame.pack(pady=pad_y)
