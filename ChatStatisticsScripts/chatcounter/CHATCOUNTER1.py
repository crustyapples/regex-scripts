import re
import pyperclip
import pprint

def instanceCounter(script):
#to count the number of times a word occurs in a given script, list or string
    count = {}
    for i in script:
        if i != ' ':
            count.setdefault(i,0)
            
        if i in count.keys():
            count[i] += 1

    instanceNumber = count[i]
    return instanceNumber

cricbois = pyperclip.paste()

aduRegex = re.compile(r'] Adu:')
ayuRegex = re.compile(r'] Ayushman:')
devaRegex = re.compile(r'] Devan:')
akasRegex = re.compile(r'] Akash:|9752 5474:')
subuRegex = re.compile(r'] Shubu:|] shubu old')
rhythmRegex = re.compile(r'] Rhythm:')
somesRegex = re.compile(r'] Somesh Sahu:')
adidRegex = re.compile(r'] Adit:')

regexnameDict = {'advait':aduRegex,'ayushman':ayuRegex,'devanshu':devaRegex,'akash':akasRegex,'shubu':subuRegex,'rhythm':rhythmRegex,'somesh':somesRegex,'adit':adidRegex}

for i in regexnameDict:
    x = instanceCounter(regexnameDict[i].findall(cricbois))
    print(i + ' = ' + str(x))


