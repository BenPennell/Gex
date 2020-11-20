# this file was used to parse the gex voicelines file, voicelines.txt

inFile = open("ParsedLines.txt")
outFile = open("GexVoiceLines.txt", "w")
lines = inFile.readlines()

'''
for line in lines:
    if line[0] == "\'" or line[0] == "\"":
        if line[len(line) - 2] == "\'":
            line = line[:-2]
            line = line + "\n"

        newLine = ""
        for i in range(len(line)):
            if line[i] != "\"":
                newLine += line[i]
        outFile.write(newLine)
'''

for line in lines:
    if line[0] == "\'":
        line = line[1:]

    if line[len(line) - 2] == "\'":
        line = line[:-2]
        line = line + "\n"

    newLine = ""
    for i in range(len(line)):
        if line[i] != "\"":
            newLine += line[i]
    outFile.write(newLine)
    