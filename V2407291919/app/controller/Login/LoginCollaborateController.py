import view.Login.LoginCollaborateView as LoginCollaborate
import model.Login.LoginModel as LoginModel
import core.DataImage as CoreDataImage
import core.AppSession as CoreAppSession
import base64
from tkinter import PhotoImage, Tk
from tkinter.messagebox import showerror, showwarning, showinfo


class LoginCollaborateController:
    def __init__(self) -> None:
        self.app_title = ''
        self.app_icon = ''
        self.title = ''

        self.LoginModel = LoginModel.LoginModel()
        self.sdtLogin = self.LoginModel.getSdtLogin()
    
    def mount_screen(self):
        csCoreDataImage = CoreDataImage.DataImage()
        data_image = csCoreDataImage.get('Logo','logo')
        data_image_banner = csCoreDataImage.get('Logo','collaborate')

        self.root_loginCollaborate = Tk()
        self.root_loginCollaborate.title("{} Login".format(self.app_title))
        self.root_loginCollaborate.iconbitmap(self.app_icon)
        
        remember = self.LoginModel.getRememberMe()
        remember_username = ''
        
        if remember['remember_me'] == True:
            remember_username = remember['username']

        # LoginCollaborate
        wLoginCollaborate = LoginCollaborate.LoginCollaborateView(self.root_loginCollaborate)
        wLoginCollaborate.data_image = PhotoImage(data=base64.b64decode(data_image))
        wLoginCollaborate.data_image_banner = PhotoImage(data=base64.b64decode(data_image_banner))
        wLoginCollaborate.title = self.title
        wLoginCollaborate.set_controller(self)
        wLoginCollaborate.setUsrLgn(remember_username)
        wLoginCollaborate.create()
        # /LoginCollaborate

        self.root_loginCollaborate.mainloop()
    
    def save(self):
        csCoreAppSession = CoreAppSession.AppSession()

        self.sdtLogin = self.LoginModel.getSdtLogin()
        self.LoginModel.setRememberMe(self.sdtLogin['RememberMe'])
        status_connected = csCoreAppSession.single_login(self.sdtLogin)

        if (status_connected):
            self.root_loginCollaborate.destroy()
        else:
            wShowMsg = showwarning('Atenção', 'Verifique usuário e senha!')