#text files are easy to work with in python. Python has a few functions to handle txt files to save permantly (persistance)

#create and write to a file
#open (file name, argument for read write or append)
#write - makes a new file if none exists, and overwrites a file - w
f = open("myfile.txt", "w")
f.write("File now has text\n")
f.write("File has some more text")
f.close()

#reading - read a file
# f = open("myfile.txt", "r")
# print(f.readline())
# print(f.readline())


#some utilities to help read everything in a text file
with open("myfile.txt", "r") as f:
    while True:
        line = f.readline()
        if not line: #checks if the line is empty (EOF)
            break
        print(line)


