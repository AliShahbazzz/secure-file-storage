import os
from des import DesKey
from Crypto.Cipher import AES, ARC4
from key import mykey
from core.read import read_file, read_img
from core.download import download_file
from core.upload import upload_file
from fsplit.filesplit import Filesplit

# Splits the file into 2 parts


def split_file(filename):
    fs = Filesplit()
    filedata = read_file(filename, "r")
    split_length = (len(filedata)//2)
    if split_length % 2 != 0:
        split_length += 1
    fs.split(file=filename, split_size=split_length, output_dir="cache")
    return True

# Splits the file into 2 parts


def split_efile(filename):
    fs = Filesplit()
    filedata = read_file(filename, "rb")
    split_length = len(filedata)//2
    if split_length % 2 != 0:
        split_length += 1
    fs.split(file=filename, split_size=split_length, output_dir="cache")
    return True


# Merges the files into one

def merge_encrypted(filename):
    fs = Filesplit()
    fs.merge(input_dir="cache", cleanup=True)
    enc_file = open("cache/"+filename, "rb")
    filedata = enc_file.read()
    enc_file_copy = open("encryptedFiles/"+filename, "wb")
    enc_file_copy.write(filedata)
    enc_file.close()
    enc_file_copy.close()

    return True

# Merges the files into one


def merge_decrypted(filename):
    fs = Filesplit()
    fs.merge(input_dir="cache", cleanup=True)
    dec_file = open("cache/"+filename, "rb")
    filedata = dec_file.read()
    dec_file_copy = open("decryptedFiles/"+filename, "wb")
    dec_file_copy.write(filedata)
    dec_file.close()
    dec_file_copy.close()

    return True


# Applies AES to the file part-1

def encrypt_AES(text, filename):
    a = AES.new(mykey, mode=AES.MODE_EAX)
    text = str.encode(text)
    text = a.encrypt(text)
    mynonce = a.nonce
    key_file = open("non.py", "wb")
    key_file.write(mynonce)
    key_file.close()
    enc_file = open("cache/"+filename, "wb")
    enc_file.write(text)
    enc_file.close()
    return True


# Applies AC4 to the file part-2

def encrypt_AC4(text, filename):
    a = ARC4.new(mykey)
    text = str.encode(text)
    text = a.encrypt(text)
    enc_file = open("cache/"+filename, "wb")
    enc_file.write(text)
    enc_file.close()
    return True


# Decrypts the file part-1

def decrypt_AES(text, filename):
    mynonce = read_file("non.py", "rb")
    a = AES.new(mykey, mode=AES.MODE_EAX, nonce=mynonce)
    text = a.decrypt(text)
    text = text.decode()
    dec_file = open("cache/"+filename, "w")
    dec_file.write(text)
    dec_file.close()
    return True


# Decrypts the file part-2

def decrypt_AC4(text, filename):
    a = ARC4.new(mykey)
    text = a.decrypt(text)
    text = text.decode()
    dec_file = open("cache/"+filename, "w")
    dec_file.write(text)
    dec_file.close()
    return True


def main():
    choice = int(input("Choose: \n 1: Encrpt\n 2: Decrypt\n"))
    if(choice == 1):
        filename = input("Enter filename to encrypt: ")
        if split_file(filename):
            filename, file_extension = os.path.splitext(filename)
            file1 = filename+'_1'+file_extension
            file2 = filename+'_2'+file_extension
        filedata1 = read_file('cache/'+file1, "r")
        filedata2 = read_file('cache/'+file2, "r")
        if encrypt_AES(filedata1, file1):
            print("AES Encrypted")
        if encrypt_AC4(filedata2, file2):
            print("AC4 Encrypted")
        if merge_encrypted(filename+file_extension):
            print("Files merged")
        # upload_file(filename)
        # print("File uploaded")

    elif(choice == 2):
        filename = input("Enter filename to decrypt: ")
        # if download_file(filename):
        #     print("File downloaded")
        #     filedata = read_file("downloads/"+filename, "rb")
        if split_efile('cache/'+filename):
            filename, file_extension = os.path.splitext(filename)
        file1 = filename+'_1'+file_extension
        file2 = filename+'_2'+file_extension
        filedata1 = read_file('cache/'+file1, "rb")
        filedata2 = read_file('cache/'+file2, "rb")
        if decrypt_AES(filedata1, file1):
            print("AES Decrypted")
        if decrypt_AC4(filedata2, file2):
            print("AC4 Decrypted")
        if merge_decrypted(filename+file_extension):
            print("Files merged")

    else:
        print("Invalid Selection")

    print("Done")


if __name__ == '__main__':
    main()
