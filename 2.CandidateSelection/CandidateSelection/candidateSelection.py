#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
import codecs
import os
from trainStoryProcessor import createDict

####################################################
#This function selects the candidate antecedents for a given annaphora. 
#The antecedents are selected from the current and previous line.
#Antecedents are selected based on Gender and POS tag currently.
#We are planning add Number (singular/plural) and person (1/2/3 person) 
####################################################
def candidateSelection(rootDir,word,sentenceNum,gender):
    possibleCandidates=[]
    previousLine = {}
    if sentenceNum > 3:
        previousLine["0"] = rootDir[sentenceNum]
        previousLine["1"]=rootDir[sentenceNum - 1]
        previousLine["2"]=rootDir[sentenceNum - 2]
        previousLine["3"]=rootDir[sentenceNum - 3]
        previousLine["4"]=rootDir[sentenceNum - 4]
    if sentenceNum > 2:
        previousLine["0"] = rootDir[sentenceNum]
        previousLine["1"]=rootDir[sentenceNum - 1]
        previousLine["2"]=rootDir[sentenceNum - 2]
        previousLine["3"]=rootDir[sentenceNum - 3]
    if sentenceNum > 1:
        previousLine["0"] = rootDir[sentenceNum]
        previousLine["1"]=rootDir[sentenceNum - 1]
        previousLine["2"]=rootDir[sentenceNum - 2]
    elif sentenceNum > 0:
        previousLine["0"] = rootDir[sentenceNum]
        previousLine["1"]=rootDir[sentenceNum - 1]
#         if gender=="m" or gender=="f" or gender=="n" or gender=="fn" :
#             for linevalue in previousLine.itervalues():
#                 for wordDict in linevalue.itervalues():
#                     if len(wordDict) > 9:
#                         if ( wordDict[0]!='NULL' and ( wordDict[7] == gender) and (wordDict[1] == "NN" or wordDict[1]=="NNP" or (wordDict[5]==True and wordDict[6]==True and wordDict[0]!=word))):
#                             possibleCandidates.append(wordDict)
#         elif gender=="mf":
#             for linevalue in previousLine.itervalues():
#                 for wordDict in linevalue.itervalues():
#                     if len(wordDict) > 9:
#                         currentWordGender = wordDict[7]
#                         if( wordDict[0]!='NULL' and (currentWordGender == "m" or currentWordGender == "f" or currentWordGender == "mf") and (wordDict[1]=="NP" or wordDict[1]=="NNP" or (wordDict[5]==True and wordDict[6]==True and wordDict[0]!=word))):
#                             possibleCandidates.append(wordDict)
#         else:
    templist=[]
    if (len(previousLine)!=0):    
        for linekey, linevalue in previousLine.iteritems():
            for wordDict in linevalue.itervalues():
                if( wordDict[0]!='NULL' and (wordDict[1] == "NN" or wordDict[1]=="NNP" or (wordDict[5]==True and wordDict[6]==True and wordDict[0]!=word))):
                    if len(wordDict) > 9:
                        templist = wordDict
                        templist.append(linekey)
                        possibleCandidates.append(templist)
        
            
        return possibleCandidates
    else:
        return []


########################################################################
#This function processes all the sentences in the input story file one by one
#Selects annaphoras, and calls the candidateSelection routine for the selected annaphoras
######################################################################### 
def processfileLineByLine(rootDir):
    result=""
    isann=False
    for i in range (0,len(rootDir)):
        for wordDict in rootDir[i]:
            word=rootDir[i][wordDict][0] 
            isann = rootDir[i][wordDict][5]
            #Check if the function is an annaphora (Should be PRP, B-NP and tagged n the training data)         
            if isann:
                ann_num = rootDir[i][wordDict][9]
                if len(rootDir[i][wordDict]) > 5:
                    gender = rootDir[i][wordDict][7]
                    #Fetch list of candidate antecedents for the annaphora
                    possibleCand = candidateSelection(rootDir,word, i, gender)                
                    for candidate in possibleCand:
                        #print(ann_num + " - " + candidate[0] + " - " + str(candidate[5]) + " - " + str(candidate[6]))
                        can_num=candidate[10]
                        #Check if the candidate is the marked/annotated antecedent in the training data
                        if(ann_num==can_num and candidate[6]==True):
                            iscurrCandidate=True
#                         elif (candidate[5]==True and candidate[6]==True):
#                              iscurrCandidate=True
                        else:
                            iscurrCandidate=False
                        result =  result + word + "\t"  + (candidate[0] or "-") +  "\t"+ (candidate[1] or "-") + "\t"+(rootDir[i][wordDict][7] or "-")+ "\t" + (candidate[7] or "-") + "\t" + (rootDir[i][wordDict][8] or "-") + "\t" + (candidate[8] or "-")+ "\t" + candidate[11] + "\t" + str(iscurrCandidate)
                        result = result + "\n"
    result = result + "\n"
    return result

###############################################################
#Program starts here 
############################################################### 
def main():
    out_file=codecs.open("test_out.txt","w")
    foldername='C:/USC Course material/CS - 544 NLP/Research Project/Final Idea/Code/workspace/annaphora/testfiles'
    #Process one file at a time
    filelist=os.listdir(foldername)
    for x in filelist:
            print(foldername+'/' + x)
            rootDir= createDict(foldername+'/' + x)
            result= processfileLineByLine(rootDir)
            out_file.write(result)
if __name__ == '__main__':main()
