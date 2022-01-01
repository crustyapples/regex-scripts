import re, pyperclip, pprint

finalDictData = {}
print('Enter the file path of your exported chat text file')
path = input()
print('Are you on Android or iOS?')
platformSpec = input().lower()
chat_file = open(path, encoding="utf8")
print('Enter Start date')
StartDate = input()
print('Enter End date')
EndDate = input()

def chatnameSort(script, platform):
    count = {}
#regex searches for usernames with given parameters
    if platform == 'android':
        andwordregex = re.compile('M\s-\s\w*\s*\w*\s*\w+:')
        nameList = andwordregex.findall(script)

    elif platform == 'ios':
        ioswordregex = re.compile('M] (\w*\s*\w+):')
        nameList = ioswordregex.findall(script)

    phonenumregex = re.compile('M*]*\s*(\W\d+\xa0\d+\xa0\d+):*')   
    numList = phonenumregex.findall(script)

#for loop sorts and counts names
    for i in nameList:
        count.setdefault(i,0)
        if i in count.keys():
            count[i] += 1

    for j in numList:
        count.setdefault(j,0)
        if j in count.keys():
            count[j] += 1
    return count

try:
    chat = chat_file.read()   
    Num1 = chat.index(StartDate)
    Num2 = chat.index(EndDate)
    chatslice = chat[Num1:Num2]
except:
    raise Exception('Invalid date,Either no messages were sent on those days :(, or the date is invlaid, please key in in the form dd/mm/yy, you can also key in Specific strings including timings and colon')

finalDictData = chatnameSort(chatslice, platformSpec)
pprint.pprint(finalDictData)

totalMessages = sum(finalDictData.values())
print ('Total texts = ' + str(totalMessages))





