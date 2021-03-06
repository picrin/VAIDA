import sys
from PyQt4.QtGui import QApplication, QDialog, QMessageBox
from PyQt4.phonon import Phonon
from GUI.Layouts.VideoVerificationFormLayout import Ui_VideoVerificationDialog
from GUI.KeySavedForm import KeySavedForm
from GPG.gpglib import untar_verify_vaida, add_tmp_to_keyring
from PyQt4.QtGui import QMessageBox
import os.path
from GPG import uIntToString

class VideoVerificationForm (QDialog) :

    def showMessage(self, text):
        message = QMessageBox()
        message.setText(text)
        message.exec()

    def checkBoxChecked(self, x):
        if (self.ui.checkBox.isChecked() and self.ui.checkBox_2.isChecked() and self.ui.checkBox_3.isChecked() and self.ui.checkBox_4.isChecked()):
            try:
                add_tmp_to_keyring()
            except GPGException as e:
                self.showMessage(str(e))
            else:
                newForm = KeySavedForm(self.app)
                self.close()
                newForm.exec()
   
    def __init__(self, app, vaidaPath):
        super(QDialog, self).__init__()
        
        success, fingerprint, absoluteVideoPath, dateUInt, uid = untar_verify_vaida(vaidaPath)
        
        expirationDate = uIntToString.uIntToString(dateUInt)
        
        if not success:
            self.showMessage("VAIDA verification failed!")
            return
        
        self.ui = Ui_VideoVerificationDialog()
        self.ui.setupUi(self)
        self.app = app
        
        # Set text
        self.ui.fingerprintLabel.setText("Key fingerprint: " + fingerprint)
        self.ui.keyExpirationLabel.setText("Key expiration date: " + expirationDate)
        
        # First name
        name = uid.split("<")[0].strip()
        self.ui.checkBox.setText("Does this look like " + name + "?")
        self.ui.checkBox_2.setText("Does this sound like " + name + "?")

        # Set media
        self.source = Phonon.MediaSource(absoluteVideoPath)
        self.media = Phonon.MediaObject()
        self.media.setCurrentSource(self.source)
        self.video = Phonon.VideoWidget(self.ui.videoPlayerWidget)
        self.video.setMinimumSize(600, 600)
        
        # Scale mode - 0 = do not scale, 1 = scale and crop
        self.video.setScaleMode(Phonon.VideoWidget.ScaleMode(0))
        
        self.audio = Phonon.AudioOutput(Phonon.VideoCategory, self.ui.videoPlayerWidget)
        Phonon.createPath(self.media, self.audio)
        Phonon.createPath(self.media, self.video)

        self.ui.checkBox.stateChanged.connect(self.checkBoxChecked)
        self.ui.checkBox_2.stateChanged.connect(self.checkBoxChecked)
        self.ui.checkBox_3.stateChanged.connect(self.checkBoxChecked)
        self.ui.checkBox_4.stateChanged.connect(self.checkBoxChecked)
        
        self.show()
        self.media.play()
