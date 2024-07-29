import model.UIElements.FormDesign as FormDesign

class DashboardModel(FormDesign.FormDesignModel):
    def __init__(self) -> None:
        self.sd = self.structured_data()
        self.sd["FormDesign"]["Title"] = "Dashboard"
