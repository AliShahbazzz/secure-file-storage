from des import DesKey
from core.read import read_file
from key import mykey

key = DesKey(mykey)


def encrypt_DES(text, filename):
    spaces = 0
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


choice = int(input("Choose: \n 1: Encrpt\n 2: Decrypt\n"))
if(choice == 1):
    filename = input("Enter filename to encrypt: ")
    filedata = read_file(filename, "r")
    encrypt_DES(filedata, filename)
    print("Encrypted")

elif(choice == 2):
    filename = input("Enter filename to decrypt: ")
    filedata = read_file("encryptedFiles/"+filename, "rb")
    decrypt_DES(filedata, filename)
    print("Decrypted")

else:
    print("Invalid Selection")


print("Done")
