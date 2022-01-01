import re, pyperclip, pprint
from operator import  itemgetter, attrgetter

path = 'C:\\Users\\user\\pythonTINGS\\dataTOPLAYWITH\\WhatsApp Chat - WHO IS BOOMER BANDICOOT\\_chat.txt'
chat_file = open(path, encoding="utf8")
chat = chat_file.read()
scriptchat = chat.lower()

dictA = {}
dictT = {}
totalA = 0
totalG = 0
combinedDict = {}
finalDict = {}

def wordSort(script):
    count = {}

    pattern = '[a-z]{4,}'
    wordregex = re.compile(pattern)
    wordList = wordregex.findall(script)

    for i in wordList:
        count.setdefault(i,0)
        if i in count.keys():
            count[i] += 1

    return count

print('whose unique words do u want to find?')
name = input()

nameBoy = {'somesh':'Somesh Sahu','adit':'Adit','rhythm':'Rhythm','advait':'Adu','devan':'Devan','ayushman':'Ayushman','shubu':'shubu old:|\d{1,2}\/\d{1,2}\/\d{2},\s\S{7,8}\s\D{2}] Shubu','akash':'Akash:|\d{1,2}\/\d{1,2}\/\d{2},\s\S{7,8}\s\D{2}] ‪\W65 9752 5474‬'}

generalTextPattern = '\d{1,2}\/\d{1,2}\/\d{2},\s\S{7,8}\s\D{2}] '
totalTextCounter = re.compile(generalTextPattern)

boyName = nameBoy[name]
NameTextPattern = '] ' + boyName + ': ([a-z0-9_. ]+)'
indivTextRegex = re.compile(NameTextPattern, re.IGNORECASE)
indivTextlist = indivTextRegex.findall(scriptchat)

inputWordList = ' '.join(indivTextlist)

dictA = wordSort(inputWordList)
dictT = wordSort(scriptchat)

totalA = len(indivTextRegex.findall(scriptchat))
totalG = len(totalTextCounter.findall(scriptchat))

print(totalA)
print(totalG)

dictA = {value:key for key, value in dictA.items()}
dictAprime = dictA

for i in list(dictAprime):
    if i < 100:
        dictA.pop(i)

dictA = {value:key for key, value in dictA.items()}

for keys in dictA:
    combinedDict.setdefault(keys,[dictA[keys],dictT[keys]])

#print(combinedDict)

for word in combinedDict:
    eqnOutput = ((combinedDict[word][0])/(combinedDict[word][1])*(totalG/totalA))
    finalDict.setdefault(word, eqnOutput)

#print(finalDict)

resultsTuple = list(finalDict.items())
sortedTuple = sorted(resultsTuple, key=itemgetter(1), reverse = True)

truncatedTuple = sortedTuple[:10]

#pprint.pprint(truncatedTuple)

for i in range(len(truncatedTuple)):
    print(truncatedTuple[i][0] + '(' + str(float("{:.2f}".format(truncatedTuple[i][1]))) + ')' + ' = ' + str(dictA[truncatedTuple[i][0]]))
