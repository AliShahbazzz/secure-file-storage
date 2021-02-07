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
