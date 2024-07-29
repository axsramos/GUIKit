from tkinter import BooleanVar, Button, Checkbutton, Entry, Frame, Label, StringVar
import view.UIElements.UIForm as UIForm


class LoginInternalView(UIForm.UIForm):
    def __init__(self, root) -> None:
        self.parent = root
        self.data_image = None
        self.title = ''
        self.controller = None

        self._attUsrLgn = StringVar()
        self._attUsrPwd = StringVar()
        self._chk_lermbar_me = BooleanVar()

    def set_controller(self, controller):
        self.controller = controller

    def setUsrLgn(self, data_content):
        self._attUsrLgn.set(data_content)
        self._chk_lermbar_me.set(True)

    def setUsrPwd(self, data_content):
        self._attUsrPwd.set(data_content)

    def create(self):
        frm_body = Frame(self.parent)

        frm_group = Frame(frm_body)
        Label(frm_group, image=self.data_image, text=self.title,
              wraplength=160, compound="left").pack(side="left")
        Label(frm_group, text="Entrar", font=(
            "Tahoma", 22)).pack(side="right", padx=30)
        frm_group.pack(fill="x")

        frm_group = Frame(frm_body)
        Label(frm_group, text="Entre com suas credenciais de acesso.",
              font=("Tahoma", 11), anchor="w").pack(fill="x", pady=4)
        frm_group.pack(fill="x", padx=35, pady=4)

        frm_group = Frame(frm_body)
        Label(frm_group, text="Digite seu e-mail:",
              font=("Tahoma", 11), anchor="w").pack(fill="x", pady=4)
        ent_UsrLgn = Entry(
            frm_group, textvariable=self._attUsrLgn, font=("Tahoma", 10))
        ent_UsrLgn.pack(fill="x", ipady=2)
        ent_UsrLgn.focus()
        ent_UsrLgn.bind("<Return>", self._btn_confirmar_click)
        frm_group.pack(fill="x", padx=35, pady=2)

        frm_group = Frame(frm_body)
        Label(frm_group, text="Senha:", font=("Tahoma", 11),
              anchor="w").pack(fill="x", pady=4)
        ent_UsrPwd = Entry(frm_group, textvariable=self._attUsrPwd, font=(
            "Tahoma", 10), show='*')
        ent_UsrPwd.pack(fill="x", ipady=2)
        ent_UsrPwd.bind("<Return>", self._btn_confirmar_click)
        frm_group.pack(fill="x", padx=35, pady=2)

        frm_group = Frame(frm_body)
        Checkbutton(frm_group, text="Lembrar-me", font=("Tahoma", 10),
                    variable=self._chk_lermbar_me, onvalue=True, offvalue=False).pack(pady=4, anchor='w')
        frm_group.pack(fill="x", padx=35, pady=2)

        frm_group = Frame(frm_body)
        btn_confirmar = Button(frm_group, text="Confirmar",
                               command=self._btn_confirmar_click, font=("Tahoma", 10), width=15)
        btn_confirmar.pack(ipady=2, side="right")
        btn_confirmar.bind("<Return>", self._btn_confirmar_click)
        
        lbl_recoverpwd = Label(
            frm_group, text="Recuperar Senha", font=("Tahoma", 10), anchor="w")
        # lbl_recoverpwd.pack(ipady=2, side="left")
        frm_group.pack(fill="x", padx=35, pady=2)

        frm_group = Frame(frm_body)
        lbl_new_account = Label(
            frm_group, text="Não tem uma conta? Inscreva-se.", font=("Tahoma", 10), anchor="w")
        # lbl_new_account.pack(fill="x", pady=4)
        frm_group.pack(fill="x", padx=35, pady=2)

        frm_body.pack(fill="x")

        self.set_size_window(400, 390, 30)
        data_geometry = self.set_geometry()
        self.parent.geometry(data_geometry)
        self.parent.resizable(False, False)

    def _btn_confirmar_click(self, event=None):
        if self.controller:
            self.controller.LoginModel.setUsrLgn(self._attUsrLgn.get())
            self.controller.LoginModel.setUsrPwd(self._attUsrPwd.get())
            self.controller.LoginModel.setRememberMe(self._chk_lermbar_me.get())
            self.controller.save()

    def _lbl_recoverpwd_click(self):
        print('recoverpwd_click')

    def _lbl_new_account_click(self):
        print('new_account_click')
    
    
