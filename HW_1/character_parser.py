import os

if __name__ == "__main__":
    fileExt = str(os.getcwd()) + "/characters.txt"
    newExt = str(os.getcwd()) + "/testCharFile.html"
    myfile = open((fileExt),'r')
    writeFile = open((newExt),'w')
    writeFile.write(str("<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">"))
    writeFile.write("\n<table>\n\t<tr>")
    writeFile.write("\n\t\t<th>Character</th>")
    writeFile.write("\n\t\t<th>Description</th>")
    writeFile.write("\n\t\t<th>Image</th>")
    writeFile.write("\n\t</tr>")

    for line in myfile:
        try:
            seperate = line.split(" - ", 1)
            fix = seperate[1].split("\n",1)
            writeFile.write("\n\t<tr>")
            line1 = ("\n\t\t<td>" + seperate[0] + "</td>")
            line2 = ("\n\t\t<td>" + fix[0] + "</td>")
            line3 = ("\n\t\t<td>IMAGELOC</td>")
            writeFile.write(line1)
            writeFile.write(line2)
            writeFile.write(line3)
            writeFile.write("\n\t</tr>")

        except:
            print("error?")
    writeFile.write("\n</table>")
    myfile.close()
    writeFile.close()

