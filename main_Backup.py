from types import MethodType

from info import Ui_Info
from SignUp import Ui_signUp
from login import Ui_login , overWriteMouse
import win32gui,win32api,win32con

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget , QDialog
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

def CheckConsole():
    console = win32api.GetConsoleTitle()
    handle= win32gui.FindWindow(0,console)
    win32gui.ShowWindow(handle,0)
    print(handle)

if __name__ == "__main__":
    import sys
    # CheckConsole()
    app = QtWidgets.QApplication(sys.argv)
    login = QWidget()
    ui = Ui_login()
    ui.setupUi(login)
    overWriteMouse(login)
    login.show()
    sys.exit(app.exec_())


from info import Ui_Info
from PyQt5.QtCore import Qt
from SignUp import Ui_signUp
from types import MethodType


def overWriteMouse(window):

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.setCursor(Qt.OpenHandCursor)
            self.m_drag = True
            self.m_DragPosition = event.globalPos()-self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and Qt.LeftButton:
                self.move(event.globalPos()-self.m_DragPosition)#move将窗口移动到指定位置
                event.accept()
        except AttributeError:
            print("error")
            pass

    def mouseReleaseEvent(self, event):

        if event.button()==Qt.LeftButton:
            self.m_drag = False
            self.unsetCursor()

    window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    window.mouseMoveEvent = MethodType(mouseMoveEvent,window)
    window.mousePressEvent = MethodType(mousePressEvent,window)
    window.mouseReleaseEvent = MethodType(mouseReleaseEvent,window)
