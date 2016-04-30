#!/usr/bin/python3
import os
import sys
import json
from _ast import Str

def getFileLength(fname):
    with open(fname,encoding='utf-8') as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def main():
    
    #annotation_path = '/Users/PavanLupane/Documents/EclipseWorkspace/pythonWork/anaphora-resolution-work/evaluate-data/annotated-data' 
#     annotation_path = '/Users/PavanLupane/Documents/EclipseWorkspace/pythonWork/anaphora-resolution-work/evaluate-data/annotated-data/testoutput'
    annotation_path = '/Users/PavanLupane/Documents/EclipseWorkspace/pythonWork/anaphora-resolution-work/evaluate-data/ano'
    evalDict = dict()
    fileCnt = 0;
    
    for root, dirs, files in os.walk(sys.argv[1],topdown=True):
        for name in files:
            print(name)
            evalList = list()
            crf_anaphoraDict = dict()
            anno_anaphoraDict = dict()
    
            totalCnt = 0
            totalCandidates = 0
            truePositives = 0
            trueNegatives = 0
            falsePositives = 0
            falseNegatives = 0
            
            
            path = os.path.join(root, name)
            if '.txt' in name:      #Evaluate only .txt files
                
                #path1 = annotation_path+'/'+name[:-4]+'_ant.txt'        #setup the path for annotated data
                path1 = annotation_path+'/'+name        #setup the path for annotated data
                
                if getFileLength(path) == getFileLength(path1):     #check if both files have same number of lines
                    fileCnt += 1
                    with open(path, 'r', encoding='utf-8') as f_crf, open(path1, 'r', encoding='utf-8') as f_anno: 
                        for crf_line, annotation_line in zip(f_crf, f_anno):
#                             print(crf_line)
#                             print(annotation_line)
                            
                            crf_line_tokens = crf_line.rstrip('\n').split('\t')
                            annotation_line_tokens = annotation_line.rstrip('\n').split('\t')
                            
#                             print(crf_line_tokens)
#                             print(annotation_line_tokens)
#                             print(len(annotation_line_tokens))
                            #Calculations of Positives
                            if len(annotation_line_tokens) > 1:
                                totalCandidates += 1
                                if(annotation_line_tokens[12] == 'True'):
                                    #first add the anaphora to the anno_anaphoraDict
                                    if annotation_line_tokens[0] in anno_anaphoraDict:
                                        anno_anaphoraDict[annotation_line_tokens[0]] += 1
                                    else:
                                        anno_anaphoraDict[annotation_line_tokens[0]] = 1
                                    
                                    #update total correct anaphoras in annotated corpus
                                    totalCnt += 1
                                    
                                #Calculate True Positives - check if anno and crf anaphora are both true 
                                if annotation_line_tokens[12] == 'True' and crf_line_tokens[12] == 'True':
                                    truePositives += 1
                                    if crf_line_tokens[0] in crf_anaphoraDict: 
                                        crf_anaphoraDict[crf_line_tokens[0]] += 1
                                    else:
                                        crf_anaphoraDict[crf_line_tokens[0]] = 1
                                          
                                #Calculate True Negatives 
                                elif annotation_line_tokens[12] == 'False' and crf_line_tokens[12] == 'False':
                                    trueNegatives += 1
                                
                                #Calculate False Positives
                                elif annotation_line_tokens[12] == 'False' and crf_line_tokens[12] == 'True':
                                    falsePositives += 1
                                
                                #Calculate False Negatives
                                elif  annotation_line_tokens[12] == 'True' and crf_line_tokens[12] == 'False':
                                    falseNegatives += 1
                                
                                
                else:
                    print("Files are of different length. Some data missed while processing file ",name)
#                 print("Name is :: ",name)
                print("Total Annotated Anaphoras :: ", totalCnt)
    
                print(anno_anaphoraDict)
                print(crf_anaphoraDict)
                print("truePositives ::",truePositives)
                print("falsePositives ::",falsePositives)
                print("trueNegatives ::",trueNegatives)
                print("falseNegatives ::",falseNegatives)                         
                evalList.append(totalCnt)
                evalList.append(totalCandidates)
                evalList.append(truePositives)
                evalList.append(falsePositives)
                evalList.append(trueNegatives)
                evalList.append(falseNegatives)
                
                precision = truePositives / (truePositives + falsePositives)
                
                recall =  truePositives / (truePositives + falseNegatives)
                
                accuracy = (trueNegatives + truePositives) / (trueNegatives + falsePositives)
                
                if precision + recall > 0:
                    fmeasure = (2 * precision * recall)/(precision+recall)
                else:
                    fmeasure = 0
               
                evalList.append(precision)
                evalList.append(recall)
                evalList.append(fmeasure)
                stringVal = 'S'+str(fileCnt)+','+str(totalCandidates)+','+str(round((fmeasure*100),5))
                stringVal1 = 'S'+str(fileCnt)+','+str(totalCnt)+','+str(truePositives)
                print(stringVal)
                # Source :: http://www.kdnuggets.com/faq/precision-recall.html
    
                print("Correctly found Anaphoras:: ",truePositives)
                print("Precision is :: ",precision)
                print("Recall is :: ",recall)
                print("F-Measure is :: ",fmeasure)
                evalDict[name] = evalList 
    print("Evaluation is ::",evalDict)
    with open('evaluationParam.txt', 'w',encoding='utf8') as fp:
        json.dump(evalDict, fp, ensure_ascii=False)

if __name__ == "__main__":main()
##### evalDict index list #####
# [0] -> Total Annotated Anaphoras
# [1] -> totalCandidates
# [2] -> truePositives
# [3] -> falsePositives
# [4] -> trueNegatives
# [5] -> falseNegatives
# [6] -> precision
# [7] -> recall
# [8] -> fmeasure