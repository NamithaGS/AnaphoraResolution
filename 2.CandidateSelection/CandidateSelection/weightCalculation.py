import sys,math

from collections import Counter,defaultdict


GenderDict=defaultdict(Counter)
NumberDict=defaultdict(Counter)
finalDict=dict()

def createDict():
    GenderDict['any']['m']=5
    GenderDict['any']['any'] = 4
    GenderDict['any']['-'] = 2
    GenderDict['any']['f'] = 3

    GenderDict['m']['m'] = 5
    GenderDict['m']['any'] = 5
    GenderDict['m']['-'] = 2
    GenderDict['m']['f'] = 4

    GenderDict['f']['m'] = 5
    GenderDict['f']['any'] = 5
    GenderDict['f']['-'] = 1
    GenderDict['f']['f'] = 5

    GenderDict['-']['m'] = 1
    GenderDict['-']['any'] = 0
    GenderDict['-']['-'] = 3
    GenderDict['-']['f'] = 5

    NumberDict['sg']['sg']=3
    NumberDict['sg']['pl'] = 5
    NumberDict['sg']['any'] = 1
    NumberDict['sg']['-'] = 3

    NumberDict['pl']['sg']=5
    NumberDict['pl']['pl'] = 3
    NumberDict['pl']['any'] = 0
    NumberDict['pl']['-'] = 2

    NumberDict['any']['sg']=5
    NumberDict['any']['pl'] = 3
    NumberDict['any']['any'] = 1
    NumberDict['any']['-'] = 3

    NumberDict['-']['sg']=5
    NumberDict['-']['pl'] = 3
    NumberDict['-']['any'] = 0
    NumberDict['-']['-'] = 2

    finalDict['GDict']=GenderDict
    finalDict['NDict']=NumberDict

    print finalDict

def main():
    createDict()
    file=open("test_out.txt","rb")
    weightedFile=open("test_output.txt","w")
    for line in file:
        if line == "\r\n":
            weightedFile.write("\n")
            continue
        originalLine=line.strip()
        tokens=line.strip().split()
        if len(tokens[8]) > 1:
            extraCredit=5
        else:
             extraCredit=4
        value= int(finalDict['GDict'][tokens[3]][tokens[4]]) + int(finalDict['NDict'][tokens[5]][tokens[6]]) +  (5- int(tokens[7]))
        divValue=  (value + extraCredit) / float(4)
        weight= round(divValue)
        #print value, divValue, weight
        originalLine += "\t" + str(weight)

        weightedFile.write(originalLine)
        weightedFile.write("\n")

if __name__ == '__main__':main()

