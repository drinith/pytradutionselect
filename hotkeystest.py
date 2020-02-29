from pynput import keyboard
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__()
        self.hotKey()
    # function hotkey     
    def hotKey(self):
        # The key combination to check

        COMBINATIONS = [
            {keyboard.Key.shift, keyboard.KeyCode(char='a')},
            {keyboard.Key.shift, keyboard.KeyCode(char='A')}
        ]
        # The currently active modifiers
        current = set()

        def execute():
            print ("Do Something")

        def on_press(key):
            if any([key in COMBO for COMBO in COMBINATIONS]):
                current.add(key)
                if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
                    execute()

        def on_release(key):
            if any([key in COMBO for COMBO in COMBINATIONS]):
                current.remove(key)

        #with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        #    listener.join()
        listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release)
        listener.start()





#main to test instance of class

if __name__=="__main__":
 
    root = QApplication(sys.argv)
    app = Window()
    app.show()
    
    sys.exit(root.exec_())
   
    
