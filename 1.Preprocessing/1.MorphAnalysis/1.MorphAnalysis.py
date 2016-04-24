__author__ = 'namithags'
import codecs
import re, os, sys
import string,math
import numpy as np
import json

import time
import urllib2, urllib

import sys
import requests
import re

reload(sys)
sys.setdefaultencoding('utf8')

#input train data
trainfoldername = 'C:\Users\Namithaa\Desktop\NLP\project\corpus\DATADATADATA\hi_test'

#output morphologically analysed train data
newfoldername = 'C:\Users\Namithaa\Desktop\NLP\project\corpus\DATADATADATA\hi_test_new'

def getdata(page):
    aa = page.split("\n")
    bb =  aa.index('<p><b>Morph Analyzer Output</b></p>')
    returndata = []
    for eachline in aa[bb:]:

        start = '&lt;'
        end = '&gt;'
        r = re.compile('&lt;(.*?)&gt;')
        m = r.search(eachline)
        if m:
            lyrics = "| < "+ m.group(1) +">"
            returndata.append(lyrics)
    return returndata


for path1,dir,files in os.walk(trainfoldername):
    for files1 in files:
        if files1 in "desktop.ini":
            continue
        else:
            path_to_file = path1+ '/' + files1
            new_file = newfoldername + '/' + files1
            new_file_fp = codecs.open(new_file,"wb",encoding="utf-8")
            with codecs.open(path_to_file,"rb",encoding="utf-8") as filepointer:
                sentence = []
                for eachline in filepointer.readlines():
                    if not eachline.startswith('#begin document' ) and not eachline.startswith('#end document') and not (eachline == "\n"):
                       word = (eachline.split("\t")[3])
                       print unicode.encode(word , "utf-8")
                       #print unicode.encode(" ".join(sentence),'utf-8')

                       morpheddata = unicode.encode(word,'utf-8')
                       #mydata={'batch_query':morpheddata}    #The first is the var name the second is the value
                       mydata={'yourtext':morpheddata , 'outtype': 'utf', 'submit':"Submit"}    #The first is the var name the second is the value

                       mydata=urllib.urlencode(mydata)
                       #path='http://www.cfilt.iitb.ac.in/~ankitb/ma/batch_submit.php'    #the url you want to POST to
                       path='http://sampark.iiit.ac.in/hindimorph/web/restapi.php/indic/morphclient'
                       req=urllib2.Request(path, mydata)
                       req.add_header("Content-type", "application/x-www-form-urlencoded")
                       page=urllib2.urlopen(req).read()

					   # request to the sampark tool for morphological data for the word
                       page1 = requests.post(path,   params=mydata)

                       printtext = getdata(page1.text)
                       #outputfile = "http://www.cfilt.iitb.ac.in/~ankitb/ma/output.txt"
                       #data = urllib2.urlopen(outputfile)

                       #start = False
                       #outputno = 0
                       #allinfo = []
                       # for line in data: # files are iterable
                       #     #print line
                       #     if line.startswith("NOT IN LEXICON"):
                       #         continue
                       #     if line.startswith("Token : "):
                       #         outputno = (int(line.split(":")[-1].strip("\n")) * 2 ) + 1
                       #         if outputno!=0:
                       #             start = True
                       #     if start == True and outputno!=0:
                       #         outputno -=1
                       #         allinfo.append(line)
                       #         allinfo.append(" \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t | ")

                       datatoappend = eachline.rstrip('\n') + "\t" + "MorphAnalysis : " + str(" ".join(printtext)).decode() +"\n"
                       #stringto = unicode(datatoappend,'utf-8')
                       new_file_fp.write(datatoappend)
                    else:
                        new_file_fp.write(eachline)


