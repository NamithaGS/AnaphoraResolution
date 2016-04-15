from collections import defaultdict,Counter

dictionary = defaultdict()
wordDict=defaultdict()

def getGender(word):
    return "m"

def getPOSTag(word):
    return "NN"

def getSP(word):
    return "s"

def isAnaphora(word):
    return False

def candidateSelection(word,lineNum,gender):
    possibleCandidates=[]
    previousLine = dictionary[lineNum - 1]
    if gender=="m" or gender=="f" or gender=="n" or gender=="fn" :
        for word in previousLine:
            if word.getGender == gender:
                possibleCandidates.add(word)
    elif gender=="mf":
        for word in previousLine:
            if word.getGender == "m" or word.getGender == "f" or word.getGender == "mf" :
                possibleCandidates.add(word)
    elif gender=="any":
        for word in previousLine:
                possibleCandidates.add(word)
    return possibleCandidates

def processLine(line,lineNum):

    list = []

    for word in line.split(" "):
        gender = getGender(word)

        if not isAnaphora(word):
            POS= getPOSTag(word)
            if POS == "NN":
                sp=getSP(word)
                list.append(gender)
                list.append(sp)
                wordDict[word]=list
        else:
            possibleCand= candidateSelection(word,lineNum,gender)
            for candidate in possibleCand:
                print candidate

        dictionary[lineNum] = wordDict

def main():
    input_file=open("story10.txt","rb")
    lines= input_file.read().split("|")
    count=1
    for line in lines:
        processLine(line,count)
        count+=1

    print dictionary

if __name__ == '__main__':main()
