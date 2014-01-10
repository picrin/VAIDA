import sys
from PyQt4.QtGui import QApplication, QDialog, QMessageBox, QFileDialog
from GUI.Layouts.HomeLayout import Ui_HomeDialog
from GUI.GenerateForm1 import GenerateForm1
from os.path import expanduser
from GUI.VideoVerificationForm import VideoVerificationForm

class VAIDAApp (QApplication) :
    
    def onCreateButtonClicked(self):
        # Create
        form = GenerateForm1(self)
        self.window.close()
        form.exec()

    def onVerifyButtonClicked(self):
        # Verify
        homeDir = expanduser("~")
        fname = str(QFileDialog.getOpenFileName(caption="Choose a VAIDA file", directory=homeDir))
        if len(fname) == 0:
            # No file selected (dialog cancelled)
            return
        form = VideoVerificationForm(self, vaidaPath=fname)
        self.window.close()
        form.exec()

    def closeApp(self):
        # Kill the app
        self.exit(0)
        
    def __init__(self, argv):
        super(VAIDAApp, self).__init__(argv)
        self.window = QDialog()
        self.ui = Ui_HomeDialog()
        self.ui.setupUi(self.window)
        
        # Add button connections and last window closed kills app
        self.ui.createButton.clicked.connect(self.onCreateButtonClicked)
        self.ui.verifyButton.clicked.connect(self.onVerifyButtonClicked)
        self.lastWindowClosed.connect(self.closeApp)
        
        self.window.show()
        
        # Start QApplication loop
        sys.exit(self.exec_())

VAIDAApp(sys.argv)
