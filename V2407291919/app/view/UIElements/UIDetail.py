import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class UIDetail:
    def __init__(self, root, parent, controller, data_content) -> None:
        self.root_parent = root
        self.parent = parent
        self.controller = controller
        self.data_content = data_content
        
    def create_header(self):
        self.v_msg_display = ttk.StringVar()
        
        # id_user_session = "USER:{} | ID:{}".format(self.data_content["FormSession"]["user"], self.data_content["FormSession"]["id"])
        id_user_session = "{} | {}".format(self.data_content["FormSession"]["user"], self.data_content["FormSession"]["id"])

        frm_group = ttk.Frame(self.parent, bootstyle=ttk.DEFAULT)
        ttk.Label(frm_group, text=id_user_session, font=(
            "Tahoma", 10), bootstyle=ttk.DEFAULT).pack(anchor="e", padx=2, side="right")
        ttk.Label(frm_group, textvariable=self.v_msg_display, font=(
            "Tahoma", 10), bootstyle=ttk.DEFAULT).pack(anchor="e", padx=2, side="right")
        frm_group.pack(fill="x")

    def create_footer(self):
        frm_group = ttk.Frame(self.parent, bootstyle=ttk.DEFAULT)

        btn_fechar = ttk.Button(frm_group, text="Fechar",
                            command=self._btClose_click, width=12, padding=8, bootstyle=ttk.DARK)
        btn_fechar.pack(side="left", padx=4, pady=2)
        btn_fechar.bind("<Return>", self._btClose_click)

        btn_confirmar = ttk.Button(frm_group, text="Confirmar",
                               command=self._btConfirm_click, width=12, padding=8, bootstyle=SUCCESS)
        btn_confirmar.pack(side="left", padx=4, pady=2)
        btn_confirmar.bind("<Return>", self._btConfirm_click)

        btn_editar = ttk.Button(frm_group, text="Editar",
                            command=self._btUpdate_click, width=12, padding=8, bootstyle=ttk.PRIMARY)
        btn_editar.pack(side="left", padx=4, pady=2)
        btn_editar.bind("<Return>", self._btUpdate_click)

        btn_excluir = ttk.Button(frm_group, text="Excluir",
                             command=self._btDelete_click, width=12, padding=8, bootstyle=ttk.DANGER)
        btn_excluir.pack(side="left", padx=4, pady=2)
        btn_excluir.bind("<Return>", self._btDelete_click)

        btn_options = ttk.Button(frm_group, text="Opções",
                             command=self._btOptions_click, width=12, padding=8, bootstyle=ttk.SECONDARY)
        btn_options.pack(side="left", padx=4, pady=2)
        btn_options.bind("<Return>", self._btOptions_click)

        frm_group.pack(fill="x", padx=5, pady=5, anchor="se")

        self.root_parent.bind("<Any-KeyPress>", self._press_key_shortcut)

    def set_top_message_display(self, message_out=''):
        self.v_msg_display.set(message_out)

    def _btClose_click(self, event=None):
        if self.controller:
            self.controller._close()

    def _btConfirm_click(self, event=None):
        if self.controller:
            self.controller._confirm()

    def _btUpdate_click(self, event=None):
        if self.controller:
            self.controller._update()

    def _btDelete_click(self, event=None):
        if self.controller:
            self.controller._delete()

    def _btOptions_click(self, event=None):
        if self.controller:
            self.controller._options()

    def _press_key_shortcut(self, event):
        if (event.keysym == 'f' or event.keysym == 'F'):
            self._btClose_click()

        if (event.keysym == 'c' or event.keysym == 'C'):
            self._btConfirm_click()

        if (event.keysym == 'e' or event.keysym == 'E'):
            self._btUpdate_click()

        if (event.keysym == 'x' or event.keysym == 'X'):
            self._btDelete_click()

        if (event.keysym == 'o' or event.keysym == 'O'):
            self._btOptions_click()
