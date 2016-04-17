import codecs
from collections import defaultdict,Counter
from trainStoryProcessor import createDict

rootDir=dict()
stop_list=[]

def isAnaphora(word,POS,stop_list):
    if POS == "PRP" and word not in stop_list:
        return True
    return False

def candidateSelection(rootDir,word,sentenceNum,gender):
    possibleCandidates=[]

    if sentenceNum > 0:
        previousLine = rootDir[sentenceNum - 1]
        if gender=="m" or gender=="f" or gender=="n" or gender=="fn" :
            for wordDict in previousLine:
                if len(rootDir[sentenceNum-1][wordDict]) > 5:
                    if ( ( rootDir[sentenceNum-1][wordDict][5] == gender) and (rootDir[sentenceNum-1][wordDict][1] == "NN" or rootDir[sentenceNum-1][wordDict][1]=="NNP") ):
                        possibleCandidates.append(wordDict)
        elif gender=="mf":
            for wordDict in previousLine:
                if len(rootDir[sentenceNum - 1][wordDict]) > 5:
                    currentWordGender = rootDir[sentenceNum][wordDict][5]
                    if( (currentWordGender == "m" or currentWordGender == "f" or currentWordGender == "mf") and (rootDir[sentenceNum-1][wordDict][1] == "NN" or rootDir[sentenceNum-1][wordDict][1]=="NNP") ):
                        possibleCandidates.append(wordDict)
        elif gender=="any":
            for wordDict in previousLine:
                if ( rootDir[sentenceNum-1][wordDict][1] == "NN" or rootDir[sentenceNum-1][wordDict][1]=="NNP" ):
                    if len(rootDir[sentenceNum - 1][wordDict]) > 5:
                        possibleCandidates.append(wordDict)

        return possibleCandidates



def processLineByLine(rootDir,stop_list):
    result=""
    for i in range (0,len(rootDir)):
        for wordDict in rootDir[i]:
            word=rootDir[i][wordDict][0]
            POS = rootDir[i][wordDict][1]
            if isAnaphora(word,POS,stop_list):
                if len(rootDir[i][wordDict]) > 5:
                    gender = rootDir[i][wordDict][5]
                    possibleCand = candidateSelection(rootDir,word, i, gender)
                    for candidate in possibleCand:

                        result =  result + word + "\t"  + (rootDir[i-1][candidate][0] or "-") +  "\t"+ (rootDir[i-1][candidate][1] or "-") + "\t"+(rootDir[i][wordDict][5] or "-")+ "\t" + (rootDir[i-1][candidate][5] or "-") + "\t" + (rootDir[i][wordDict][6] or "-") + "\t" + (rootDir[i-1][candidate][6] or "-")
                        result = result + "\n"
    return result

def main():
    stop_list = []
    fp = codecs.open("stop_list.txt", "rb")
    for line in fp:
        stop_list.append(line)

    out_file=open("out.txt","wb")

    rootDir= createDict()
    result= processLineByLine(rootDir,stop_list)
    out_file.write(result)

if __name__ == '__main__':main()
