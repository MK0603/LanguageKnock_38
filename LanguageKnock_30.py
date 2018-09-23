#!/usr/bin/python
# coding: UTF-8
import os

def makeMecabPattern():
    dirPath=os.path.dirname(os.path.abspath(__file__))

    ifile = open(dirPath+'/neko.txt.mecab')

    idata = ifile.readlines()
    ifile.close()
    wordCounter=0
    sentenseCounter=0
    sentenseList=[]
    novelList=[]

    for word in idata:
        # print("word :%s and findEOS boolean :%s"%(word ,word.find("EOS")==-1))
        if word.find("EOF") == -1 and word.find("EOS") == -1:
            wordArray=word.replace('\t',',').split(',')
            wordCounter+=1
            # print(wordCounter)
            # print(wordArray)
            wordDict={}
            wordDict.setdefault("surface",wordArray[0])
            wordDict.setdefault("base",wordArray[7])
            wordDict.setdefault("pos",wordArray[1])
            wordDict.setdefault("pos1",wordArray[2])
            sentenseList.append(wordDict)
            
            if wordArray[0]=='。' or wordArray[0]=='」':
                novelList.append(sentenseList)
                # sentenseList.clear()
                sentenseList=[]
                sentenseCounter+=1

#     print(novelList)
    return novelList
