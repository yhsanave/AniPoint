from config import ballot
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from show import Show

class Ui_Search(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Ui_Search, self).__init__(parent)
        font = QtGui.QFont()
        font.setPointSize(12)

        # Window
        self.setWindowTitle("Search")
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setStyleSheet("background-color: #272c38;")
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        
        # Search bar
        self.searchBar = QtWidgets.QWidget()
        self.searchBar.setStyleSheet("background: #1f232d; border-radius: 10px")
        self.barLayout = QtWidgets.QHBoxLayout()
        self.searchBar.setLayout(self.barLayout)

        # Search By Name
        self.nameSearch = QtWidgets.QLineEdit()
        self.nameSearch.setFont(font)
        self.nameSearch.setStyleSheet("color: rgb(159,173,189); font: Arial 12pt; background: #272c38; border: 1px solid; border-color: #2f3641; border-radius: 5px;  padding: 5px;")
        self.nameSearch.setPlaceholderText("Search by Title")
        self.nameSearch.returnPressed.connect(self.searchName)
        self.barLayout.addWidget(self.nameSearch, 1)

        # Search by ID
        self.idSearch = QtWidgets.QLineEdit()
        self.idSearch.setFont(font)
        self.idSearch.setStyleSheet("color: rgb(159,173,189); font: Arial;  background: #272c38; border: 1px solid; border-color: #2f3641; border-radius: 5px;  padding: 5px;")
        self.idSearch.setPlaceholderText("Search by ID")
        self.idSearch.returnPressed.connect(self.searchId)
        self.barLayout.addWidget(self.idSearch, 0)
        
        self.layout.addWidget(self.searchBar)
        
        # Results
        self.results = QtWidgets.QWidget(self)
        self.resultLayout = QtWidgets.QVBoxLayout()
        self.results.setLayout(self.resultLayout)
        self.results.setStyleSheet("background: #1f232d; border-radius: 10px")
        self.results.setMinimumWidth(750)
        self.results.setMinimumHeight(400)

        self.layout.addWidget(self.results, 1)

    def searchName(self):
        for i in self.results.children():
            if (isinstance(i, Ui_Result)):
                i.deleteLater()

        if (self.nameSearch.text()):
            results = ballot.search(self.nameSearch.text())
            for i in results:
                widget = Ui_Result(i, self.results)
                self.resultLayout.addWidget(widget)

    def searchId(self):
        for i in self.results.children():
            if (isinstance(i, Ui_Result)):
                i.deleteLater()
            
        if (self.idSearch.text()):
            result = Show(self.idSearch.text())
            data = {'id': result.id, 'title': {'english': result.data["title"]["english"], 'romaji': result.data["title"]["romaji"]}, 'seasonYear': result.data["seasonYear"], 'coverImage': {'large': result.getCoverUrl()}}
            widget = Ui_Result(data, self.results)
            self.resultLayout.addWidget(widget)

class Ui_Result(QtWidgets.QWidget):
    def __init__(self, data: dict, parent=None):
        super(Ui_Result, self).__init__(parent)
        self.id = int(data["id"])
        self.parent = parent

        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFixedHeight(70)
        self.setContentsMargins(0,0,0,0)
        self.clayout = QtWidgets.QHBoxLayout(self)
        self.clayout.setContentsMargins(0,0,0,0)
        self.container = QtWidgets.QWidget(self)
        self.container.setContentsMargins(0,0,0,0)
        self.layout = QtWidgets.QHBoxLayout(self.container)
        self.layout.setContentsMargins(10,5,10,5)
        self.container.setLayout = self.layout
        self.container.setStyleSheet("background: #2f3641; padding: 0px; margin: 0px")

        # Cover
        self.cover = QtWidgets.QLabel(self.container)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(requests.get(data["coverImage"]["large"]).content)
        self.cover.setPixmap(pixmap.scaledToHeight(50))
        self.cover.setFixedHeight(60)
        self.cover.setStyleSheet("border-radius: 5px; height: 50px; padding: 0px")
        self.layout.addWidget(self.cover)

        # Title
        self.title = QtWidgets.QLabel(self.container)
        if (data["title"]["english"]):
            self.title.setText(data["title"]["english"])
        else:
            self.title.setText(data["title"]["romaji"])
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(159,173,189); font: Arial")
        self.layout.addWidget(self.title, 1)

        # Year
        if (data["seasonYear"]):
            self.year = QtWidgets.QLabel(self.container)
            self.year.setFont(font)
            self.year.setText(f'{data["seasonYear"]}')
            self.year.setStyleSheet("color: rgb(159,173,189); font: Arial")
            self.layout.addWidget(self.year)

        # Add Button
        self.addBtn = QtWidgets.QPushButton(self.container)
        self.addBtn.setFont(font)
        self.addBtn.setStyleSheet("color: rgb(159,173,189); font: Arial; background: #272c38; border: 1px solid; border-color: #2f3641; border-radius: 5px; padding: 5px;")
        self.addBtn.setText("Add")
        self.addBtn.clicked.connect(self.addShow)
        self.layout.addWidget(self.addBtn)

        self.clayout.addWidget(self.container)

    def addShow(self):
        self.parent.parentWidget().done(self.id)