
def main():
    print("Start")
    filename = 'story.txt'
    rootDir = dict()
    newSentenceDict = dict()
    sentenceCntr = 0
    
    with open(filename,'r',encoding='utf-8') as infile:
        for line in infile:
#             print(line)
            lineTuples = line.split('\t')
            #print(lineTuples)
            
            if lineTuples[0] == '\n':
                rootDir[sentenceCntr] = newSentenceDict
                sentenceCntr += 1
                newSentenceDict = dict() 
                continue
            else:
                wordAttribList = list()
                wordAttribList = lineTuples[3:8]
                
                ####### Morph string manipulation starts here #####
                if len(lineTuples) > 7:
                    morphString = lineTuples[8]
                    morphTupples = morphString.split('|')
                    morphResults = len(morphTupples)
                    if morphResults > 1:
                        str = morphTupples[1].strip()
                        
                        str = str.split("\'",1)[1]
                        str = str[:-2]
                        
                        morphKnowledge = str.split(',')     #this has tupples from first morph output
                        #print(morphKnowledge)
                        
                        wordAttribList.append(morphKnowledge[2])
                        wordAttribList.append(morphKnowledge[3])
                
                ##### End of Morph String #####
                
                newSentenceDict[lineTuples[2]] = wordAttribList # Added word attributes
#                 print(newSentenceDict)
        
        rootDir[sentenceCntr] = newSentenceDict     #once last sentence addition      
    print(rootDir)    
if __name__ == "__main__":main()
##################### Notes ########################
# These are the fields in rootDir #
# [0] -> Word #
# [1] -> POS #
# [2] -> Chunk Tag #
# [3] -> NER #
# [5] -> Gender#
# [6] -> singular/plural #
# Usage: rootDir[sentence number][word number][0-6]#
 