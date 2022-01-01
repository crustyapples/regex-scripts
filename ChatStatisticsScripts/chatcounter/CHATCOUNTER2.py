import re
import pyperclip
import pprint

def instanceCounter(script):
#to count the number of times a word occurs in a given script, list or string
    count = {}
    valueList = []
    for i in script:
        if i != ' ':
            count.setdefault(i,0)
        if i in count.keys():
            count[i] += 1
    for j in count:
        valueList.append(count[j])
    if len(valueList) == 2:    
        return(valueList[0] + valueList[1])
    else:
        return(valueList[0])
    
path = 'C:/Users/user/Desktop/pythonTINGS/dataTOPLAYWITH/WhatsApp Chat - WHO IS BOOMER BANDICOOT/_chat.txt'
cricbois_file = open(path, encoding="utf8")
cricbois = cricbois_file.read()

aduRegex = re.compile(r'] Adu:')
ayuRegex = re.compile(r'] Ayushman:')
devaRegex = re.compile(r'] Devan:')
akasRegex = re.compile(r'] Akash:|5474')
subuRegex = re.compile(r'] Shubu:|] shubu old')
rhythmRegex = re.compile(r'] Rhythm:')
somesRegex = re.compile(r'] Somesh Sahu:')
adidRegex = re.compile(r'] Adit:')

regexnameDict = {'advait':aduRegex,'ayushman':ayuRegex,'devanshu':devaRegex,'akash':akasRegex,'shubu':subuRegex,'rhythm':rhythmRegex,'somesh':somesRegex,'adit':adidRegex}

finaldataDict = {}

for i in regexnameDict:
    x = instanceCounter(regexnameDict[i].findall(cricbois))
    finaldataDict.setdefault(i,str(x))
    print(i + ' = ' + str(x))

print(finaldataDict)



