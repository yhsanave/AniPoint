from config import ballot
from PyQt5 import QtCore, QtGui, QtWidgets
import requests, webbrowser

class Ui_Settings(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Ui_Settings, self).__init__(parent)
        font = QtGui.QFont()
        font.setPointSize(12)

        # Window
        self.setWindowTitle("Settings")
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setStyleSheet("background-color: #272c38;")
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        # Access Token Widget
        self.accessWidget = QtWidgets.QWidget(self)
        self.accessLayout = QtWidgets.QHBoxLayout(self.accessWidget)
        self.accessLayout.setContentsMargins(0, 0, 0, 0)
        
        # Access Token Entry
        self.accessEntry = QtWidgets.QLineEdit(self.accessWidget)
        self.accessEntry.setFont(font)
        self.accessEntry.setStyleSheet("color: rgb(159,173,189); font: Arial; background: #272c38; border: 1px solid; border-color: #2f3641; border-radius: 5px; padding: 5px; margin-right: 5px;")
        self.accessEntry.setPlaceholderText("Access Token")
        self.accessEntry.setText(ballot.accessToken)
        self.accessEntry.editingFinished.connect(self.setAccessToken)
        self.accessLayout.addWidget(self.accessEntry, 1)

        # Access Token Button
        self.accessBtn = QtWidgets.QPushButton(self.accessWidget)
        self.accessBtn.setFont(font)
        self.accessBtn.setStyleSheet("color: rgb(159,173,189); font: Arial; background: #272c38; border: 1px solid; border-color: #2f3641; border-radius: 5px; padding: 5px;")
        self.accessBtn.setText("Get Access Token")
        self.accessBtn.setAutoDefault(False)
        self.accessBtn.clicked.connect(self.getToken)
        self.accessLayout.addWidget(self.accessBtn)

        self.layout.addWidget(self.accessWidget)

        # Account Info
        self.accountInfo = QtWidgets.QLabel(self)
        self.accountInfo.setFont(font)
        self.accountInfo.setAlignment(QtCore.Qt.AlignHCenter)
        self.accountInfo.setStyleSheet("color: rgb(159,173,189); font: Arial;")
        self.setAccessToken()
        self.layout.addWidget(self.accountInfo)

        # Custom List Entry
        self.customListEntry = QtWidgets.QLineEdit(self)
        self.customListEntry.setFont(font)
        self.customListEntry.setStyleSheet("color: rgb(159,173,189); font: Arial; background: #272c38; border: 1px solid; border-color: #2f3641; border-radius: 5px; padding: 5px; margin-right: 5px;")
        self.customListEntry.setPlaceholderText("Custom List Name")
        self.customListEntry.setText(ballot.customList)
        self.customListEntry.editingFinished.connect(self.setCustomList)
        self.layout.addWidget(self.customListEntry)

    def setAccessToken(self):
        user = ballot.setAccessToken(self.accessEntry.text())
        self.accountInfo.setText(user)

    def getToken(self):
        webbrowser.open_new_tab("https://anilist.co/api/v2/oauth/authorize?client_id=3352&response_type=token")

    def setCustomList(self):
        ballot.setCustomList(self.customListEntry.text())