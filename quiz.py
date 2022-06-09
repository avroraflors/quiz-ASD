import re

##1
username = '@fadil12'
username = '@fadil12_'
cocok = re.findall(r'@+[a-z]+[0-9]+\w', username)
if cocok:
    print(cocok, 'pass') 
else:
    print('Fail')

##2
note = open("kuiz.txt", "r" )
teks = note.read()
note.close()
pola = r"\w+@+[\w.-]+"
string = re.findall(pola, teks)
print(string)




