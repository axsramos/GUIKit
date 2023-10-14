from tkinter import Tk
import model.Dashboard.DashboardModel as DashboardModel
import view.Dashboard.DashboardView as DashboardView

class DashboardController:
    def __init__(self) -> None:
        self.app_title = ''
        self.title = ''
        self.csCascadingMenuModel = DashboardModel.DashboardModel()
        self.data_content = self.csCascadingMenuModel.sd
    
    def mount_screen(self):
        self._root = Tk()
        app_title = "{} Dashboard".format(self.app_title)
        self._root.title(app_title)

        # DashboardView
        self._wDashboardView = DashboardView.DashboardView(self._root)
        self._wDashboardView.set_controller(self, self.data_content)
        self._wDashboardView.create()
        # /DashboardView

        self._root.mainloop()
    
    def _close(self):
        self._root.quit()