class UIForm:
    def __init__(self) -> None:
        pass

    def set_size_window(self, sz_width, sz_height, sz_tskbar):
        self.size_form_width = sz_width
        self.size_form_height = sz_height
        self.size_form_tskbar = sz_tskbar

    def set_size_extreme_small(self):
        self.size_form_width = 360
        self.size_form_height = 280
        self.size_form_tskbar = 15

    def set_size_small(self):
        self.size_form_width = 680
        self.size_form_height = 480
        self.size_form_tskbar = 22

    def set_size_medium(self):
        self.size_form_width = 790
        self.size_form_height = 500
        self.size_form_tskbar = 30

    def set_size_large(self):
        self.size_form_width = 1020
        self.size_form_height = 580
        self.size_form_tskbar = 38

    def set_geometry(self, center=True):
        if center == True:
            sww = self.parent.winfo_screenwidth()
            swh = self.parent.winfo_screenheight()

            psx = int((sww / 2) - (self.size_form_width / 2))
            psy = int((swh / 2) - (self.size_form_height / 2)) - \
                self.size_form_tskbar

            data_geometry = '{}x{}+{}+{}'.format(
                self.size_form_width, self.size_form_height, psx, psy)
        else:
            data_geometry = '{}x{}'.format(
                self.size_form_width, self.size_form_height)

        return data_geometry
