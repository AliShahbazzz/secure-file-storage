# from des import DesKey

# key = DesKey(b"mykey123")

# myfile = open("new.txt", "r")
# filedata = myfile.read()
# print(filedata)
# myfile.close()
# while len(filedata) % 8 != 0:
#     filedata += " "
# enc = str.encode(filedata)
# print(enc)
# filedata = key.encrypt(enc)
# print(filedata)
# enc_file = open("newEb.txt", "wb")
# enc_file.write(filedata)
# enc_file.close()


# myfile = open("newEb.txt", "rb")
# filedata = myfile.read()
# print(filedata)
# myfile.close()
# filedata = key.decrypt(filedata)
# print(filedata)
# print(filedata.decode())
# my_file = open("new.txt", "w")
# my_file.write(filedata)
# my_file.close()

# from fsplit.filesplit import Filesplit

# fs = Filesplit()


# #fs.split(file="test.txt", split_size=500000, output_dir='.')

# fs.merge(input_dir=".", cleanup=True)

from Crypto.Cipher import AES, ARC4
import os

mynonce = os.urandom(16)
mynonce = mynonce
print(mynonce)
mykey = b")H@McQfTjWnZq4t7w!z%C*F-JaNdRgUk"

text = "My name is Shahbaz"
print("1 " + text)

text = str.encode(text)
print("2 " + str(text))

a = AES.new(mykey, mode=AES.MODE_EAX)
#abc = a.nonce
# print(abc)
text = a.encrypt(text)
print("3 " + str(text))

a = AES.new(mykey, mode=AES.MODE_EAX, nonce=mynonce)
text = a.decrypt(text)
print("4 " + str(text))

text = text.decode()
print("5 " + text)

print(text)
