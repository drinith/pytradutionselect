from pynput import keyboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize   
import sys

class Window(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(640, 480))
        
        self.setWindowTitle("Hello world - pythonprogramminglanguage.com") 

        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)   

        gridLayout = QGridLayout(self)     
        centralWidget.setLayout(gridLayout)  

        title = QLabel("Hello World from PyQt", self) 
        title.setAlignment(QtCore.Qt.AlignCenter) 
        gridLayout.addWidget(title, 0, 0)  
        #self.hotKey()
    
    
    # function hotkey     
    def hotKey(self):
        # The key combination to check

        COMBINATIONS = [
            {keyboard.Key.shift, keyboard.KeyCode(char='a')},
            {keyboard.Key.shift, keyboard.KeyCode(char='A')}
        ]
        # The currently active modifiers
        current = set()

         #with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        #    listener.join()
        listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release)
        listener.start()

        def execute(self):
            print ("Do Something")

        def on_press(key):
            if any([key in COMBO for COMBO in COMBINATIONS]):
                current.add(key)
                if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
                    execute()

        def on_release(key):
            if any([key in COMBO for COMBO in COMBINATIONS]):
                current.remove(key)

       

if __name__=="__main__":
    
    root = QtWidgets.QApplication(sys.argv)
    app = Window()
    app.show
    sys.exit(root.exec_())
   
    
