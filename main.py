'''
    MAIN APP renderiza e importa bibliotecas do PYQT5
'''
import views.resQuiz_rc
import views.resRank_rc
import views.resHome_rc
import views.resLogin_rc
import views.resAbout_rc

from PyQt5.QtWidgets import QApplication

from controllers.AuthController import LoginPage

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    quiz = LoginPage()
    app.exec()
