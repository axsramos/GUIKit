import os.path as OSPath
import sys
sys.path.append(OSPath.abspath(''))
import time
import core.Config as CoreConfig
import core.AppSession as CoreAppSession
import controller.Maintenance.MaintenanceController as Maintenance
import controller.Login.LoginInternalController as LoginInternal
import controller.Login.LoginExternalController as LoginExternal
import controller.Login.LoginCollaborateController as LoginCollaborate
import controller.Dashboard.DashboardController as Dashboard


class GUIKitProgram:
    def __init__(self) -> None:
        print("> GUIKitProgram - serviço iniciado.")

        self.csCoreConfig = CoreConfig.Config()
        self.csCoreConfig.load()

        self.app_auth = self.csCoreConfig.get_block_item('DEFAULT', 'app_auth')
        self.app_start = self.csCoreConfig.get_block_item(
            'DEFAULT', 'app_start')
        self.app_title = self.csCoreConfig.get_block_item(
            'DEFAULT', 'application')
        self.title = self.csCoreConfig.get_block_item('DEFAULT', 'title')
        self.icon = self.csCoreConfig.get_block_item('DEFAULT', 'icon')
        self.maintenance = self.csCoreConfig.get_block_item(
            'DEFAULT', 'maintenance')

        self._start_session()
        self._start_program()

    def _start_session(self):
        self.csCoreAppSession = CoreAppSession.AppSession()
        self.csCoreAppSession.create_session_file()

    def _start_program(self):
        if self.maintenance == 'yes':
            csMaintenance = Maintenance.MaintenanceController()
            csMaintenance.app_title = self.app_title
            csMaintenance.app_icon = self.icon
            csMaintenance.title = self.title
            csMaintenance.mount_screen()
        else:
            status_connected = self.csCoreAppSession.get_status_connected()
            self._process_login(status_connected)

    def _process_login(self, status_connected):
        implemented_programs = ['internal', 'external', 'collaborate']

        if not status_connected:
            if self.app_auth in (implemented_programs):
                if self.app_auth == 'internal':
                    csLoginInternal = LoginInternal.LoginInternalController()
                    csLoginInternal.app_title = self.app_title
                    csLoginInternal.app_icon = self.icon
                    csLoginInternal.title = self.title
                    csLoginInternal.mount_screen()

                if self.app_auth == 'external':
                    csLoginExternal = LoginExternal.LoginExternalController()
                    csLoginExternal.app_title = self.app_title
                    csLoginExternal.app_icon = self.icon
                    csLoginExternal.title = self.title
                    csLoginExternal.mount_screen()

                if self.app_auth == 'collaborate':
                    csLoginCollaborate = LoginCollaborate.LoginCollaborateController()
                    csLoginCollaborate.app_title = self.app_title
                    csLoginCollaborate.app_icon = self.icon
                    csLoginCollaborate.title = self.title
                    csLoginCollaborate.mount_screen()

                status_connected = self.csCoreAppSession.get_status_connected()
            else:
                if self.app_auth != "":
                    print('Programa ({}) não implementado\nUtilize as opções: {} \nNo arquivo config.ini no bloco [DEFAULT] em app_auth'.format(
                        self.app_auth, implemented_programs))

        if status_connected:
            if self.csCoreAppSession.get_app_start():
                self.start()

    def start(self):
        # Dashboard - exemple run
        csDashboard = Dashboard.DashboardController()
        csDashboard.data_content["FormDesign"]["AppTitle"] = self.app_title
        csDashboard.data_content["FormDesign"]["AppIcon"] = self.icon
        csDashboard.data_content["FormDesign"]["Title"] = self.title

        csDashboard.mount_screen()
        # /Dashboard


if __name__ == "__main__":
    GUIKitProgram()
    print("> GUIKitProgram - serviço finalizado.")
