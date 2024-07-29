import view.Login.LoginExternalView as LoginExternal
import model.Login.LoginModel as LoginModel
import core.DataImage as CoreDataImage
import core.AppSession as CoreAppSession
import base64
from tkinter import PhotoImage, Tk
from tkinter.messagebox import showerror, showwarning, showinfo


class LoginExternalController:
    def __init__(self) -> None:
        self.app_title = ''
        self.app_icon = ''
        self.title = ''

        self.LoginModel = LoginModel.LoginModel()
        self.sdtLogin = self.LoginModel.getSdtLogin()

    def mount_screen(self):
        csCoreDataImage = CoreDataImage.DataImage()
        data_image = csCoreDataImage.get('Logo','logo')
        data_image_banner = csCoreDataImage.get('Logo','external')

        self.root_LoginExternal = Tk()
        self.root_LoginExternal.title("{} Login".format(self.app_title))
        self.root_LoginExternal.iconbitmap(self.app_icon)
        
        remember = self.LoginModel.getRememberMe()
        remember_username = ''
        
        if remember['remember_me'] == True:
            remember_username = remember['username']

        # LoginExternal
        wLoginExternal = LoginExternal.LoginExternalView(self.root_LoginExternal)
        wLoginExternal.data_image = PhotoImage(data=base64.b64decode(data_image))
        wLoginExternal.data_image_banner = PhotoImage(data=base64.b64decode(data_image_banner))
        wLoginExternal.title = self.title
        wLoginExternal.set_controller(self)
        wLoginExternal.setUsrLgn(remember_username)
        wLoginExternal.create()
        # /LoginExternal

        self.root_LoginExternal.mainloop()
    
    def save(self):
        csCoreAppSession = CoreAppSession.AppSession()

        self.sdtLogin = self.LoginModel.getSdtLogin()
        self.LoginModel.setRememberMe(self.sdtLogin['RememberMe'])
        status_connected = csCoreAppSession.single_login(self.sdtLogin)

        if (status_connected):
            self.root_LoginExternal.destroy()
        else:
            wShowMsg = showwarning('Atenção', 'Verifique usuário e senha!')