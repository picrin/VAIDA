from PyQt4.QtGui import QDialog, QFileDialog, QMessageBox
from GUI.Layouts.PrivateKeySelectorDialog import Ui_PrivateKeySelectorDialog
from GPG.gpglib import private_keys_users, true_gpg_path, test_passphrase
from GUI.MakeVideoForm import MakeVideoForm
from os.path import expanduser

def showPrivateKeySelector(app):
    PrivateKeySelector(app)

class PrivateKeySelector (QDialog):
    
    def startMakeVideo(self, passphrase, keyID):
        form = MakeVideoForm(self.app, passphrase, keyID)
        self.close()
        form.exec()
    
    def __init__(self, app):
        #Set up window
        super(QDialog, self).__init__()
        self.ui = Ui_PrivateKeySelectorDialog()
        self.ui.setupUi(self)
        self.app = app
        
        self.keysDict = private_keys_users()
        if not self.keysDict:
            # Didn't find any keys so ask for their location
            homeDir = expanduser("~")
            keysLocation = str(QFileDialog.getOpenFileName(caption="Choose your private keys location", directory=homeDir))
            true_gpg_path = keysLocation
            self.keysDict = private_keys_users()
        
        for key in self.keysDict.keys():
            self.ui.keyListWidget.addItem(key)
        
        self.ui.selectKeyButton.clicked.connect(self.selectKey)
        
        self.show()
        
    def selectKey(self):
        # TODO rename "lineEdit" to something descriptive
        passphrase = self.ui.lineEdit.text()
        
        # Get keyID from list
        selected = self.ui.keyListWidget.selectedItems()[0].text()
        print (selected)
        keyID = self.keysDict[selected]
        
        # Test passphrase and handle failure
        if not test_passphrase(keyID, passphrase):
            message = QMessageBox()
            message.setText("Incorrect passphrase")
            message.exec()
            return
        
        self.startMakeVideo(passphrase, keyID)
