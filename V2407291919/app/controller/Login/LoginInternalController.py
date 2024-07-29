import view.Login.LoginInternalView as LoginInternal
import model.Login.LoginModel as LoginModel
import core.DataImage as CoreDataImage
import core.AppSession as CoreAppSession
import base64
from tkinter import PhotoImage, Tk
from tkinter.messagebox import showerror, showwarning, showinfo


class LoginInternalController:
    def __init__(self) -> None:
        self.app_title = ''
        self.app_icon = ''
        self.title = ''
        self.title = ''

        self.LoginModel = LoginModel.LoginModel()
        self.sdtLogin = self.LoginModel.getSdtLogin()
    
    def mount_screen(self):
        csCoreDataImage = CoreDataImage.DataImage()
        data_image = csCoreDataImage.get('Logo','logo')

        self.root_loginInternal = Tk()
        self.root_loginInternal.title( "{} Login".format(self.app_title))
        self.root_loginInternal.iconbitmap(self.app_icon)

        remember = self.LoginModel.getRememberMe()
        remember_username = ''
        
        if remember['remember_me'] == True:
            remember_username = remember['username']
        
        # LoginInternal
        wLoginInternal = LoginInternal.LoginInternalView(self.root_loginInternal)
        wLoginInternal.data_image = PhotoImage(data=base64.b64decode(data_image))
        wLoginInternal.title = self.title
        wLoginInternal.set_controller(self)
        wLoginInternal.setUsrLgn(remember_username)
        wLoginInternal.create()
        # /LoginInternal

        self.root_loginInternal.mainloop()
    
    def save(self):
        csCoreAppSession = CoreAppSession.AppSession()

        self.sdtLogin = self.LoginModel.getSdtLogin()
        self.LoginModel.setRememberMe(self.sdtLogin['RememberMe'])
        status_connected = csCoreAppSession.single_login(self.sdtLogin)

        if (status_connected):
            self.root_loginInternal.destroy()
        else:
            wShowMsg = showwarning('Atenção', 'Verifique usuário e senha!')
        
    