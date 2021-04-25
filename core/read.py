def read_file(filename, readtype):
    myfile = open(filename, readtype)
    filedata = myfile.read()
    myfile.close()
    return filedata
