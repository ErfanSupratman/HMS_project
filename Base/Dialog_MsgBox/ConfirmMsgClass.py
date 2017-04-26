import sys
from PySide.QtGui import *


class ConfirmYesNo(QDialog):
    def __init__(self, parent=None):
        super(ConfirmYesNo, self).__init__(parent)
        msgBox = QMessageBox()
        msgBox.setText("The document has been modified.")
        msgBox.setInformativeText("Do you want to discard your changes?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        layout = QGridLayout()
        layout.addWidget(msgBox)
        self.setLayout(layout)
        self.setModal(True)
        self.show()
        choose = msgBox.exec()
        if choose == QMessageBox.Yes:
            self.ans = True
        else:
            self.ans = False


def main():
    app = QApplication(sys.argv)
    win = ConfirmYesNo()
    exit(app.exec_())

if __name__ == "__main__":
    main()