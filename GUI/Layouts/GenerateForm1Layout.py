# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GenerateForm1Layout.ui'
#
# Created: Fri Jan 10 20:18:26 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GenerateForm1Dialog(object):
    def setupUi(self, GenerateForm1Dialog):
        GenerateForm1Dialog.setObjectName(_fromUtf8("GenerateForm1Dialog"))
        GenerateForm1Dialog.resize(646, 536)
        font = QtGui.QFont()
        font.setPointSize(12)
        GenerateForm1Dialog.setFont(font)
        self.existingPGPLabel = QtGui.QLabel(GenerateForm1Dialog)
        self.existingPGPLabel.setGeometry(QtCore.QRect(0, 10, 651, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.existingPGPLabel.setFont(font)
        self.existingPGPLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.existingPGPLabel.setObjectName(_fromUtf8("existingPGPLabel"))
        self.loadKeyButton = QtGui.QPushButton(GenerateForm1Dialog)
        self.loadKeyButton.setGeometry(QtCore.QRect(210, 70, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loadKeyButton.setFont(font)
        self.loadKeyButton.setObjectName(_fromUtf8("loadKeyButton"))
        self.newPGPLabel = QtGui.QLabel(GenerateForm1Dialog)
        self.newPGPLabel.setGeometry(QtCore.QRect(0, 100, 651, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.newPGPLabel.setFont(font)
        self.newPGPLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newPGPLabel.setObjectName(_fromUtf8("newPGPLabel"))
        self.nameLabel = QtGui.QLabel(GenerateForm1Dialog)
        self.nameLabel.setGeometry(QtCore.QRect(10, 160, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.nameTextEdit = QtGui.QPlainTextEdit(GenerateForm1Dialog)
        self.nameTextEdit.setGeometry(QtCore.QRect(190, 150, 451, 31))
        self.nameTextEdit.setTabChangesFocus(True)
        self.nameTextEdit.setObjectName(_fromUtf8("nameTextEdit"))
        self.emailLabel = QtGui.QLabel(GenerateForm1Dialog)
        self.emailLabel.setGeometry(QtCore.QRect(10, 200, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.emailTextEdit = QtGui.QPlainTextEdit(GenerateForm1Dialog)
        self.emailTextEdit.setGeometry(QtCore.QRect(190, 190, 451, 31))
        self.emailTextEdit.setTabChangesFocus(True)
        self.emailTextEdit.setObjectName(_fromUtf8("emailTextEdit"))
        self.passphraseLabel = QtGui.QLabel(GenerateForm1Dialog)
        self.passphraseLabel.setGeometry(QtCore.QRect(10, 390, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passphraseLabel.setFont(font)
        self.passphraseLabel.setObjectName(_fromUtf8("passphraseLabel"))
        self.passphraseTipsTextEdit = QtGui.QLabel(GenerateForm1Dialog)
        self.passphraseTipsTextEdit.setGeometry(QtCore.QRect(20, 290, 621, 81))
        font = QtGui.QFont()
        font.setItalic(True)
        self.passphraseTipsTextEdit.setFont(font)
        self.passphraseTipsTextEdit.setObjectName(_fromUtf8("passphraseTipsTextEdit"))
        self.generateKeyButton = QtGui.QPushButton(GenerateForm1Dialog)
        self.generateKeyButton.setGeometry(QtCore.QRect(210, 490, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.generateKeyButton.setFont(font)
        self.generateKeyButton.setObjectName(_fromUtf8("generateKeyButton"))
        self.passphraseLengthLabel = QtGui.QLabel(GenerateForm1Dialog)
        self.passphraseLengthLabel.setGeometry(QtCore.QRect(590, 390, 51, 20))
        self.passphraseLengthLabel.setObjectName(_fromUtf8("passphraseLengthLabel"))
        self.passphraseLineEdit = QtGui.QLineEdit(GenerateForm1Dialog)
        self.passphraseLineEdit.setGeometry(QtCore.QRect(170, 390, 401, 22))
        self.passphraseLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passphraseLineEdit.setObjectName(_fromUtf8("passphraseLineEdit"))
        self.repeatPassphraseLineEdit = QtGui.QLineEdit(GenerateForm1Dialog)
        self.repeatPassphraseLineEdit.setGeometry(QtCore.QRect(170, 440, 401, 22))
        self.repeatPassphraseLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.repeatPassphraseLineEdit.setObjectName(_fromUtf8("repeatPassphraseLineEdit"))
        self.passphraseLabel_2 = QtGui.QLabel(GenerateForm1Dialog)
        self.passphraseLabel_2.setGeometry(QtCore.QRect(10, 440, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passphraseLabel_2.setFont(font)
        self.passphraseLabel_2.setObjectName(_fromUtf8("passphraseLabel_2"))
        self.nicknameTextEdit = QtGui.QPlainTextEdit(GenerateForm1Dialog)
        self.nicknameTextEdit.setGeometry(QtCore.QRect(190, 230, 451, 31))
        self.nicknameTextEdit.setTabChangesFocus(True)
        self.nicknameTextEdit.setObjectName(_fromUtf8("nicknameTextEdit"))
        self.emailLabel_2 = QtGui.QLabel(GenerateForm1Dialog)
        self.emailLabel_2.setGeometry(QtCore.QRect(10, 240, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.emailLabel_2.setFont(font)
        self.emailLabel_2.setObjectName(_fromUtf8("emailLabel_2"))

        self.retranslateUi(GenerateForm1Dialog)
        QtCore.QMetaObject.connectSlotsByName(GenerateForm1Dialog)

    def retranslateUi(self, GenerateForm1Dialog):
        GenerateForm1Dialog.setWindowTitle(_translate("GenerateForm1Dialog", "VAIDA - Choose Key", None))
        self.existingPGPLabel.setText(_translate("GenerateForm1Dialog", "Already  have a PGP Key?", None))
        self.loadKeyButton.setText(_translate("GenerateForm1Dialog", "Load Key", None))
        self.newPGPLabel.setText(_translate("GenerateForm1Dialog", "Otherwise, generate a new key:", None))
        self.nameLabel.setText(_translate("GenerateForm1Dialog", "Your name:", None))
        self.emailLabel.setText(_translate("GenerateForm1Dialog", "Your email address:", None))
        self.passphraseLabel.setText(_translate("GenerateForm1Dialog", "Passphrase", None))
        self.passphraseTipsTextEdit.setText(_translate("GenerateForm1Dialog", "Your passphrase should be at least 20 characters long and should be as difficult\n"
"to guess as possible.It should contain words not found in the dictionary.\n"
"\n"
"For example: \"Dirty loondry! Boundry. Stash/\"", None))
        self.generateKeyButton.setText(_translate("GenerateForm1Dialog", "Generate Key", None))
        self.passphraseLengthLabel.setText(_translate("GenerateForm1Dialog", "0", None))
        self.passphraseLabel_2.setText(_translate("GenerateForm1Dialog", "Repeat Passphrase", None))
        self.emailLabel_2.setText(_translate("GenerateForm1Dialog", "Nickname (optional):", None))

