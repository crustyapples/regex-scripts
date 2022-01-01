import re, pyperclip, pprint
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
import wordSortFunc as ws

boyName = ''
boyNamesDict = {'advait':'Adu','ayushman':'Ayushman','devan':'Devan','akash':'Akash:|\W65 9752 5474','shubhangam':'Shubu:|shubu old','rhythm':'Rhythm','somesh':'Somesh Sahu','adit':'Adit'}

path = 'C:\\Users\\user\\pythonTINGS\\dataTOPLAYWITH\\WhatsApp Chat - WHO IS BOOMER BANDICOOT\\_chat.txt'
chat_file = open(path, encoding="utf8")
chat = chat_file.read()
lowerChat = chat.lower()

#to cut a slice of the chat data within a time period
print('Enter Start date')
StartDate = input()
print('Enter End date')
EndDate = input()
print('whose messages do u want to analyse?')
boyChoice = input()

indivTextlist = []

  
Num1 = lowerChat.index(StartDate)
Num2 = lowerChat.index(EndDate)
chatslice = lowerChat[Num1:Num2]

boyName = boyNamesDict[boyChoice]
pattern = '(] ' + boyName + ':) ([a-z0-9_. ]+)'
indivTextRegex = re.compile(pattern, re.IGNORECASE)
indivTextlist = indivTextRegex.findall(chatslice)
wordSortScript = ' '

for i in range(len(indivTextlist)):
    wordSortScript = wordSortScript + indivTextlist[i][1]

print('how long do u want the words to be?')
userinput = input()
print('how many words do u want to search?')
userinput2 = input()
#print(indivTextlist)
#print(wordSortScript)
#pprint.pprint(indivTextlist)

ws.wordSort(wordSortScript, userinput, userinput2)
