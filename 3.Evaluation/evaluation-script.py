#!/usr/bin/python3
import os
import sys

def getFileLength(fname):
    with open(fname,encoding='utf-8') as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def main():
    
    annotation_path = '/Users/PavanLupane/Documents/EclipseWorkspace/pythonWork/anaphora-resolution-work/evaluate-data/annotated-data' 
    crf_anaphoraDict = dict()
    anno_anaphoraDict = dict()
    
    totalCnt = 0
    truePositives = 0
    trueNegatives = 0
    falsePositives = 0
    falseNegatives = 0
    
    for root, dirs, files in os.walk(sys.argv[1],topdown=True):
        for name in files:
            path = os.path.join(root, name)
            if '.txt' in name:      #Evaluate only .txt files
                
                path1 = annotation_path+'/'+name[:-4]+'_ant.txt'        #setup the path for annotated data
                
                if getFileLength(path) == getFileLength(path1):     #check if both files have same number of lines
                
                    with open(path, 'r', encoding='utf-8') as f_crf, open(path1, 'r', encoding='utf-8') as f_anno: 
                        for crf_line, annotation_line in zip(f_crf, f_anno):
#                             print(crf_line)
#                             print(annotation_line)
                            
                            crf_line_tokens = crf_line.rstrip('\n').split('\t')
                            annotation_line_tokens = annotation_line.rstrip('\n').split('\t')
                            
                            print(crf_line_tokens)
                            print(annotation_line_tokens)
                            #Calculations of Positives
                            
                            if(annotation_line_tokens[7] == 'True'):
                                #first add the anaphora to the anno_anaphoraDict
                                if annotation_line_tokens[0] in anno_anaphoraDict:
                                    anno_anaphoraDict[annotation_line_tokens[0]] += 1
                                else:
                                    anno_anaphoraDict[annotation_line_tokens[0]] = 1
                                
                                #update total correct anaphoras in annotated corpus
                                totalCnt += 1
                                
                            #Calculate True Positives - check if anno and crf anaphora are both true 
                            if annotation_line_tokens[7] == 'True' and crf_line_tokens[7] == 'True':
                                truePositives += 1
                                if crf_line_tokens[0] in crf_anaphoraDict: 
                                    crf_anaphoraDict[crf_line_tokens[0]] += 1
                                else:
                                    crf_anaphoraDict[crf_line_tokens[0]] = 1
                                      
                            #Calculate True Negatives 
                            elif annotation_line_tokens[7] == 'False' and crf_line_tokens[7] == 'False':
                                trueNegatives += 1
                            
                            #Calculate False Positives
                            elif annotation_line_tokens[7] == 'False' and crf_line_tokens[7] == 'True':
                                falsePositives += 1
                            
                            #Calculate False Negatives
                            elif  annotation_line_tokens[7] == 'True' and crf_line_tokens[7] == 'False':
                                falseNegatives += 1
                                
                                
                else:
                    print("Files are of different length. Some data missed while processing file ",name)
    
    print("Total Annotated Anaphoras :: ", totalCnt)
    
    print(anno_anaphoraDict)
    print(crf_anaphoraDict)
                              
    
    precision = truePositives / (truePositives + falsePositives)
    
    recall =  truePositives / (truePositives + falseNegatives)
    
    accuracy = (trueNegatives + truePositives) / (trueNegatives + falsePositives)
                
    # Source :: http://www.kdnuggets.com/faq/precision-recall.html
    
    print("Precision is :: ",precision)
    print("Recall is :: ",recall)
    print("Accuracy is ::",accuracy)

if __name__ == "__main__":main()