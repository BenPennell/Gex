# this file was used to parse the gex voicelines file, voicelines.txt

inFile = open("voicelines2.txt")
outFile = open("GexVoiceLines.txt", "w")
lines = inFile.readlines()

for line in lines:
    if line[len(line) - 2] == "\'":
        line = line[:-2]
        line = line + "\n"

    newLine = ""
    for i in range(len(line)):
        if line[i] != "\"":
            newLine += line[i]
    outFile.write(newLine)
    