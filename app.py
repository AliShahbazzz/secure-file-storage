from des import DesKey
from key import mykey
from core.read import read_file, read_img
from core.download import download_file
from core.upload import upload_file

key = DesKey(mykey)


def encrypt_DES(text, filename):
    spaces = 0
    if len(text) % 8 == 7:
        spaces += 1
    else:
        while len(text) % 8 != 0:
            text += " "
            spaces += 1
        text = text[:-1]
    text += str(spaces)
    text = str.encode(text)
    text = key.encrypt(text)
    enc_file = open("encryptedFiles/"+filename, "wb")
    enc_file.write(text)
    enc_file.close()
    return True


def decrypt_DES(text, filename):
    text = key.decrypt(text)
    text = text.decode()
    spaces = text[-1]
    text = text[:-int(spaces)]
    dec_file = open("decryptedFiles/"+filename, "w")
    dec_file.write(text)
    dec_file.close()
    dec_file = open("downloadedFiles/"+filename, "w")
    dec_file.write(text)
    dec_file.close()
    return True


choice = int(input("Choose: \n 1: Encrpt\n 2: Decrypt\n"))
if(choice == 1):
    filename = input("Enter filename to encrypt: ")
    if filename.lower().endswith('jpg'):
        filedata = read_img(filename, "r", 'Latin-1')
    else:
        filedata = read_file(filename, "r")
    if encrypt_DES(filedata, filename):
        print("Encrypted")
        upload_file(filename)
        print("File uploaded")

elif(choice == 2):
    filename = input("Enter filename to decrypt: ")
    if download_file(filename):
        print("File downloaded")
        filedata = read_file("downloads/"+filename, "rb")
        decrypt_DES(filedata, filename)
        print("Decrypted")

else:
    print("Invalid Selection")


print("Done")
