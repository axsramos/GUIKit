from tkinter import BooleanVar, Button, Checkbutton, Entry, Frame, Label, StringVar
import view.UIElements.UIForm as UIForm


class LoginExternalView(UIForm.UIForm):
    def __init__(self, root) -> None:
        self.parent = root
        self.data_image = None
        self.data_image_banner = None
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

    def create(self):
        self.parent.configure(bg="#FFFFFF", border=0)
        frm_body = Frame(self.parent, bg="#FFFFFF")

        # side left
        frm_banner = Frame(frm_body, bg="#FFFFFF")

        frm_group = Frame(frm_banner, bg="#FFFFFF", width=400, height=440)
        lbl_banner = Label(
            frm_group, image=self.data_image_banner, bg="#FFFFFF")
        lbl_banner.pack()
        frm_group.pack()

        frm_banner.pack(side="left")
        # /side left

        # side right
        frm_form = Frame(frm_body, bg="#FFFFFF")

        frm_group = Frame(frm_form, bg="#FFFFFF")
        Label(frm_group, image=self.data_image, text=self.title,
              wraplength=160, compound="left", bg="#FFFFFF").pack(side="left")
        Label(frm_group, text="Entrar", font=("Tahoma", 22),
              bg="#FFFFFF").pack(side="right", padx=30)
        frm_group.pack(fill="x")

        frm_group = Frame(frm_form, bg="#FFFFFF")
        Label(frm_group, text="Entre com suas credenciais de acesso.", font=(
            "Tahoma", 11), anchor="w", bg="#FFFFFF").pack(fill="x", pady=4)
        frm_group.pack(fill="x", padx=35, pady=4)

        frm_group = Frame(frm_form, bg="#FFFFFF")
        Label(frm_group, text="Digite seu e-mail:", font=("Tahoma", 11),
              anchor="w", bg="#FFFFFF").pack(fill="x", pady=4)
        ent_UsrLgn = Entry(
            frm_group, textvariable=self._attUsrLgn, font=("Tahoma", 10))
        ent_UsrLgn.pack(fill="x", ipady=2)
        ent_UsrLgn.bind("<Return>", self._btn_confirmar_click)
        ent_UsrLgn.focus()
        frm_group.pack(fill="x", padx=35, pady=2)

        frm_group = Frame(frm_form, bg="#FFFFFF")
        Label(frm_group, text="Senha:", font=("Tahoma", 11),
              anchor="w", bg="#FFFFFF").pack(fill="x", pady=4)
        ent_UsrPwd = Entry(frm_group, textvariable=self._attUsrPwd, font=(
            "Tahoma", 10), show='*')
        ent_UsrPwd.pack(fill="x", ipady=2)
        ent_UsrPwd.bind("<Return>", self._btn_confirmar_click)
        frm_group.pack(fill="x", padx=35, pady=2)

        frm_group = Frame(frm_form, bg="#FFFFFF")
        Checkbutton(frm_group, text="Lembrar-me", font=("Tahoma", 10), variable=self._chk_lermbar_me,
                    onvalue=True, offvalue=False, bg="#FFFFFF").pack(pady=4, anchor='w')
        frm_group.pack(fill="x", padx=35, pady=2)

        frm_group = Frame(frm_form, bg="#FFFFFF")
        btn_confirmar = Button(frm_group, text="Confirmar",
                               command=self._btn_confirmar_click, font=("Tahoma", 10), width=15)
        btn_confirmar.pack(ipady=2, side="right")
        btn_confirmar.bind("<Return>", self._btn_confirmar_click)

        lbl_recoverpwd = Label(frm_group, text="Recuperar Senha", font=(
            "Tahoma", 10), anchor="w", bg="#FFFFFF")
        # lbl_recoverpwd.pack(ipady=2, side="left")
        frm_group.pack(fill="x", padx=35, pady=2)

        frm_group = Frame(frm_form, bg="#FFFFFF")
        lbl_new_account = Label(frm_group, text="Não tem uma conta? Inscreva-se.",
                                font=("Tahoma", 10), anchor="w", bg="#FFFFFF")
        # lbl_new_account.pack(fill="x", pady=4)
        frm_group.pack(fill="x", padx=35, pady=2)

        frm_form.pack(side="top")
        # /side right

        frm_body.pack(fill="x")

        self.set_size_window(790, 440, 30)
        data_geometry = self.set_geometry(True)
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
