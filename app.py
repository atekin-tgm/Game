import sys
import model
#import controller
from simplegame import *
from PyQt5 import QtGui


app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
view = Ui_MainWindow()
view.setupUi(MainWindow)
model = model.Model()
#controller = controller.Controller(view, model)
MainWindow.show()
sys.exit(app.exec_())