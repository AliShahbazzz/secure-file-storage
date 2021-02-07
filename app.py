from des import DesKey

key = DesKey(b"mykey123")


def read_file(filename, readtype):
    myfile = open(filename, readtype)
    filedata = myfile.read()
    myfile.close()
    return filedata


def encrypt_DES(text, filename):
    while len(text) % 8 != 0:
        text += " "
    text = str.encode(text)
    text = key.encrypt(text)
    enc_file = open("encryptedFiles/"+filename, "wb")
    enc_file.write(text)
    enc_file.close()
    return True


def decrypt_DES(text, filename):
    text = key.decrypt(text)
    text = text.decode()
    dec_file = open("decryptedFiles/"+filename, "w")
    dec_file.write(text)
    dec_file.close()


choice = int(input("Choose: \n 1: Encrpt\n 2: Decrypt\n"))
if(choice == 1):
    filename = input("Enter filename to encrypt: ")
    filedata = read_file(filename, "r")
    # myfile = open(filename, "r")
    # filedata = myfile.read()
    # myfile.close()
    encrypt_DES(filedata, filename)
    print("Encrypted")

elif(choice == 2):
    filename = input("Enter filename to decrypt: ")
    filedata = read_file("encryptedFiles/"+filename, "rb")
    # myfile = open("encryptedFiles/"+filename, "rb")
    # filedata = myfile.read()
    # myfile.close()
    decrypt_DES(filedata, filename)
    print("Decrypted")

else:
    print("Invalid Selection")


print("Done")
