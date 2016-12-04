"""
@author: TEKIN Abdurrahim Burak
@date: 2016-11-27
-- Simple game with threads! --
"""

import random
from PySide import QtCore, QtGui

class game_controller:
    """
    Controller class for the game
    """
    def __init__(self, view, model):
        """
        creating all buttons and connecting them to the method checkButton()
        :param view: object of the view class
        :param model: object of the model class
        """
        self.view = view
        self.model = model

        self.buttonText()

        #A friend of mine helped me with the idea of all buttons
        self.buttons = []

        self.buttons.append(self.view.pushButton_1)
        self.buttons.append(self.view.pushButton_2)
        self.buttons.append(self.view.pushButton_3)
        self.buttons.append(self.view.pushButton_4)
        self.buttons.append(self.view.pushButton_5)
        self.buttons.append(self.view.pushButton_6)
        self.buttons.append(self.view.pushButton_7)
        self.buttons.append(self.view.pushButton_8)
        self.buttons.append(self.view.pushButton_9)
        self.buttons.append(self.view.pushButton_10)
        self.buttons.append(self.view.pushButton_11)
        self.buttons.append(self.view.pushButton_12)
        self.buttons.append(self.view.pushButton_13)
        self.buttons.append(self.view.pushButton_14)
        self.buttons.append(self.view.pushButton_15)
        self.view.pushButton_16.clicked.connect(self.newGame)

        #page http://stackoverflow.com/questions/15080731/call-a-function-when-a-button-is-pressed-pyqt
        self.view.pushButton_1.clicked.connect(lambda: self.checkButton(self.view.pushButton_1))
        self.view.pushButton_2.clicked.connect(lambda: self.checkButton(self.view.pushButton_2))
        self.view.pushButton_3.clicked.connect(lambda: self.checkButton(self.view.pushButton_3))
        self.view.pushButton_4.clicked.connect(lambda: self.checkButton(self.view.pushButton_4))
        self.view.pushButton_5.clicked.connect(lambda: self.checkButton(self.view.pushButton_5))
        self.view.pushButton_6.clicked.connect(lambda: self.checkButton(self.view.pushButton_6))
        self.view.pushButton_7.clicked.connect(lambda: self.checkButton(self.view.pushButton_7))
        self.view.pushButton_8.clicked.connect(lambda: self.checkButton(self.view.pushButton_8))
        self.view.pushButton_9.clicked.connect(lambda: self.checkButton(self.view.pushButton_9))
        self.view.pushButton_10.clicked.connect(lambda: self.checkButton(self.view.pushButton_10))
        self.view.pushButton_11.clicked.connect(lambda: self.checkButton(self.view.pushButton_11))
        self.view.pushButton_12.clicked.connect(lambda: self.checkButton(self.view.pushButton_12))
        self.view.pushButton_13.clicked.connect(lambda: self.checkButton(self.view.pushButton_13))
        self.view.pushButton_14.clicked.connect(lambda: self.checkButton(self.view.pushButton_14))
        self.view.pushButton_15.clicked.connect(lambda: self.checkButton(self.view.pushButton_15))

        self.upd()

    def buttonText(self):
        """
        random button display -> random numbers
        """
        list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

        randomindex1 = random.choice(list)
        list.remove(int(randomindex1))
        randomindex2 = random.choice(list)
        list.remove(int(randomindex2))
        randomindex3 = random.choice(list)
        list.remove(int(randomindex3))
        randomindex4 = random.choice(list)
        list.remove(int(randomindex4))
        randomindex5 = random.choice(list)
        list.remove(int(randomindex5))
        randomindex6 = random.choice(list)
        list.remove(int(randomindex6))
        randomindex7 = random.choice(list)
        list.remove(int(randomindex7))
        randomindex8 = random.choice(list)
        list.remove(int(randomindex8))
        randomindex9 = random.choice(list)
        list.remove(int(randomindex9))
        randomindex10 = random.choice(list)
        list.remove(int(randomindex10))
        randomindex11 = random.choice(list)
        list.remove(int(randomindex11))
        randomindex12 = random.choice(list)
        list.remove(int(randomindex12))
        randomindex13 = random.choice(list)
        list.remove(int(randomindex13))
        randomindex14 = random.choice(list)
        list.remove(int(randomindex14))
        randomindex15 = random.choice(list)
        list.remove(int(randomindex15))

        self.view.pushButton_1.setText(str(randomindex1))
        self.view.pushButton_2.setText(str(randomindex2))
        self.view.pushButton_3.setText(str(randomindex3))
        self.view.pushButton_4.setText(str(randomindex4))
        self.view.pushButton_5.setText(str(randomindex5))
        self.view.pushButton_6.setText(str(randomindex6))
        self.view.pushButton_7.setText(str(randomindex7))
        self.view.pushButton_8.setText(str(randomindex8))
        self.view.pushButton_9.setText(str(randomindex9))
        self.view.pushButton_10.setText(str(randomindex10))
        self.view.pushButton_11.setText(str(randomindex11))
        self.view.pushButton_12.setText(str(randomindex12))
        self.view.pushButton_13.setText(str(randomindex13))
        self.view.pushButton_14.setText(str(randomindex14))
        self.view.pushButton_15.setText(str(randomindex15))

    def newGame(self):
        """
        the stats are being resetted
        """
        self.model.spiele += 1
        self.model.übrig = 15
        self.model.korrekt = 0
        self.model.falsch = 0
        self.model.letztes = 1

        for b in self.buttons:
            b.setEnabled(True)

        self.upd()
        self.buttonText()

    def checkButton(self, button):
        """
        the stats are being set
        :param button: pressed button
        """
        if int(button.text()) == self.model.last_one:
            button.setEnabled(False)
            self.model.letztes += 1
            self.model.übrig -= 1
            self.model.korrekt += 1
        else:
            self.model.falsch += 1

        self.upd()

    def upd(self):
        """
        sets and updates the text of the labels
        """
        self.view.label_2.setText(str(self.model.übrig))
        self.view.label_6.setText(str(self.model.korrekt))
        self.view.label_7.setText(str(self.model.falsch))
        self.view.label_8.setText(str(self.model.korrekt + self.model.falsch))
        self.view.label_10.setText(str(self.model.spiele))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    view = Ui_MainWindow()
    view.setupUi(MainWindow)
    model = game_model.Model()
    controller = game_controller.Controller(view, model)
    MainWindow.show()
    sys.exit(app.exec_())