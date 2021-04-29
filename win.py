import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from des import DesKey
from key import myDESkey, myAESkey
from core.read import read_file, read_img
from core.download import download_file
from core.upload import upload_file

key = DesKey(myDESkey)


def encrypt_DES(text, filename):
    spaces = 0
    spaces = len(text) % 8
    print(spaces)
    if spaces != 0:
        spaces = 8-spaces
        text += " "*(spaces-1)
        text += str(spaces)
    print(text)
    text = str.encode(text)
    print(text)
    text = key.encrypt(text)
    print(text)
    enc_file = open("encryptedFiles/"+filename, "wb")
    enc_file.write(text)
    enc_file.close()
    return True


def decrypt_DES(text, filename):
    text = key.decrypt(text)
    print(text)
    text = text.decode()
    print(text)
    spaces = text[-1]
    text = text[:-int(spaces)]
    print(text)
    dec_file = open("decryptedFiles/"+filename, "w")
    dec_file.write(text)
    dec_file.close()
    dec_file = open("downloads/"+filename, "w")
    dec_file.write(text)
    dec_file.close()
    return True


class MyWindow(QWidget):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowTitle("Secure File Storage")

        self.title = QLabel(self)
        self.title.setText("Secure File Storage in Cloud")
        # self.title.setText("")
        self.title.move(30, 30)

        self.uploadLabel = QLabel(self)
        self.uploadLabel.setText("Enter the file name to upload:")
        self.uploadLabel.move(30, 90)

        self.font1 = QFont()
        self.font1.setFamily("Arial")
        self.font1.setPointSize(25)

        self.font2 = QFont()
        self.font2.setFamily("Arial")
        self.font2.setPointSize(15)

        self.title.setFont(self.font1)
        self.uploadLabel.setFont(self.font2)

        self.uploadTextfield = QLineEdit(self)
        self.uploadTextfield.move(30, 120)

        self.uploadBtn = QPushButton(self)
        self.uploadBtn.setText("Upload")
        self.uploadBtn.clicked.connect(self.clickUpload)
        self.uploadBtn.move(30, 150)

        self.printMsg1 = QLabel(self)
        self.printMsg1.setText("")
        self.printMsg1.move(30, 180)

        self.downloadLabel = QLabel(self)
        self.downloadLabel.setText("Enter the file name to download:")
        self.downloadLabel.move(350, 90)
        self.downloadLabel.setFont(self.font2)

        self.downloadTextfield = QLineEdit(self)
        self.downloadTextfield.move(350, 120)

        self.downloadBtn = QPushButton(self)
        self.downloadBtn.setText("Download")
        self.downloadBtn.clicked.connect(self.clickDownload)
        self.downloadBtn.move(350, 150)

        self.printMsg2 = QLabel(self)
        self.printMsg2.setText("")
        self.printMsg2.move(350, 180)

    def clickUpload(self):
        filename = self.uploadTextfield.text()
        print(filename)
        filedata = read_file(filename, "r")
        if encrypt_DES(filedata, filename):
            print("Encrypted")
            if upload_file(filename):
                print("File uploaded")
                self.printMsg1.setText("File Uploaded Successfully")
                self.printMsg1.adjustSize()

    def clickDownload(self):
        filename = self.downloadTextfield.text()
        if download_file(filename):
            print("File downloaded")
            filedata = read_file("downloads/"+filename, "rb")
            if decrypt_DES(filedata, filename):
                print("Decrypted")
                self.printMsg2.setText("Successfully File Downloaded")
                self.printMsg2.adjustSize()


def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
