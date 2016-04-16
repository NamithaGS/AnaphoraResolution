#! /usr/bin/env python2.7
# -*- coding: utf8 -*-
import sys
import codecs, os,io
suffixes = {
    1: ["ो", "े", "ू", "ु", "ी", "ि", "ा"],
    2: ["कर", "ाओ", "िए", "ाई", "ाए", "ने", "नी", "ना", "ते", "ीं", "ती", "ता", "ाँ", "ां", "ों", "ें"],
    3: ["ाकर", "ाइए", "ाईं", "ाया", "ेगी", "ेगा", "ोगी", "ोगे", "ाने", "ाना", "ाते", "ाती", "ाता", "तीं", "ाओं", "ाएं", "ुओं", "ुएं", "ुआं"],
    4: ["ाएगी", "ाएगा", "ाओगी", "ाओगे", "एंगी", "ेंगी", "एंगे", "ेंगे", "ूंगी", "ूंगा", "ातीं", "नाओं", "नाएं", "ताओं", "ताएं", "ियाँ", "ियों", "ियां"],
    5: ["ाएंगी", "ाएंगे", "ाऊंगी", "ाऊंगा", "ाइयाँ", "ाइयों", "ाइयां"],
}


        
def hi_stem(word):
    for L in 5, 4, 3, 2, 1:
        if len(word) > L + 1:
            for suf in suffixes[L]:
                if word.endswith(suf):
                    return word[:-L]
    return word

if __name__ == '__main__':
    file = os.getcwd() + '/annaphoralist_dev.txt'
    opfile = open(os.getcwd() + '/annaphoralist_stemmed_dev.txt',"wb")
    annaphoralist=[]
    with open(file,'r',encoding='utf-8') as f:
        for eachline in f:
            annaphoralist.append(hi_stem(eachline.strip()))
        annaphoradeduplicated = list(set(annaphoralist))
        for eachitem in annaphoralist:
            opfile.write(eachitem.encode('utf-8'))
            opfile.write('\n'.encode('utf-8'))
            
        
