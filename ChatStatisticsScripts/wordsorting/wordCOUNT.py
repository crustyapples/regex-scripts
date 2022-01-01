import re
import operator

path = 'C:\\Users\\user\\Downloads\\Telegram Desktop\\WhatsApp Chat - Hey panini bbq when pinis\\_chat.txt'
chat_file = open(path, encoding="utf8")
chat = chat_file.read()
scriptchat = chat.lower()
finaldataDict = {}
print("do u want to search for any particular words?")
userinput3 = input().lower()
userinput2 = 1
i = 0
cont = ''
if userinput3 == 'yes':
    print("ok, type one word u want to search")
    userinput = input()

    while (cont != 'no'):
        print("one more?")
        cont = input()
        if cont == 'yes':
            print('enter word')
            userinput = userinput + '|' + input()
            userinput2 += 1
        elif cont == 'no':
            i = 1000
else:
    print(
        'ok, I will find the most common words in this chat, how many letters long do you want your word to be at '
        'minimum?')
    userinput = input()
    print("how long do u want your list to be?")
    userinput2 = input()


def wordSort(script, wordlengthORcustomword):
    count = {}

    if userinput3 == 'yes':
        pattern = wordlengthORcustomword
        wordregex = re.compile(pattern)
        wordList = wordregex.findall(script)
    else:
        pattern = '[a-z]{%s,}' % wordlengthORcustomword
        wordregex = re.compile(pattern)
        wordList = wordregex.findall(script)

    for i in wordList:
        count.setdefault(i, 0)
        if i in count.keys():
            count[i] += 1

    return count


def entries_to_remove(entries, the_dict):
    for key in entries:
        if key in the_dict:
            del the_dict[key]


names = (
    'advait', 'devan', 'somesh', 'rhythm', 'akash', 'ayushman', 'adit', 'omitted', 'pm', 'am', 'image', 'cel', 'ausie',
    'meshies', 'shuboobs', 'dylan', 'jiwoney', 'joanne', 'grisel', 'neha', 'kathleen')

finaldataDict = wordSort(scriptchat, userinput)
entries_to_remove(names, finaldataDict)
dataTupleList = list(finaldataDict.items())
sortedTupleList = sorted(dataTupleList, key=operator.itemgetter(1), reverse=True)
truncatedList = []

for i in range(int(userinput2)):
    truncatedList.append(sortedTupleList[i])

FinalList = truncatedList
# FinalList = sorted(truncatedList, key=itemgetter(0))

for i in range(len(FinalList)):
    print(str(FinalList[i][0]) + ' = ' + str(FinalList[i][1]))
