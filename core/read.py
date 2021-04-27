def read_file(filename, readtype):
    myfile = open(filename, readtype)
    filedata = myfile.read()
    myfile.close()
    return filedata


def read_img(filename, readtype, *args):
    myfile = open(filename, readtype, encoding=args[0])
    filedata = myfile.read()
    myfile.close()
    return filedata
