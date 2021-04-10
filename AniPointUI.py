from config import ballot
from EntryUI import Ui_Entry
from SearchUI import Ui_Search
from SettingsUI import Ui_Settings
from PyQt5 import QtCore, QtGui, QtWidgets
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon(":/AniPointLogoSmall.png"))
        MainWindow.setStyleSheet("background-color: #272c38;")
        
        # Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Central Widget Layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Toolbar
        self.toolbar = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolbar.sizePolicy().hasHeightForWidth())
        self.toolbar.setSizePolicy(sizePolicy)
        self.toolbar.setAutoFillBackground(False)
        self.toolbar.setStyleSheet("background: #1f232d; border-radius: 10px")
        self.toolbar.setObjectName("toolbar")
        
        # Toolbar Layout
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.toolbar)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        # Anipoint Logo
        self.logo = QtWidgets.QLabel(self.toolbar)
        self.logo.setMinimumSize(QtCore.QSize(30, 30))
        self.logo.setBaseSize(QtCore.QSize(50, 50))
        self.logo.setStyleSheet("image: url(:/AniPointLogoTransparent.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.horizontalLayout_3.addWidget(self.logo)
        
        # Meeting Title
        self.lineEdit = QtWidgets.QLineEdit(self.toolbar)
        self.lineEdit.setStyleSheet("color: rgb(159,173,189); font: Arial; background: #272c38; border: 1px solid; border-color: #2f3641; border-radius: 5px;  padding: 5px; margin-right: 5px;")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.editingFinished.connect(self.setTitle)
        self.horizontalLayout_3.addWidget(self.lineEdit)
        
        # Meeting Date
        self.dateEdit = QtWidgets.QDateEdit(self.toolbar)
        self.dateEdit.setStyleSheet("color: rgb(159,173,189); font: Arial; background: #272c38; border: 1px solid; border-color: #2f3641; border-radius: 5px;  padding: 5px; margin-right: 5px;")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.dateChanged.connect(self.setDate)
        self.horizontalLayout_3.addWidget(self.dateEdit)
        
        # Meeting Number
        self.spinBox = QtWidgets.QSpinBox(self.toolbar)
        self.spinBox.setStyleSheet("color: rgb(159,173,189); font: Arial; background: #272c38; border: 1px solid; border-color: #2f3641; border-radius: 5px;  padding: 5px; margin-right: 5px;")
        self.spinBox.setObjectName("spinBox")
        self.spinBox.valueChanged.connect(self.setNum)
        self.horizontalLayout_3.addWidget(self.spinBox)
        
        # Spacer
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)

        # Add Show Button
        self.showBtn = QtWidgets.QPushButton(self.toolbar)
        self.showBtn.clicked.connect(self.addShow)
        self.showBtn.setStyleSheet("color: rgb(159,173,189); font: Arial; background: #272c38; border: 1px solid; border-color: #2f3641; border-radius: 5px;  padding: 5px; margin-right: 5px;")
        self.showBtn.setObjectName("showBtn")
        self.horizontalLayout_3.addWidget(self.showBtn)
        
        # Settings Button
        self.settingsBtn = QtWidgets.QPushButton(self.toolbar)
        self.settingsBtn.setStyleSheet("color: rgb(159,173,189); font: Arial; background: #272c38; border: 1px solid; border-color: #2f3641; border-radius: 5px;  padding: 5px; margin-right: 5px;")
        self.settingsBtn.setObjectName("settingsBtn")
        self.settingsBtn.clicked.connect(self.settings)
        self.horizontalLayout_3.addWidget(self.settingsBtn)

        # Export Button
        self.exportBtn = QtWidgets.QPushButton(self.toolbar)
        self.exportBtn.setStyleSheet("color: rgb(159,173,189); font: Arial; background: #272c38; border: 1px solid; border-color: #2f3641; border-radius: 5px;  padding: 5px; margin-right: 5px;")
        self.exportBtn.setObjectName("exportBtn")
        self.exportBtn.clicked.connect(self.export)
        self.horizontalLayout_3.addWidget(self.exportBtn)
        self.verticalLayout.addWidget(self.toolbar)

        # List of Shows
        self.listWidget = QtWidgets.QWidget()
        self.listBuilder = QtWidgets.QVBoxLayout(self.listWidget)
        self.listLayout = QtWidgets.QVBoxLayout()
        self.listBuilder.addLayout(self.listLayout)
        self.listBuilder.addStretch(1)
        self.listLayout.setContentsMargins(0,0,0,0)
        self.listBuilder.setContentsMargins(0,0,0,0)
        self.listWidget.setObjectName("listWidget")
        
        # Scroll Area for List
        self.scrollbox = QtWidgets.QScrollArea()
        self.scrollbox.setWidgetResizable(True)
        self.scrollbox.setWidget(self.listWidget)
        self.scrollbox.setStyleSheet("background: #1f232d; border-radius: 10px; padding: 5px; margin: 5px;")

        # Scrollbar Style
        self.scrollbar = QtWidgets.QScrollBar()
        self.scrollbar.setStyleSheet("QScrollBar {background: #2f3641; border-radius: 5px; padding: 0px;} QScrollBar::handle {background-color: #555555; border: none;} QScrollBar::add-line, QScrollBar::sub-line {height: 0px}")
        self.scrollbox.setVerticalScrollBar(self.scrollbar)
        self.verticalLayout.addWidget(self.scrollbox, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AniPoint"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Meeting Title"))
        self.dateEdit.setToolTip(_translate("MainWindow", "Meeting Date"))
        self.spinBox.setToolTip(_translate("MainWindow", "Meeting Number"))
        self.showBtn.setText(_translate("MainWindow", "Add Show"))
        self.settingsBtn.setText(_translate("MainWindow", "Settings"))
        self.exportBtn.setText(_translate("MainWindow", "Export"))

    def setTitle(self):
        if (self.lineEdit.text()):
            ballot.setTitle(self.lineEdit.text())
        else:
            ballot.setTitle("Meeting Title")

    def setDate(self):
        ballot.setDate(self.dateEdit.date().toString("MMMM d yyyy"))
    
    def setNum(self):
        ballot.setNumber(self.spinBox.value())

    def addShow(self):
        searchWin = Ui_Search()
        result = searchWin.exec_()
        if result:
            entry = QtWidgets.QWidget(self.listWidget)
            entry.setStyleSheet("background: #2f3641; padding: 0px; margin: 0px")
            entryLayout = QtWidgets.QHBoxLayout(entry)
            entryLayout.setContentsMargins(0,0,0,0)
            entryLayout.addWidget(Ui_Entry(QtWidgets.QWidget(entry), result))
            self.listLayout.addWidget(entry)

    def settings(self):
        settingsWin = Ui_Settings()
        settingsWin.exec_()

    def export(self):
        path = QtWidgets.QFileDialog.getSaveFileName(caption = "Export Powerpoint", directory = f".\\{ballot.getNumber()} - {ballot.getTitle()}.pptx", filter = "Powerpoint Presentation (*.pptx)")[0]
        if (path):
            ballot.export(outputPath=path)

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.showMaximized()
        sys.exit(app.exec_())