from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QRunnable, pyqtSlot, QThreadPool

from views.UiGameScreen import Ui_Form as UiGameScreen
from views.component import Ui_Frame

from model.Game import Game


class GamePage(QWidget, UiGameScreen):

    closed = pyqtSignal()

    def __init__(self, user):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.model = Game(user['id'])

        self.btnClose.clicked.connect(self.closed)
        self.backBtn.clicked.connect(self.closed)

        self.loadGames()

    def loadGames(self):
        self.gameHistory = self.model.getAllGames()

        for game in self.gameHistory:

            object = Ui_Frame()
            object.label.setText(f"GAMEID\n{game['id']}")
            object.label_2.setText(f"POINTS\n{game['points']}/10")
            object.label_3.setText(f"TIME\n{game['total_time']}s")

            if game["points"] == 10:
                text = "PERFECT"
            elif game['points'] > 7:
                text = "GOOD"
            else:
                text = "BAD"

            object.label_4.setText(f"STATS\n{text}")

            self.verticalLayout.addWidget(object)
