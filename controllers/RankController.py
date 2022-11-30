from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QRunnable, pyqtSlot, QThreadPool

from views.UiRankScreen import Ui_Form as UiRankScreen

from model.User import User


class WorkerSignals(QObject):
    finished = pyqtSignal()
    result = pyqtSignal()


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.signals = WorkerSignals()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):

        self.fn(*self.args, **self.kwargs)
        self.signals.result.emit()
        self.signals.result.connect(lambda: print("teste"))
        self.signals.finished.emit()


class RankPage(QWidget, UiRankScreen):

    closed = pyqtSignal()

    def __init__(self, user):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.model = User(user['id'])
        self.threadpool = QThreadPool()
        self.user = user

        self.rankList = [self.rank1lbl, self.rank2lbl,
                         self.rank3lbl, self.rank4lbl, self.rank5lbl]

        self.btnClose.clicked.connect(self.closed)
        self.backBtn.clicked.connect(self.closed)

        self.loadRank()

    def loadRank(self):
        worker = Worker(self.loadData)
        worker.signals.result.connect(self.setData)
        worker.signals.finished.connect(lambda: print('TERMINOU O ROLE'))

        self.threadpool.start(worker)

    def loadData(self):

        self.games = self.model.countGames()
        print(self.games)
        if self.games['games'] != 0:
            self.points = self.model.getBestGame()
            self.pRank = self.model.getPersonalRank()
        else:
            self.points = 0
            self.pRank = {'user_rank': "##"}
        self.rank = self.model.getGlobalRank()

    def setData(self):
        self.ranklbl.setText(f"#{self.pRank['user_rank']}")
        self.bestlbl.setText(f"{self.points}/10")
        self.gameslbl.setText(str(self.games['games']))

        print(self.rank)

        for i in range(len(self.rankList)):
            try:
                text = f"{self.rank[i]['username']}\n{self.rank[i]['grade']}/10"
                if self.rank[i]['username'] == self.user['username']:
                    self.rankList[i].setStyleSheet(
                        "color: rgba(165,4,255,255)")
            except IndexError:
                text = "---"

            self.rankList[i].setText(text)
