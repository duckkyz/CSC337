import os

if __name__ == "__main__":
    fileExt = str(os.getcwd()) + "/characters.txt"
    myfile = open((fileExt),'r')
    for line in myfile:
        seperate = line.split(" - ", 1)
        for word in seperate:
            print (str("<td>" + word + "</td>"))
            #get rid of the newline after the last word
        print ("<td>IMAGELOC</td>")
        print ()

