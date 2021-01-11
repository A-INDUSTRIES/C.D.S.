from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2 import QtWidgets, QtCore, QtGui

import sys, pypresence as rpc

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layout()
        self.setup_connetions()
        self.rpc_start()

    def create_widgets(self):
        self.btn_set = QtWidgets.QPushButton("Set as Status")
        self.btn_clear = QtWidgets.QPushButton("Clear current Status")
        self.cb_icon_choice = QtWidgets.QComboBox()
        self.le_details = QtWidgets.QLineEdit("Top Line")
        self.le_status = QtWidgets.QLineEdit("Bottom Line")
        self.img = QtWidgets.QLabel()

    def modify_widgets(self):
        self.cb_icon_choice.addItems(["VisualStudioCode", "Youtube", "Technical Stuff"])
        self.img.setPixmap(QtGui.QPixmap(appctxt.get_resource("RPC.png")))

    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

    def add_widgets_to_layout(self):
        self.main_layout.addWidget(self.img, 1,1,10,10)
        self.main_layout.addWidget(self.cb_icon_choice, 4,3,1,1)
        self.main_layout.addWidget(self.btn_set, 10,1,1,1)
        self.main_layout.addWidget(self.btn_clear, 10,2,1,1)

    def setup_connetions(self):
        self.btn_set.clicked.connect(self.rpc_set)
        self.btn_clear.clicked.connect(self.rpc_clear)

    def rpc_clear(self):
        self.presence.clear()

    def rpc_start(self):
        self.presence = rpc.Presence("797892938201432125")
        self.presence.connect()
        self.presence.update(details="Setting up custom status...", state="Coded by AINDUSTRIES")

    def rpc_set(self):
        if self.cb_icon_choice.currentText() == "VisualStudioCode":
            self.presence.update(details="Coding Stuff in", state="Visual Studio Code")

    def closeEvent(self, event=QtGui.QCloseEvent):
        self.presence.clear()
        self.presence.close()

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.resize(250, 150)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)