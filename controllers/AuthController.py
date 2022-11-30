from PyQt5.QtWidgets import QWidget, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
from controllers.MainController import MainPage
from views.UiLoginScreen import Ui_Form as Ui_LoginScreen

from model.User import User as Model


class LoginPage(QWidget, Ui_LoginScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.model = Model()

        self.loginBtn.clicked.connect(self.handleLogin)
        self.registerBtn.clicked.connect(self.handleRegister)

        self.goToRegister.clicked.connect(self.goToRegisterPage)
        self.goToLogin.clicked.connect(self.goToLoginPage)
        self.close_label.mousePressEvent = self.teste
        self.close_label_2.mousePressEvent = self.teste

        #self.listRegister = self.page_2.findChildren(QLineEdit)

        self.show()

    def handleLogin(self):
        username = self.userText.text()
        password = self.passwordText.text()

        erros = False
        erros_msg = ''

        if len(username) < 5 or len(password) < 5:
            erros_msg += "Valores menores que 8 digitos\n"
            erros = True

        if not erros:
            self.user = self.model.getUser(username, password)

            if self.user['userExists'] != 1:
                QMessageBox.critical(
                    self, 'ERROR', "Senha ou usuario invalidos")
            else:
                self.clearInputs([self.userText, self.passwordText])
                self.startApp()
        else:
            QMessageBox.critical(self, 'ERROR', erros_msg)

        erros = False
        erros_msg = ''

    def handleRegister(self):
        # VERIFICAÇÃO DE VALORES - MUDAR PARA UTILS DEPOIS ***

        newUser = {
            "username": self.regUserText.text(),
            "password": self.regPasswordText.text(),
            "cPassword": self.regCPasswordtxt.text(),
            "email": self.regEmailTxt.text()
        }

        erros = False
        erros_msgs = ''

        if len(newUser["username"]) < 8:
            erros_msgs += "Username com poucos digitos\n"
            erros = True

        if len(newUser["password"]) < 8:
            erros_msgs += "senha com poucos digitos\n"
            erros = True

        if newUser['password'] != newUser["cPassword"]:
            erros_msgs += "Senhas não batem!"
            erros = True

        if not erros:
            if self.model.createUser(newUser):
                QMessageBox.information(self, "INFO", "User cadastrado")
                self.clearInputs([self.regUserText, self.regPasswordText,
                                 self.regCPasswordtxt, self.regEmailTxt])
                self.goToLoginPage()
            else:
                QMessageBox.information(
                    self, "INFO", "Username ou email já em uso")
        else:
            QMessageBox.critical(self, "ERROR", erros_msgs)

        erros = False
        erros_msgs = ''

    def goToRegisterPage(self):
        self.stackedWidget.setCurrentIndex(1)

    def goToLoginPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def startApp(self):
        self.mainApp = MainPage(self.user)
        self.mainApp.show()
        self.mainApp.closed.connect(self.log_out)
        self.close()

    def log_out(self):
        self.mainApp.close()
        self.show()

    def clearInputs(self, inputs):
        for input in inputs:
            input.setText('')

    def teste(self, *args, **kargs):
        self.close()
