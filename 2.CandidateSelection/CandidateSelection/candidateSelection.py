#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
import codecs
import os
from trainStoryProcessor import createRootList

####################################################
#This function selects the candidate antecedents for a given annaphora. 
#The antecedents are selected from the current and 5 previous lines.
#During training we select all candidate antecedents between annaphora and actual antecedent
#During testing, we select all candidates between annaphora and previous 3 lines
####################################################
def candidateSelection(rootList,word,sentenceNum,ann_position, ann_num):
    possibleCandidates=[]
    candidateLines = []
    #The sentence lists are reversed so that we can read backwards from the annaphora until the candidate
    #look back 5 previous lines
    if sentenceNum > 4:
        candidateLines.insert(0,rootList[sentenceNum][::-1])
        candidateLines.insert(1,rootList[sentenceNum - 1][::-1])
        candidateLines.insert(2,rootList[sentenceNum - 2][::-1])
        candidateLines.insert(3,rootList[sentenceNum - 3][::-1])
        candidateLines.insert(4,rootList[sentenceNum - 4][::-1])
        candidateLines.insert(5,rootList[sentenceNum - 5][::-1])
    #look back 4 previous lines
    elif sentenceNum > 3:
        candidateLines.insert(0,rootList[sentenceNum][::-1])
        candidateLines.insert(1,rootList[sentenceNum - 1][::-1])
        candidateLines.insert(2,rootList[sentenceNum - 2][::-1])
        candidateLines.insert(3,rootList[sentenceNum - 3][::-1])
        candidateLines.insert(4,rootList[sentenceNum - 4][::-1])
    #look back 3 previous lines
    if sentenceNum > 2:
        candidateLines.insert(0,rootList[sentenceNum][::-1])
        candidateLines.insert(1,rootList[sentenceNum - 1][::-1])
        candidateLines.insert(2,rootList[sentenceNum - 2][::-1])
        candidateLines.insert(3,rootList[sentenceNum - 3][::-1])
    #look back 2 previous lines
    elif sentenceNum > 1:
        candidateLines.insert(0,rootList[sentenceNum][::-1])
        candidateLines.insert(1,rootList[sentenceNum - 1][::-1])
        candidateLines.insert(2,rootList[sentenceNum - 2][::-1])
    #look back 1 previous lines
    elif sentenceNum > 0:
        candidateLines.insert(0,rootList[sentenceNum][::-1])
        candidateLines.insert(1,rootList[sentenceNum - 1][::-1])
    else:
        candidateLines.insert(0,rootList[sentenceNum][::-1])
    cont = True
    lineCntr=0
    bnp_Countr=-1
    start=False
    #If previous sentences exist do this
    if (len(candidateLines)!=0):    
        for linevalue in candidateLines: # For each line
            for wordDict in linevalue: #For each word word in line
                #Look back words only after annaphora is encountered
                if(wordDict[5]==True and wordDict[10]==ann_num):
                    start=True
                if start:
                    templist=[]
                    if(wordDict[2] == "B-NP"):
                        bnp_Countr+=1
                    #If valid candidate is found i.e NN or NNP add to selected list of candidates
                    if( wordDict[0]!='NULL' and (wordDict[1] == "NN" or wordDict[1]=="NNP" or (wordDict[5]==True and wordDict[6]==True))):
                        if len(wordDict) > 9:
                            templist = wordDict
                            can_num = wordDict[11]
                            templist.append(str(bnp_Countr))
                            templist.append(str(lineCntr))
                            possibleCandidates.append(templist)
                            #stop process when manually annotated candidate is encountered
                            if(ann_num==can_num):
                                cont = False
                                break                           
            if(cont==False):
                break
            lineCntr+=1
        return possibleCandidates
    else:
        return []


########################################################################
#This function processes all the sentences in the input story file one by one
#Selects annaphoras, and calls the candidateSelection routine for the selected annaphoras
######################################################################### 
def processfileLineByLine(cnt, rootList):
    result=""
    isann=False
    
    for i in range (0,len(rootList)):
        ann_position=0 #annaphora position in sentence
        for wordDict in rootList[i]:
            word=wordDict[0] 
            isann = wordDict[5]
            #Check if the word is an annaphora (Should be PRP, B-NP and tagged n the training data)         
            if isann:
                ann_num = wordDict[10]
                if len(wordDict) > 5:
                    #Fetch list of candidate antecedents for the annaphora
                    possibleCand = candidateSelection(rootList,word, i,ann_position, ann_num)                
                    for candidate in possibleCand:
                        can_num=candidate[11]
                        #Check if the candidate is the marked/annotated antecedent in the training data
                        if(ann_num==can_num and candidate[6]==True):
                            iscurrCandidate=True
                        else:
                            iscurrCandidate=False
                        #result =  result + str(cnt) + '\t' + ann_num + '\t' + word + "\t"  + (candidate[0] or "-") +  "\t"+ (candidate[1] or "-") + "\t"+(wordDict[7] or "-")+ "\t" + (candidate[7] or "-") + "\t" + (wordDict[8] or "-") + "\t" + (candidate[8] or "-")+ "\t" + candidate[13] + "\t" + (candidate[3] or "-") + "\t" + (wordDict[9] or "-") + "\t" + (candidate[9] or "-") + '\t' + candidate[12] + '\t' + str(iscurrCandidate)
                        result =  result  + word + "\t"  + (candidate[0] or "-") +  "\t"+ (candidate[1] or "-") + "\t"+(wordDict[7] or "-")+ "\t" + (candidate[7] or "-") + "\t" + (wordDict[8] or "-") + "\t" + (candidate[8] or "-")+ "\t" + candidate[13] + "\t" + (candidate[3] or "-") + "\t" + (wordDict[9] or "-") + "\t" + (candidate[9] or "-") + '\t' + candidate[12] + '\t' + str(iscurrCandidate)
                        result = result + "\n"
            ann_position+=1
    #result = result + "\n"
    return result

###############################################################
#Program starts here 
############################################################### 
def main():
    out_file=codecs.open("train_out.txt","w")
    foldername='C:/USC Course material/CS - 544 NLP/Research Project/Final Idea/Code/workspace/annaphora/trainfiles'
    #Process one file at a time
    filelist=os.listdir(foldername)
    i=1
    for x in filelist:
            print(foldername+'/' + x)
            rootList= createRootList(foldername+'/' + x)
            result= processfileLineByLine(i,rootList)
            i+=1
            out_file.write(result)
if __name__ == '__main__':main()