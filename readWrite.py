file  = open("test.txt")
#read all the contents of file

#print(file.read(5))

#print(file.readline())
#print(file.readline())

#print line by line using readline method

#line = file.readline()
#while line!="":
#   print(line)
#    line =file.readline()


for line in file.readlines():
    print(line)




file.close()