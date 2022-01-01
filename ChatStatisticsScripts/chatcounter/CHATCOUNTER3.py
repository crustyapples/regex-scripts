import re, pyperclip, pprint

finaldataDict = {}
path = 'C:/Users/user/Desktop/pythonTINGS/dataTOPLAYWITH/WhatsApp Chat - WHO IS BOOMER BANDICOOT/_chat.txt'
chat_file = open(path, encoding="utf8")

#to cut a slice of the chat data within a time period
print('Enter Start date')
StartDate = input()
print('Enter End date')
EndDate = input()

try:
    chat = chat_file.read()   
    Num1 = chat.index(StartDate)
    Num2 = chat.index(EndDate)
    chatslice = chat[Num1:Num2]
except:
    raise Exception('Invalid date,Either no messages were sent on those days :(, or the date is invlaid, please key in in the form dd/mm/yy, you can also key in Specific strings including timings and colon')

aduRegex = re.compile(r'] Adu:')
ayuRegex = re.compile(r'] Ayushman:')
devaRegex = re.compile(r'] Devan:')
akasRegex = re.compile(r'] Akash:|\xa09752\xa0')
subuRegex = re.compile(r'] Shubu:|] shubu old')
rhythmRegex = re.compile(r'] Rhythm:')
somesRegex = re.compile(r'] Somesh Sahu:')
adidRegex = re.compile(r'] Adit:')

regexnameDict = {'advait':aduRegex,'ayushman':ayuRegex,'devanshu':devaRegex,'akash':akasRegex,'shubu':subuRegex,'rhythm':rhythmRegex,'somesh':somesRegex,'adit':adidRegex}

def instanceCounter2(script):
#to count the number of times the search query appeared in regex obj
    count = len(script)
    return count

#loops through names corresponding to respective regex objects to search for the specified username
for i in regexnameDict:
    freq = instanceCounter2(regexnameDict[i].findall(chatslice))
#enters the name using setdefault method (adds key to dict if it doesnt exist in the dict)
    finaldataDict.setdefault(i,freq)
    print(i + ' sent ' + str(freq) + ' messages.')
    
totalMessages = sum(finaldataDict.values())
print('Total messages = ' + str(totalMessages))


