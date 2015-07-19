__author__ = 'Daniel'

import sys
from PySide.QtCore import *
from PySide.QtGui import *
import GUI.ui_menu
import GUI.ui_startwidget
import GUI.ui_gamedialog
import GUI.ui_historywidget

class MenuWidget(QWidget, GUI.ui_menu.Ui_Menu):
    def __init__(self):
        super(MenuWidget, self).__init__()
        self.setupUi(self)
        model = QStringListModel(list(map(str, range(100))))
        self.myListView.setModel(model)


class GameDialog(QDialog, GUI.ui_gamedialog.Ui_Dialog):
    def __init__(self, parent=None):
        super(GameDialog, self).__init__(parent)
        self.parent_component = parent
        self.setupUi(self)
        self.game = parent.game
        self.t = QTimer()
        self.lag = 1


    def start(self):
        x, ok = QInputDialog.getInt(self, "Rounds", "Rounds", 10)
        if not (ok and isinstance(x, int)):
            return
        self.questions_left = x
        self.lcdNumber.display(self.lag)
        self.t.timeout.connect(self.on_timeout)
        self.t.start(1000)
        self.userInputLineEdit.textEdited.connect(self.on_userInputLineEdit_textEdited)
        self.userInputLineEdit.returnPressed.connect(self.on_userInputLineEdit_returnPressed)
        self.show()


    def on_userInputLineEdit_returnPressed(self):
        txt = self.userInputLineEdit.text()
        self.submit_answer(txt)

    def on_userInputLineEdit_textEdited(self, txt):
        if self.parent_component.checkAns(txt):
            self.submit_answer(txt)

    def submit_answer(self, txt):
        self.game.end_timing()
        _, solution, time_taken = self.game.solve_question(int(txt))
        self.lcdNumber.display(time_taken)
        self.questions_left -= 1
        if self.questions_left == 0:
            self.stop_game()
        else:
            self.start_game()

    def on_timeout(self):
        self.lag -= 1
        self.lcdNumber.display(self.lag)
        if self.lag <= 0:
            self.t.stop()
            self.start_game()

    def start_game(self):
        self.game.gen_next_question()
        self.game.start_timing()
        self.userInputLineEdit.setText("")
        self.questionLabel.setText(self.game.current_question.query)

    def stop_game(self):
        self.done()

    def done(self, *args):
        # Cleanup as well
        try:
            self.game.user_score.save_db()
            QMessageBox.information(self, "Statistics", "blah\nblah\nblah")
            self.t.stop()
        except:
            pass
        super(GameDialog, self).done(0)

class StartWidget(QWidget, GUI.ui_startwidget.Ui_Form):
    def __init__(self, parent=None):
        super(StartWidget, self).__init__(parent)
        self.setupUi(self)
        self.quickGameBtn.clicked.connect(parent.start_quick_game)
        self.historyOrSavedBtn.clicked.connect(parent.display_history)
        self.trainingBtn.clicked.connect(parent.start_training)
        self.settingsBtn.clicked.connect(parent.display_settings)

class HistoryDlg(QDialog, GUI.ui_historywidget.Ui_Dialog):
    def __init__(self, parent=None):
        super(HistoryDlg, self).__init__(parent)
        self.parent_component = parent
        self.setupUi(self)
        self.historyTableView.resizeColumnsToContents()
        self.historyTableView.setSortingEnabled(True)

    def set_up_history(self, model):
        self.historyTableView.setModel(model)