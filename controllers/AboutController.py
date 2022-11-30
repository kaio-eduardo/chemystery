from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, pyqtSignal

from views.UiAboutScreen import Ui_Form as UiAboutScreen


class AboutPage(QWidget, UiAboutScreen):
    closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.backBtn.clicked.connect(self.closed)
