import os
from des import DesKey
from Crypto.Cipher import AES
from key import myDESkey, myAESkey
from core.read import read_file, read_img
from core.download import download_file
from core.upload import upload_file
from fsplit.filesplit import Filesplit

key = DesKey(myDESkey)


# Splits the file into 3 parts

def split_file(filename):
    fs = Filesplit()
    filedata = read_file(filename, "r")
    fs.split(file=filename, split_size=(
        len(filedata)//2)+1, output_dir="cache")
    return True

# Splits the file into 3 parts


def split_efile(filename):
    fs = Filesplit()
    filedata = read_file(filename, "rb")
    fs.split(file=filename, split_size=(
        len(filedata)//2)+1, output_dir="cache")
    return True


# Merges the files into one

def merge_file():
    fs = Filesplit()
    fs.merge(input_dir="cache", cleanup=True)
    return True


# Applies DES to the file part 1

def encrypt_DES(text, filename):
    print(text)
    spaces = 0
    spaces = len(text) % 8
    if spaces != 0:
        spaces = 8-spaces
        text += " "*(spaces-1)
        text += str(spaces)
    print(text)
    text = str.encode(text)
    print(text)
    text = key.encrypt(text)
    print(text)
    enc_file = open("cache/"+filename, "wb")
    enc_file_copy = open("encryptedFiles/"+filename, "wb")
    enc_file.write(text)
    enc_file_copy.write(text)
    enc_file.close()
    enc_file_copy.close()
    return True


# Decrypts the file part-1

def decrypt_DES(text, filename):
    text = key.decrypt(text)
    print(text)
    text = text.decode()
    print(text)
    spaces = len(text) % 8
    if spaces != 0:
        spaces = text[-1]
        text = text[:-int(spaces)]
    dec_file = open("decryptedFiles/"+filename, "w")
    dec_file.write(text)
    dec_file.close()
    # dec_file = open("downloads/"+filename, "w")
    # dec_file.write(text)
    # dec_file.close()
    return True


# Applies AES to the file part-2

def encrypt_AES(text, filename):
    text = str.encode(text)
    print(text)
    a = AES.new(myAESkey, mode=AES.MODE_EAX)
    text = a.encrypt(text)
    print(text)
    enc_file = open("cache/"+filename, "wb")
    enc_file_copy = open("encryptedFiles/"+filename, "wb")
    enc_file.write(text)
    enc_file_copy.write(text)
    enc_file.close()
    enc_file_copy.close()
    return True


# Decrypts the file part-2

def decrypt_AES(text, filename):
    a = AES.new(myAESkey, mode=AES.MODE_EAX)
    text = a.decrypt(text)
    print(text)
    text = text.decode()
    print(text)
    dec_file = open("cache/"+filename, "w")
    dec_file_copy = open("decryptedFiles/"+filename, "w")
    dec_file.write(text)
    dec_file_copy.write(text)
    dec_file.close()
    dec_file_copy.close()
    # dec_file = open("downloads/"+filename, "w")
    # dec_file.write(text)
    # dec_file.close()
    return True


def main():
    choice = int(input("Choose: \n 1: Encrpt\n 2: Decrypt\n"))
    if(choice == 1):
        filename = input("Enter filename to encrypt: ")
        if split_file(filename):
            filename, file_extension = os.path.splitext(filename)
            file1 = filename+'_1'+file_extension
            file2 = filename+'_2'+file_extension
            file3 = filename+'_3'+file_extension
        print(file1, file2, file3)
        filedata1 = read_file('cache/'+file1, "r")
        filedata2 = read_file('cache/'+file2, "r")
        #filedata3 = read_file(file3, "r")
        if encrypt_DES(filedata1, file1):
            print("DES Encrypted")
        if encrypt_AES(filedata2, file2):
            print("AES Encrypted")
        if merge_file():
            print("Files merged")
        # upload_file(filename)
        # print("File uploaded")

    elif(choice == 2):
        filename = input("Enter filename to decrypt: ")
        # if download_file(filename):
        #     print("File downloaded")
        #    filedata = read_file("downloads/"+filename, "rb")
        if split_efile('cache/'+filename):
            filename, file_extension = os.path.splitext(filename)
            file1 = filename+'_1'+file_extension
            file2 = filename+'_2'+file_extension
            file3 = filename+'_3'+file_extension
        filedata1 = read_file('cache/'+file1, "rb")
        filedata2 = read_file('cache/'+file2, "rb")
        #filedata3 = read_file(file3, "r")
        if decrypt_DES(filedata1, file1):
            print("DES Decrypted")
        if decrypt_AES(filedata2, file2):
            print("AES Decrypted")
        if merge_file():
            print("Files merged")

    else:
        print("Invalid Selection")

    print("Done")


if __name__ == '__main__':
    main()
    # merge_file()
