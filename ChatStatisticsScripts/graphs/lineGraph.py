import re, pyperclip, pprint
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter

def chatdateSort(script):
    count = {}
#regex searches for months with given parameters
    year = 17
    while year <= 20:
        dateFormat = '/(\d{1,2}/' + str(year) + '),'
        iosdateregex = re.compile(dateFormat)
        dateList = iosdateregex.findall(script)

    #for loop sorts and counts months
        for i in dateList:
            count.setdefault(i,0)
            if i in count.keys():
                count[i] += 1
        year += 1
    return count

path = 'C:\\Users\\user\\Downloads\\Telegram Desktop\\WhatsApp Chat - Hey panini bbq when pinis\\_chat.txt'
chat_file = open(path, encoding="utf8")
chat = chat_file.read()

finalDataDict = {}
finalDataDict = chatdateSort(chat)

#print(finalDataDict)

for i in finalDataDict.keys():
    print(i + " : " + str(finalDataDict[i]))

plt.plot(list(finalDataDict.keys()),list(finalDataDict.values()))
plt.ylabel('number of messages')
plt.xlabel('months')
plt.show()
