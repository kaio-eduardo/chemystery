from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, pyqtSignal

from controllers.QuizController import QuizPage
from controllers.RankController import RankPage
from controllers.AboutController import AboutPage
from controllers.GameController import GamePage

from views.UiHomeScreen import Ui_MainWindow as Ui_HomeWindow

# ==============================
#  Página inicial
# ==============================


class MainPage(QMainWindow, Ui_HomeWindow):

    closed = pyqtSignal()

    def __init__(self, user):
        super().__init__()
        self.setupUi(self)

        # Tranparent background attributes
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.user = user

        self.lblUser.setText(self.user['username'].split(" ")[0].upper())

        self.btnClose.clicked.connect(self.log_out)

        # NAVIGATION BUTTONS
        self.startBtn.clicked.connect(self.goToQuestion)
        self.rankBtn.clicked.connect(self.goToRank)
        self.aboutBtn.clicked.connect(self.goToAbout)
        self.gamesBtn.clicked.connect(self.goToGames)

    # =======================================
    #   QUESTION PAGE
    # =======================================
    def goToQuestion(self):
        self.hide()
        self.pageQuiz = QuizPage(self.user)
        self.pageQuiz.show()
        self.pageQuiz.closed.connect(self.closeQuestion)

    def closeQuestion(self):
        self.pageQuiz.close()
        self.show()

    # ========================================
    #   RANK PAGE
    # ========================================
    def goToRank(self):
        self.hide()
        self.pageRank = RankPage(self.user)
        self.pageRank.show()
        self.pageRank.closed.connect(self.closeRank)

    def closeRank(self):
        self.pageRank.close()
        self.show()

    # ========================================
    #   ABOUT PAGE
    # ========================================
    def goToAbout(self):
        self.hide()
        self.pageAbout = AboutPage()
        self.pageAbout.show()
        self.pageAbout.closed.connect(self.closeAbout)

    def closeAbout(self):
        self.pageAbout.close()
        self.show()

    # ========================================
    #   Game PAGE
    # ========================================
    def goToGames(self):
        self.hide()
        self.pageGame = GamePage(self.user)
        self.pageGame.show()
        self.pageGame.closed.connect(self.closeGame)

    def closeGame(self):
        self.pageGame.close()
        self.show()

    # ==========================================
    # LOG OUT
    # =========================================
    def log_out(self):
        self.closed.emit()
