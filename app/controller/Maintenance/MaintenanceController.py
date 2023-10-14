import view.Maintenance.MaintenanceView as MaintenanceView
import model.Maintenance.MaintenanceModel as MaintenanceModel
import core.DataImage as CoreDataImage
import base64
from tkinter import PhotoImage, Tk


class MaintenanceController:
    def __init__(self) -> None:
        self.app_title = ''

    def mount_screen(self):
        csCoreDataImage = CoreDataImage.DataImage()
        data_image = csCoreDataImage.get('Maintenance','maintenance')

        csMaintenanceModel = MaintenanceModel.MaintenanceModel()
        data_message = csMaintenanceModel.get_message()

        root_maintenance = Tk()
        title = "{} Maintenance".format(self.app_title)
        root_maintenance.title(title)

        # Maintenance
        wMaintenance = MaintenanceView.MaintenanceView(root_maintenance)
        wMaintenance.data_image = PhotoImage(data=base64.b64decode(data_image))
        wMaintenance.data_message = data_message
        wMaintenance.create()
        # /Maintenance

        root_maintenance.mainloop()