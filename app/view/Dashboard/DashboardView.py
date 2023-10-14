import view.UIElements.UIForm as UIForm


class DashboardView(UIForm.UIForm):
    def __init__(self, root) -> None:
        self.parent = root
        self.controller = None

    def set_controller(self, controller, data_content={}):
        self.controller = controller
        self.data_content = data_content

    def create(self):
        self.set_size_large()
        data_geometry = self.set_geometry()
        self.parent.geometry(data_geometry)
        self.parent.resizable(False, False)
