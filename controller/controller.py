from infra.hotkey import hotKey
from view.windowview import Window
from PyQt5 import QtCore, QtWidgets
import sys
class ControlTradutionModule():

    def __init__(self):
        print('controll')

    def controllerTradutionModule(self):
        hotKey()
        self.createWindow()        
    
    def createWindow(self):
        app = QtWidgets.QApplication(sys.argv)
        mainWin = Window()
        mainWin.show()
        sys.exit( app.exec_() )
    
   

