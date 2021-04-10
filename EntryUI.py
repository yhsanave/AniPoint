import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from show import Show
from config import ballot


class Ui_Entry(QtWidgets.QWidget):
    def __init__(self, Entry, id: int, parent=None):
        super(Ui_Entry, self).__init__(parent)
        self.setObjectName("Entry")
        self.setFixedHeight(70)
        self.setStyleSheet("padding: 0px")
        self.info = Show(id)
        ballot.addShow(self.info)
        
        # Layout
        self.entryLayout = QtWidgets.QHBoxLayout(self)
        self.entryLayout.setObjectName("entryLayout")
        self.entryLayout.setSpacing(5)
        self.entryLayout.setContentsMargins(10,5,10,5)

        # Cover
        self.cover = QtWidgets.QLabel(Entry)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(requests.get(self.info.getCoverUrl()).content)
        self.cover.setPixmap(pixmap.scaledToHeight(50))
        self.cover.setFixedHeight(60)
        self.cover.setStyleSheet("border-radius: 5px; height: 50px; padding: 0px")
        self.cover.setObjectName("cover")
        self.entryLayout.addWidget(self.cover)
        
        # Title
        self.title = QtWidgets.QLabel(Entry)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(159,173,189); font: Arial")
        self.title.setText(self.info.getTitleENG())
        self.title.setObjectName("title")
        self.entryLayout.addWidget(self.title)
        
        # Warnings
        self.warning = QtWidgets.QLabel(Entry)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.warning.setFont(font)
        self.warning.setScaledContents(False)
        self.warning.setAlignment(QtCore.Qt.AlignCenter)
        self.warning.setStyleSheet("QToolTip {color: rgb(159,173,189); border: 1px solid #3f4651}")
        self.warning.setObjectName("warning")
        self.entryLayout.addWidget(self.warning)
        
        # Episode
        self.episode = QtWidgets.QLineEdit(Entry)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.episode.setFont(font)
        self.episode.setStyleSheet("color: rgb(159,173,189); font: Arial; background: #272c38; border: 1px solid; border-color: #2f3641; border-radius: 5px; padding: 5px; margin-right: 5px;")
        self.episode.setObjectName("episode")
        self.episode.editingFinished.connect(self.setEpisode)
        self.entryLayout.addWidget(self.episode)
        
        # Subbed/Dubbed
        self.subCheck = QtWidgets.QCheckBox("Sub")
        self.subCheck.setChecked(True)
        self.dubCheck = QtWidgets.QCheckBox("Dub")
        self.subCheck.setStyleSheet("color: rgb(159,173,189); font: Arial; font-size: 12pt; background: #272c38; border: 1px solid; border-color: #2f3641; border-radius: 5px; padding: 5px;")
        self.dubCheck.setStyleSheet("color: rgb(159,173,189); font: Arial; font-size: 12pt; background: #272c38; border: 1px solid; border-color: #2f3641; border-radius: 5px; padding: 5px;")
        self.subCheck.stateChanged.connect(self.toggleSub)
        self.dubCheck.stateChanged.connect(self.toggleDub)
        self.entryLayout.addWidget(self.subCheck)
        self.entryLayout.addWidget(self.dubCheck)
        
        # Gif Button
        self.gifBtn = QtWidgets.QPushButton(Entry)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.gifBtn.setFont(font)
        self.gifBtn.setStyleSheet("color: rgb(159,173,189); font: Arial; background: #272c38; border: 1px solid; border-color: #2f3641; border-radius: 5px; padding: 5px;")
        self.gifBtn.setObjectName("gifBtn")
        self.gifBtn.clicked.connect(self.setGif)
        self.entryLayout.addWidget(self.gifBtn)
        
        # Remove Button
        self.removeBtn = QtWidgets.QPushButton(Entry)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.removeBtn.setFont(font)
        self.removeBtn.setStyleSheet("color: rgb(159,173,189); font: Arial; background: #272c38; border: 1px solid; border-color: #2f3641; border-radius: 5px; padding: 5px;")
        self.removeBtn.setObjectName("removeBtn")
        self.removeBtn.clicked.connect(self.remove)
        self.entryLayout.addWidget(self.removeBtn)
        self.entryLayout.setStretch(1, 1)

        self.retranslateUi(Entry)
        QtCore.QMetaObject.connectSlotsByName(Entry)

    def retranslateUi(self, Entry):
        _translate = QtCore.QCoreApplication.translate
        Entry.setWindowTitle(_translate("Entry", "Form"))
        if (self.info.warn()):
                self.warning.setToolTip(_translate("Entry", self.info.warn()))
                self.warning.setText(_translate("Entry", "⚠️"))
        else:
                self.warning.setText("")
        self.episode.setPlaceholderText(_translate("Entry", "Episode"))
        self.gifBtn.setText(_translate("Entry", "Set GIF"))
        self.removeBtn.setText(_translate("Entry", "Remove"))

    def setEpisode(self):
        if (self.episode.text()):
            self.info.setEpisode(self.episode.text())
        else:
            self.info.setEpisode("1")

    def toggleSub(self):
        self.info.toggleSub()

    def toggleDub(self):
        self.info.toggleDub()

    def remove(self):
        ballot.removeShow(self.info)
        self.parentWidget().deleteLater()
        self.deleteLater()

    def setGif(self):
        self.info.setGifPath(QtWidgets.QFileDialog.getOpenFileName()[0])
        if (not self.info.getGifPath()):
                self.info.setGifPath(r".\default.gif")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Entry = Ui_Entry(QtWidgets.QWidget(), 97709)
    Entry.show()
    sys.exit(app.exec_())
