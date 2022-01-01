import re, pyperclip, pprint

def chatdateSort(script):
    count = {}
#regex searches for months with given parameters
    iosdateregex = re.compile(r'/\d{1,2}/\d\d,\s')
    dateList = iosdateregex.findall(script)

#for loop sorts and counts months
    for i in dateList:
        count.setdefault(i,0)
        if i in count.keys():
            count[i] += 1
    return count
    
path = 'C:/Users/user/Desktop/pythonTINGS/dataTOPLAYWITH/WhatsApp Chat - WHO IS BOOMER BANDICOOT/_chat.txt'
chat_file = open(path, encoding="utf8")
chat = chat_file.read()

pprint.pprint(chatdateSort(chat))

