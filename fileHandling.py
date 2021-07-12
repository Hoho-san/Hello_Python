myfile = open("myfile", "r")    # r - read, w - write, a - append, r+ - read and write
for file in myfile.readlines(): # to read what is in the files
    print(file)
myfile.close
# when writing in a file,you should use \n to put it to the next line