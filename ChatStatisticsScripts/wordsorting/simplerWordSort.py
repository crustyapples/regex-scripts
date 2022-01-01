import re, pyperclip, pprint
from operator import  itemgetter, attrgetter

path = 'C:/Users/user/Desktop/pythonTINGS/dataTOPLAYWITH/WhatsApp Chat - WHO IS BOOMER BANDICOOT/_chat.txt'
chat_file = open(path, encoding="utf8")
chat = chat_file.read()
scriptchat = chat.lower()
finaldataDict = {}

print("ok, I will find the most common words in this chat, how many letters long do you want your word to be at minimum?")
userinput = input()
print("how long do u want your list to be?")
userinput2 = input()

def wordSort(script, wordlength):
    count = {}

    pattern = '[a-z]{%s,}' % wordlength
    wordregex = re.compile(pattern)
    wordList = wordregex.findall(script)

    for i in wordList:
        count.setdefault(i,0)
        if i in count.keys():
            count[i] += 1

    finaldataDict = count
    dataTupleList = list(finaldataDict.items())
    sortedTupleList = sorted(dataTupleList, key=itemgetter(1), reverse=True)
    truncatedList = []
    for i in range(int(userinput2)):
        truncatedList.append(sortedTupleList[i])
    for i in range(len(truncatedList)):
        print(str(truncatedList[i][0]) + ' = ' + str(truncatedList[i][1]))

def entries_to_remove(entries, the_dict):
    for key in entries:
        if key in the_dict:
            del the_dict[key]

names = ('advait','devan','somesh','rhythm','akash','ayushman','adit','omitted','pm','am','image')

wordSort(scriptchat, userinput)

