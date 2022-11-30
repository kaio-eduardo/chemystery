'''
    Página Controller do UI QUIZSCREEN
'''
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QObject, QRunnable, pyqtSlot, QThreadPool

from views.UiQuizScreen import Ui_Form as UiQuizScreen
from model.Question import Question as Model
from model.Game import Game


class WorkerSignals(QObject):
    finished = pyqtSignal()
    result = pyqtSignal(list)


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs
        self.fn = fn
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):

        result = self.fn(*self.args, **self.kwargs)

        self.signals.result.emit(result)

        self.signals.finished.emit()


class QuizPage(QWidget, UiQuizScreen):
    '''
        Classe para renderizar a tela de perguntas
    '''

    closed = pyqtSignal()

    def __init__(self, user):
        super().__init__()
        self.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)

        # CONECTA O MODEL PARA A CLASSE
        self.model = Model()
        self.game = Game(user['id'])
        self.threadPool = QThreadPool()

        # DADOS BASICOS DA QUESTAO
        self.questions = []  # Armazena as 10 questões e seus ids
        self.alternatives = []  # Armazena as alternativas de uma questão

        self.cQuestions = 0  # Percorre o array de self.questions

        self.is_right = ''  # armazena a alternativa correta
        self.acertos = 0  # qtd de acertos
        self.total_time = 0  # tempo total para concluir o jogo

        # Lista de btn opções
        self.btnList = [self.resposta1, self.resposta2,
                        self.resposta3, self.resposta4]

        # TIMERS
        self.timer3 = QTimer(self)  # TIMER PARA TEMPO INCIAL
        self.timer3.timeout.connect(self.startCountDown)

        self.timer = QTimer(self)  # TIMER PARA DELAY DEPOIS DE RESPOSTA
        self.timer.timeout.connect(self.showNewQuestion)

        self.timer2 = QTimer(self)  # TIMER PARA TEMPO DE RESPOSTA
        self.timer2.timeout.connect(self.countTime)

        # SET CRONOMETRO
        self.tempoResposta = 40
        self.tempoPreparo = 5
        self.lblTimer.setText(f"{self.tempoResposta}")

        # Atributos para retirar o windows flag
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # Handle click buttons
        self.resposta1.clicked.connect(lambda: self.handleAnswer(
            self.resposta1.text(), self.resposta1))
        self.resposta2.clicked.connect(lambda: self.handleAnswer(
            self.resposta2.text(), self.resposta2))
        self.resposta3.clicked.connect(lambda: self.handleAnswer(
            self.resposta3.text(), self.resposta3))
        self.resposta4.clicked.connect(lambda: self.handleAnswer(
            self.resposta4.text(), self.resposta4))

        self.btnClose.clicked.connect(self.closed)

        # BTN DE VOLTAR AO INICIO
        self.btnBack.clicked.connect(self.closed)

        self.loadGame()

    # =====================
    # TIMER FUNCTIONS
    # =====================

    # TIMER3 FUNCS

    def loadGame(self):
        self.timer3.start(1000)

        worker = Worker(self.loadQuestions)
        worker.signals.result.connect(self.setQuestions)
        worker.signals.finished.connect(lambda: print('TERMINOU O ROLE'))

        self.threadPool.start(worker)

    def loadQuestions(self):
        return self.model.getQuestions()

    def setQuestions(self, questions):
        self.questions = questions

    def startCountDown(self):
        self.tempoPreparo -= 1
        if self.tempoPreparo == 0:
            self.stackedWidget.setCurrentIndex(0)
            self.timer3.stop()
            self.getQuestionsAlternatives()
            self.startTimer()
        self.prepLbl.setText(str(self.tempoPreparo))

    # TIMER2 FUNCS
    def startTimer(self):
        self.timer2.start(1000)

    def countTime(self):
        self.tempoResposta -= 1
        self.total_time += 1
        self.lblTimer.setText(f"{self.tempoResposta}")
        if self.tempoResposta == 0:
            self.showNewQuestion()

    # STOP TIMERS 1 E 2
    def endTimer(self):
        self.timer.stop()
        self.timer2.stop()

        self.tempoResposta = 40
        self.lblTimer.setText(f"{self.tempoResposta}")

    # ========================
    #   CARREGAR NOVA QUESTAO
    # ========================

    def getQuestionsAlternatives(self):
        id = self.questions[self.cQuestions]['id']
        self.alternatives = self.model.getAlternatives(id)
        self.showQuestion()
        print(self.alternatives)

    def showQuestion(self):
        self.lblQuestion.setText(
            f"{self.cQuestions + 1} - {self.questions[self.cQuestions]['question']} ")
        for i in range(4):
            self.btnList[i].setText(self.alternatives[i][2])
            if self.alternatives[i][3]:
                self.is_right = self.alternatives[i][2]

    # =======================
    # VERIFICA SE A RESPOSTA ESTÁ CERTA OU ERRADA
    # =======================

    def handleAnswer(self, alternative, btn):
        if self.is_right == alternative:
            btn.setStyleSheet(
                "color: black; background-color: rgba(150,235,152,255)")
            self.acertos += 1
        else:
            btn.setStyleSheet(
                "color: rgba(1, 0, 0, 255); background-color: rgba(235,150,152,255)")
        self.disableButtons()
        self.timer.start(250)

    # =========================
    # Reinicia a Tela de questões com uma nova questão
    # =========================

    def showNewQuestion(self):
        print(self.cQuestions, len(self.questions))
        self.cQuestions += 1
        self.endTimer()
        if self.cQuestions < len(self.questions):
            self.getQuestionsAlternatives()
            self.resetPage()
            self.startTimer()
        else:
            self.showStats()
            print(f"ACERTOS: {self.acertos}")

    # ======================
    # TELA DE ENCERRAMENTO
    # ======================
    def showStats(self):
        self.game.createGame(self.acertos, self.total_time)
        for question in self.questions:
            self.game.insertQuestions(question['id'])
            # self.game.insertQuestions(question['id'])
        self.stackedWidget.setCurrentIndex(1)
        self.btnBack.show()
        self.resultlbl.setText(
            f"ACERTOS: {self.acertos}\nTEMPO TOTAL: {self.total_time} s")

    # =======================
    # utils para funcionamento
    # =======================

    # disableButtons faz com que o usuario depois de selecionar uma resposta não possa selecionar outra

    def disableButtons(self):
        for btn in self.btnList:
            btn.setEnabled(False)

    # Ativa os botões para a próxima questão e reseta o style
    def resetPage(self):
        for btn in self.btnList:
            btn.setEnabled(True)
            btn.setStyleSheet(
                'color: rgba(165, 4, 255, 255); background-color: rgba(255,255,255,255)')
