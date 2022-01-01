#! python3
import matplotlib.pyplot as plt
import re
import operator


nameBoy = ['Somesh Sahu','Adit','Rhythm','Adu','Devan','Ayushman','shubu old:|\d{1,2}\/\d{1,2}\/\d{2},\s\S{7,8}\s\D{2}] Shubu','Akash:|\d{1,2}\/\d{1,2}\/\d{2},\s\S{7,8}\s\D{2}] ‪\W65 9752 5474‬']
ALLdata_keys = []
ALLdata_values = []
def chatdateSort(script):
        count = {}
        
        #regex searches for months with given parameters
        year = 17
        while year <= 20:
            dateFormat = '/(\d{1,2}/' + str(year) + '),'
            iosdateregex = re.compile(dateFormat)
            dateList = iosdateregex.findall(Script_s)
        
        #for loop sorts and counts months
            for i in dateList:
                count.setdefault(i,0)
                if i in count.keys():
                    count[i] += 1
            year += 1
        return count
        

for i in nameBoy:
    search_v = '\d{1,2}\/\d{1,2}\/\d{2},\s\S{7,8}\s\D{2}] ' + i + ':'
    DateRegex = re.compile(search_v)
    path = 'C:\\Users\\user\\pythonTINGS\\dataTOPLAYWITH\\WhatsApp Chat - WHO IS BOOMER BANDICOOT\\_chat.txt'
    chat_file = open(path, encoding="utf8")
    text = chat_file.read()
    Script_List = DateRegex.findall(text)
    Script_s = ''.join(Script_List)
    counted = chatdateSort(Script_s)
    ALLdata_keys.append(counted.keys())
    ALLdata_values.append(counted.values())
  

    
values_d = ALLdata_values
keys_d = ALLdata_keys

#Sahu
sahus=list(keys_d[0])
sahus_v=list(values_d[0])
sahus_dict = dict(zip(sahus, sahus_v))
#Adit
adits=list(keys_d[1])
adits_v=list(values_d[1])
adits_dict = dict(zip(adits, adits_v))
#Rhythm
rhythms=list(keys_d[2])
rhythms_v=list(values_d[2])
rhythms_dict = dict(zip(rhythms, rhythms_v))
#Adu
adus=list(keys_d[3])
adus_v=list(values_d[3])
adus_dict = dict(zip(adus, adus_v))
#Devan
devans=list(keys_d[4])
devans_v=list(values_d[4])
devans_dict = dict(zip(devans, devans_v))
#Ayushman
ayushmans=list(keys_d[5])
ayushmans_v=list(values_d[5])
ayushmans_dict = dict(zip(ayushmans, ayushmans_v))
#Shubu
shubus=list(keys_d[6])
shubus_v=list(values_d[6])
shubus_dict = dict(zip(shubus, shubus_v))
#Akash
akashs=list(keys_d[7])
akashs_v=list(values_d[7])
akashs_dict = dict(zip(akashs, akashs_v))


month = sahus
plt.plot(month, sahus_v,color='g',label = 'Somesh')
plt.plot(month, rhythms_v,color='orange',label = 'Rhythm')
plt.plot(month, akashs_v,color='blue',label = 'Akash')
plt.plot(month, shubus_v,color='red',label = 'Shubu')
plt.plot(month, ayushmans_v,color='yellow',label = 'Ayushman')
plt.plot(month, devans_v,color='black',label = 'Devan')
plt.plot(month, adus_v,color='brown',label = 'Adu')
plt.plot(month, adits_v,color='purple',label = 'Adit')
plt.xlabel('Months')
plt.ylabel('Number of messages sent')
plt.title('Cricket group messages')
plt.legend()
plt.show()
