import re
from operator import itemgetter
import pyperclip, pprint

def wordSort(script, wordlength, listLength):
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
    for i in range(int(listLength)):
        truncatedList.append(sortedTupleList[i])
    for i in range(len(truncatedList)):
        print(str(truncatedList[i][0]) + ' = ' + str(truncatedList[i][1]))
