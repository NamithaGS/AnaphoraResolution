#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
import codecs
import os
from trainStoryProcessor import createDict

def candidateSelection(rootDir,word,sentenceNum,gender):
    possibleCandidates=[]
    previousLine = {}
    if sentenceNum > 0:
        previousLine["0"] = rootDir[sentenceNum]
        previousLine["1"]=rootDir[sentenceNum - 1]
        if gender=="m" or gender=="f" or gender=="n" or gender=="fn" :
            for linevalue in previousLine.itervalues():
                for wordDict in linevalue.itervalues():
                    if len(wordDict) > 9:
                        if ( ( wordDict[7] == gender) and (wordDict[1] == "NN" or wordDict[1]=="NNP") ):
                            possibleCandidates.append(wordDict)
        elif gender=="mf":
            for linevalue in previousLine.itervalues():
                for wordDict in linevalue.itervalues():
                    if len(wordDict) > 9:
                        currentWordGender = wordDict[7]
                        if( (currentWordGender == "m" or currentWordGender == "f" or currentWordGender == "mf") and (wordDict[1] or wordDict[1]=="NNP") ):
                            possibleCandidates.append(wordDict)
        else:
            for linevalue in previousLine.itervalues():
                for wordDict in linevalue.itervalues():
                    if( wordDict[1] == "NN" or wordDict[1]=="NNP" ):
                        if len(wordDict) > 9:
                            possibleCandidates.append(wordDict)
            
        return possibleCandidates
    else:
        return []



def processLineByLine(rootDir,stop_list):
    result=""
    isann=False
    for i in range (0,len(rootDir)):
        for wordDict in rootDir[i]:
            word=rootDir[i][wordDict][0]
            POS = rootDir[i][wordDict][1]         
            if rootDir[i][wordDict][5]:#isAnaphora(word,POS,stop_list):
                ann_num = rootDir[i][wordDict][9]
                #print(rootDir[i][wordDict][0])
                if len(rootDir[i][wordDict]) > 5:
                    gender = rootDir[i][wordDict][7]
                    possibleCand = candidateSelection(rootDir,word, i, gender)
                    
                    for candidate in possibleCand:
                        can_num=candidate[10]
                        if(ann_num==can_num and candidate[6]==True):
                            isann=True
                        else:
                            isann=False
                        result =  result + word + "\t"  + (candidate[0] or "-") +  "\t"+ (candidate[1] or "-") + "\t"+(rootDir[i][wordDict][7] or "-")+ "\t" + (candidate[7] or "-") + "\t" + (rootDir[i][wordDict][8] or "-") + "\t" + (candidate[8] or "-")+ "\t" + str(isann)
                        result = result + "\n"
    return result

def main():
    stop_list = []
    out_file=codecs.open("train_out.txt","w")
    foldername='C:/USC Course material/CS - 544 NLP/Research Project/Final Idea/Code/workspace/annaphora/trainfiles'
    filelist=os.listdir(foldername)
    for x in filelist:
            print(foldername+'/' + x)
            rootDir= createDict(foldername+'/' + x)
            result= processLineByLine(rootDir,stop_list)
            out_file.write(result)
if __name__ == '__main__':main()
