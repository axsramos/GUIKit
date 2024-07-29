from os import system as OSSystem
import os.path as OSPath
import ttkbootstrap as ttk
import core.Config as CoreConfig
import model.Dashboard.DashboardModel as DashboardModel
import model.Maintenance.ConfigModel as ConfigModel
import view.Dashboard.DashboardView as DashboardView
import view.Maintenance.ConfigView as ConfigView
import core.AppSession as AppSession


class DashboardController:
    def __init__(self) -> None:
        self.csDashboardModel = DashboardModel.DashboardModel()
        self.data_content = self.csDashboardModel.sd

        csAppSession = AppSession.AppSession()
        self.id_user_session = csAppSession.get_user_connected()

    def mount_screen(self):
        self._root = ttk.Window(
            themename=self.data_content["FormDesign"]["Theme"])
        self._root.title("{} {}".format(
            self.data_content["FormDesign"]["AppTitle"],
            self.data_content["FormDesign"]["Title"]))
        self._root.iconbitmap(self.data_content["FormDesign"]["AppIcon"])

        # DashboardView
        self._wDashboardView = DashboardView.DashboardView(self._root)
        self._wDashboardView.set_controller(self, self.data_content)
        self._wDashboardView.create()
        # /DashboardView

        self._root.mainloop()

    def get_apps(self):
        csCoreConfig = CoreConfig.Config()
        csCoreConfig.load()

        apps = []
        apps = csCoreConfig.get_block_item('SERVICE', 'engines').split(",")

        return apps

    def get_blocks(self):
        csCoreConfig = CoreConfig.Config()
        csCoreConfig.load()

        blocks = []
        blocks = csCoreConfig.getall_block()

        return blocks

    def get_blocks_item(self, section=[]):
        csCoreConfig = CoreConfig.Config()
        csCoreConfig.load()

        blocks = []
        sections = []
        
        if section.__len__() == 0:
            sections = self.get_blocks()
        else:
            sections = section

        for section_item in sections:
            itens = csCoreConfig.get_block(section_item)
            blocks.append({"{}".format(section_item):""})
            for item in itens:
                blocks.append(item)

        return blocks

    def _runProgram(self, module):
        if module == "CONFIG":
            self._config()
        else:
            path = OSPath.join(OSPath.abspath(
                ''), 'service', module, 'main.py')
            if OSPath.isfile(path):
                path_command = '{} start'.format(path)
                OSSystem(path_command)
            else:
                print('Program not start. {}'.format(path))

    def _config(self):
        self.csConfigModel = ConfigModel.ConfigModel()

        self.csConfigModel.sd["FormSession"]["id"] = self.id_user_session[0]
        self.csConfigModel.sd["FormSession"]["user"] = self.id_user_session[1]

        data_item = {
            "Data": {
                "Blocks": self.get_blocks(),
                "DataAllBlocks": self.get_blocks_item()
            }
        }
        self.csConfigModel.sd.update(data_item)

        nWindow = ttk.Toplevel(self._root)
        nWindow.title("{} - {}".format(
            self.csConfigModel.sd["FormDesign"]["AppTitle"],
            self.csConfigModel.sd["FormDesign"]["Title"]))
        nWindow.iconbitmap(self.csConfigModel.sd["FormDesign"]["AppIcon"])
        nWindow.focus()

        self.wConfigView = ConfigView.ConfigView(nWindow)
        self.wConfigView.set_controller(self, self.csConfigModel.sd)
        self.wConfigView.create()

    def _load_data_tree(self, section_filter):
        section = []
        if section_filter != '(Todos)':
            section.append(section_filter)
        
        self.csConfigModel.sd.clear()
        data_item = {
            "Data": {
                "Blocks": self.get_blocks(),
                "DataAllBlocks": self.get_blocks_item(section)
            }
        }
        
        self.csConfigModel.sd.update(data_item)

    def _close(self, tab_index):
        if tab_index == 0:
            self._root.quit()
        elif tab_index == 1:
            self.wConfigView.set_tab_display(0)

    def _confirm(self, tab_index):
        if tab_index == 0:
            self.wConfigView.set_tab_insert(1)
        elif tab_index == 1:
            print("insert in database.")
    
    def _update(self, tab_index):
        if tab_index == 0:
            self.wConfigView.set_tab_update(1)
        elif tab_index == 1:
            print("update in database.")
    
    def _delete(self, tab_index):
        if tab_index == 0:
            self.wConfigView.set_tab_delete(1)
        elif tab_index == 1:
            print("delete in database.")
    
    # def _options(self, tab_index):
    #     pass
