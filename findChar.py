def findChar(list, char):
    newString = []
    for l in list:
        if l.find(char) > -1:
            newString.append(l)
    print newString
