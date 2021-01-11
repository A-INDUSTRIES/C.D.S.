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

    def create_widgets(self):
        self.btn_set = QtWidgets.QPushButton("Set as Status")
        self.btn_clear = QtWidgets.QPushButton("Clear current Status")
        self.cb_choice = QtWidgets.QComboBox()

    def modify_widgets(self):
        self.cb_choice.addItems(["VisualStudioCode", "Youtube", "Technical Stuff"])

    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout(self)

    def add_widgets_to_layout(self):
        self.main_layout.addWidget(self.cb_choice, 1,1,1,1)
        self.main_layout.addWidget(self.btn_set, 1,2,1,1)
        self.main_layout.addWidget(self.btn_clear, 2,1,1,2)

    def setup_connetions(self):
        pass

    def rpc_start(self):
        self.presence = rpc.Presence("797892938201432125")
        self.presence.connect()
        self.presence.update(details="Setting up custom status...")

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.resize(250, 150)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)