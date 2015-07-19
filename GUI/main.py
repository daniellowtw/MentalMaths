__author__ = 'Daniel'

import platform
from PySide.QtCore import *
from PySide.QtGui import *
import GUI.ui_mainwindow
from GUI.component import *
from Game import Game
from GUI.models import MyHistoryTableModel
from UserData import config
from utility import is_debug_mode, __version__


class MainWindow(QMainWindow, GUI.ui_mainwindow.Ui_MainWindow):
    def keyPressEvent(self, event):
        if is_debug_mode():
            print('key: %s -' % hex(event.key()))
            print('modifiers:', hex(int(event.modifiers())))

    def checkAns(self, user_input):
        if is_debug_mode():
            print(self.game.current_question.answer)
        try:
            return float(user_input) == self.game.current_question.answer
        except:
            return False

    def start_quick_game(self):
        g = GameDialog(self)
        g.start()

    def start_training(self):
        # TODO: Create a new dialog asking for type
        self.start_quick_game()

    def display_settings(self):
        # TODO: Create interface to change settings
        QMessageBox.information(self, "Settings", "Coming soon")

    def display_history(self):
        """Create dumb dialog and display table"""
        data = []
        for q in self.game.history.values():
            data.append([q.query.strip(), len(q.correct_times), len(q.wrong_times)])
        header = ['Query', 'Correct', 'Wrong']
        model = MyHistoryTableModel(data, header, self)

        h = HistoryDlg(self)
        h.set_up_history(model)
        h.show()

    def display_about(self):
        QMessageBox.about(self, "About Mental Math",
                          """<b>Mental Math</b> v %s
                          <br>
                          Made by Daniel Low
                          <p>This application can be used to train your mental calculation.
                          <p>Running on Python %s on %s""" % (
                          __version__, platform.python_version(), platform.system()))

    def __init__(self, game):
        self.game = game
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Mental Math trainer")
        # self.statusBar.showMessage('Ready')
        self.setCentralWidget(StartWidget(self))
        self.actionQuit.triggered.connect(self.close)
        self.actionQuick_Game.triggered.connect(self.start_quick_game)
        self.actionTraining.triggered.connect(self.start_training)
        self.actionHistory.triggered.connect(self.display_history)
        self.actionAbout.triggered.connect(self.display_about)


def main():
    app = QApplication(sys.argv)
    g = Game()
    f = MainWindow(g)
    f.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
