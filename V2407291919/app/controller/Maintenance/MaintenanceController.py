import view.Maintenance.MaintenanceView as MaintenanceView
import model.Maintenance.MaintenanceModel as MaintenanceModel
import core.DataImage as CoreDataImage
import base64
import ttkbootstrap as ttk


class MaintenanceController:
    def __init__(self) -> None:
        self.csMaintenanceModel = MaintenanceModel.MaintenanceModel()
        self.data_content = self.csMaintenanceModel.sd

    def mount_screen(self):
        csCoreDataImage = CoreDataImage.DataImage()
        data_image = csCoreDataImage.get('Maintenance', 'maintenance')
        data_message = self.csMaintenanceModel.get_message()

        root_maintenance = ttk.Window(
            themename=self.data_content["FormDesign"]["Theme"])
        root_maintenance.title("{} - {}".format(
            self.data_content["FormDesign"]["AppTitle"],
            self.data_content["FormDesign"]["Title"]))
        root_maintenance.iconbitmap(self.data_content["FormDesign"]["AppIcon"])

        # Maintenance
        wMaintenance = MaintenanceView.MaintenanceView(root_maintenance)
        wMaintenance.data_image = ttk.PhotoImage(
            data=base64.b64decode(data_image))
        wMaintenance.data_message = data_message
        wMaintenance.set_controller(self)
        wMaintenance.create()
        # /Maintenance

        root_maintenance.mainloop()
