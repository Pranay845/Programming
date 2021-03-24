"""
PyQt5 Module is for Making GUIs.
"""

from typing import Union
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget, QMessageBox
import sys


def clicked():
    print("you have pushed me")


def window():
    app1 = QApplication(sys.argv)  # setting the app
    win = QMainWindow()  # making window
    win.setGeometry(100, 100, 100,
                    100)  # place for window first two arguments for placing of the window on screen remaining for
    # The size of window
    win.setWindowTitle("abc")  # title for window
    label = QtWidgets.QLabel(win)  # label for window
    label.setText("python")  # text for label
    label.move(50, 50)  # placing the label
    b = QtWidgets.QPushButton(win)  # made a button
    b.setText("push me")  # given text
    b.clicked.connect(clicked)  # added a event
    win.show()  # to show the app
    sys.exit(app1.exec_())  # for a clean exit


window()  # called the function


# Topic: Using Classes and Objects
class MyWindow(QMainWindow):  # made a class which inherent from Qmainwindow
    def __init__(self):  # init
        super(MyWindow, self).__init__()  # the init of Q main window
        self.b = QtWidgets.QPushButton(self)
        self.label = QtWidgets.QLabel(self)
        self.setGeometry(100, 100, 100, 100)  # self makes the following as a global widget
        self.setWindowTitle("abc")
        self.initUI()  # for the label and button

    def initUI(self):
        self.label.setText("python")
        self.label.move(50, 50)
        self.b.setText("push me")
        self.b.clicked.connect(self.clicked)  # self for the function is because to see in only class

    def clicked(self):
        self.setWindowTitle("abcd")
        self.label.setText("you pressed button")
        self.update()  # a method for changing width

    def update(self):
        self.label.adjustSize()  # for changing width


def window():  # the method which makes app
    app2 = QApplication(sys.argv)
    win = MyWindow()
    win.setWindowTitle("abc")
    win.show()
    sys.exit(app2.exec_())


window()


# Topic: Menus
class Ui_MainWindow(object):

    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow")  # creating mainwindow
        MainWindow1.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)  # creating central widget
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)  # a label
        self.label.setGeometry(QtCore.QRect(140, 100, 301, 321))

        font = QtGui.QFont()  # designing of label
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)

        self.label.setFont(font)  # adding to widget
        self.label.setObjectName("label")
        MainWindow1.setCentralWidget(self.centralwidget)  # adding to mainwidget
        self.menubar = QtWidgets.QMenuBar(MainWindow1)  # menubar
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")  # menubar
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")  # file menu
        MainWindow1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)  # status bar
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)  # packed it
        self.actionnew = QtWidgets.QAction(MainWindow1)  # new submenu
        self.actionnew.setObjectName("actionnew")
        self.actionsave = QtWidgets.QAction(MainWindow1)  # save submenu
        self.actionsave.setObjectName("actionsave")
        self.menufile.addAction(self.actionnew)  # command for menu
        self.menufile.addAction(self.actionsave)  # command for menu
        self.menufile.addSeparator()  # separator(a line)
        self.menubar.addAction(self.menufile.menuAction())  # action for big menu

        self.retranslateUi(MainWindow1)  # for changing names
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)  # super pack

        self.actionnew.triggered.connect(lambda: self.clicking(
            "new was not clicked"))  # both for changing text of label triggered because for shortcut is there
        self.actionsave.triggered.connect(lambda: self.clicking("save was not clicked"))

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow", "MainWindow"))  # name of window
        self.label.setText(_translate("MainWindow", "TextLabel"))  # name of label

        self.menufile.setTitle(_translate("MainWindow", "file"))  # name of menus

        self.actionnew.setText(_translate("MainWindow", "new"))  # name of menus
        self.actionnew.setStatusTip(_translate("MainWindow", "press it"))  # the status tip(to show in status bar)
        self.actionnew.setShortcut(_translate("MainWindow", "Ctrl+N"))  # a keyboard shortcut

        self.actionsave.setText(_translate("MainWindow", "save"))  # name of menus
        self.actionsave.setStatusTip(
            _translate("MainWindow", "don\'t press it"))  # the status tip(to show in status bar
        self.actionsave.setShortcut(_translate("MainWindow", "Ctrl+S"))  # a keyboard shortcut

    def clicking(self, text):
        self.label.setText(text)  # for changing label
        self.label.adjustSize()  # for the conivence


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)  # making hte app
    MainWindow = QtWidgets.QMainWindow()  # making main window
    ui = Ui_MainWindow()  # instance of class
    ui.setupUi(MainWindow)  # method for making
    MainWindow.show()  # showing
    sys.exit(app.exec_())  # clean exit


# Topic: Images
class Ui_MainWindow1(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow")  # setting up the mainwindow
        MainWindow2.resize(543, 445)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)  # making the central widget
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)  # making the label
        self.label.setGeometry(QtCore.QRect(10, 0, 521, 321))  # size of label

        self.label.setPixmap(QtGui.QPixmap("first.png"))  # a image in label
        self.label.setScaledContents(True)  # for the convience
        self.label.setObjectName("label")  # it's name
        self.google = QtWidgets.QPushButton(self.centralwidget)  # button
        self.google.setGeometry(QtCore.QRect(20, 370, 75, 23))  # size of button
        self.google.setObjectName("google")
        self.lens = QtWidgets.QPushButton(self.centralwidget)
        self.lens.setGeometry(QtCore.QRect(400, 370, 75, 23))
        self.lens.setObjectName("lens")
        MainWindow2.setCentralWidget(self.centralwidget)  # runs the code

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

        self.google.clicked.connect(self.google1)
        self.lens.clicked.connect(self.lens1)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow", "MainWindow"))  # title of the window
        self.google.setText(_translate("MainWindow", "image 1"))  # text for for buttons
        self.lens.setText(_translate("MainWindow", "image2"))

    def google1(self):
        self.label.setPixmap(QtGui.QPixmap("first.png"))  # setting the pix map

    def lens1(self):
        self.label.setPixmap(QtGui.QPixmap("second.png"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)  # making hte app
    MainWindow = QtWidgets.QMainWindow()  # making main window
    ui = Ui_MainWindow1()  # instance of class
    ui.setupUi(MainWindow)  # method for making
    MainWindow.show()  # showing
    sys.exit(app.exec_())  # clean exit


# Topic: Qmessagebox
class Ui_MainWindow(object):
    def setupUi(self, MainWindow5):
        MainWindow5.setObjectName("MainWindow")  # setting up the main window
        MainWindow5.resize(579, 558)
        self.centralwidget = QtWidgets.QWidget(MainWindow5)  # setting up the main window
        self.centralwidget.setObjectName("centralwidget")
        self.button = QtWidgets.QPushButton(self.centralwidget)  # the place of button
        self.button.setGeometry(QtCore.QRect(4, 12, 531, 351))  # size of button
        self.button.setObjectName("button")  # name of button
        MainWindow5.setCentralWidget(self.centralwidget)  # packed it

        self.retranslateUi(MainWindow5)  # for a function
        QtCore.QMetaObject.connectSlotsByName(MainWindow5)  # attaching

        self.button.clicked.connect(self.showit)  # for our purpose

    def retranslateUi(self, MainWindow5):  # translate
        _translate = QtCore.QCoreApplication.translate
        MainWindow5.setWindowTitle(_translate("MainWindow", "MainWindow"))  # title for window
        self.button.setText(_translate("MainWindow", "PushButton"))  # text for button

    def showit(self):
        msg = QMessageBox()  # instance of messagebox
        msg.setWindowTitle("a message")  # title of message box
        msg.setText("the text")  # text to show
        msg.setIcon(QMessageBox.Question)  # icon inside messagebox
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Retry | QMessageBox.Ignore)  # buttons in messagebox
        msg.setDefaultButton(QMessageBox.Ignore)  # the deafault button(blue color)
        msg.setInformativeText("yeah")  # other line of text
        msg.setDetailedText("details")  # for more details
        msg.buttonClicked.connect(self.pops)  # for printing purpose
        x = msg.exec_()  # clean exit

    @staticmethod
    def pops(i):  # a function which tells which is clicked
        print(i.text())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)  # making hte app
    MainWindow = QtWidgets.QMainWindow()  # making main window
    ui = Ui_MainWindow()  # instance of class
    ui.setupUi(MainWindow)  # method for making
    MainWindow.show()  # showing
    sys.exit(app.exec_())  # clean exit


# Topic: Combo Boxs
class Ui_MainWindow(object):
    def setupUi(self, MainWindow1):

        MainWindow1.setObjectName("MainWindow")  # creating window
        MainWindow1.resize(711, 531)

        font = QtGui.QFont()  # font for window
        font.setPointSize(8)
        MainWindow1.setFont(font)  # packed it
        self.centralwidget = QtWidgets.QWidget(MainWindow1)  # created a widget
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)  # created a combobox
        self.comboBox1.setGeometry(QtCore.QRect(60, 70, 121, 111))

        font = QtGui.QFont()  # font for combobox
        font.setPointSize(48)

        self.comboBox1.setFont(font)
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")  # adding items
        self.comboBox1.addItem("")
        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)  # created a combobox
        self.comboBox2.setGeometry(QtCore.QRect(500, 70, 121, 111))

        font = QtGui.QFont()  # font for combobox
        font.setPointSize(48)

        self.comboBox2.setFont(font)
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")  # adding items
        self.comboBox2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)  # a pushbutton
        self.pushButton.setGeometry(QtCore.QRect(200, 260, 301, 141))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)  # a label
        self.label.setGeometry(QtCore.QRect(240, 140, 201, 71))

        font = QtGui.QFont()  # font for label
        font.setPointSize(36)

        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow1.setCentralWidget(self.centralwidget)  # packed everything

        # self.comboBox1.addItem("madhav")# for adding item
        # index = self.comboBox1.findText("madhav",QtCore.Qt.MatchFixedString)
        # self.comboBox1.setCurrentIndex(index)# for deaf

        self.retranslateUi(MainWindow1)  # for changing purpose
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

        self.pushButton.clicked.connect(self.press)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox1.setItemText(0, _translate("MainWindow", "0"))  # adding item
        self.comboBox1.setItemText(1, _translate("MainWindow", "1"))

        self.comboBox2.setItemText(0, _translate("MainWindow", "0"))  # adding item
        self.comboBox2.setItemText(1, _translate("MainWindow", "1"))

        self.pushButton.setText(_translate("MainWindow", "submit"))  # for button
        self.label.setText(_translate("MainWindow", "xor="))  # forlabel

    def press(self):  # for result
        x = int((self.comboBox1.currentText()))  # for current text
        y = int((self.comboBox2.currentText()))  # for current text
        xor = (x and not y) or (not x and y)  # formula
        if xor == True:  # for only 0 and 1
            xor = 1
        else:
            xor = 0
        self.label.setText("x xor y=" + str(xor))  # changing label
        self.label.adjustSize()  # for convince


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)  # making hte app
    MainWindow = QtWidgets.QMainWindow()  # making main window
    ui = Ui_MainWindow()  # instance of class
    ui.setupUi(MainWindow)  # method for making
    MainWindow.show()  # showing
    sys.exit(app.exec_())  # clean exit

# Topic: Containers
"""
containers: frames, groupbox
groupbox is a container where all the widgets share the all properties.
"""

# Note: It's better to use Object Orientation for GUIs

# Documentation: https://doc.qt.io/qtforpython/
