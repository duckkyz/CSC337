import os

if __name__ == "__main__":
    fileExt = str(os.getcwd()) + "/characters.txt"
    newExt = str(os.getcwd()) + "/testCharFile.html"
    myfile = open((fileExt),'r')
    writeFile = open((newExt),'w')

    writeFile.write("<table>\n<tr>")
    writeFile.write("<th><b>Character</b></th>")
    writeFile.write("<th><b>Description</b></th>")
    writeFile.write("<th><b>Image</b></th>")
    writeFile.write("</tr>")

    for line in myfile:
        try:
            writeFile.write("<tr>")
            seperate = line.split(" - ", 1)
            fix = seperate[1].split("\n",1)
            line1 = ("<td>" + seperate[0] + "</td>\n")
            line2 = ("<td>" + fix[0] + "</td>\n")
            line3 = ("<td>IMAGELOC</td>")
            writeFile.write(line1)
            writeFile.write(line2)
            writeFile.write(line3)
            writeFile.write("</tr>")

        except:
            writeFile.write("\n\n")
    writeFile.write("</table>")
    myfile.close()
    writeFile.close()

