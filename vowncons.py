import os
os.chdir(r"C:\Users\Jagadish\Desktop")
f = open("text.txt", "r")
fl = f.read()
cha = vow = cons = 0
for i in fl:
    if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
        vow = vow+1
    elif ord(i)>=66 and ord(i)<=68 or ord(i)>=70 and ord(i)<=72 or ord(i)>=74 and ord(i)<=78 or ord(i)>=80 and ord(i)<=84 or ord(i)>=86 and ord(i)<=90 or ord(i)>=98 and ord(i)<=100 or ord(i)>=102 and ord(i)<=104 or ord(i)>=106 and ord(i)<=110 or ord(i)>=112 and ord(i)<=116 or ord(i)>=118 and ord(i)<=122:
        cons = cons+1
wor = [] 
lin = fl.split('\n')
cha = len(fl)-len(lin)+1
for i in lin:
    k = i.split(' ')
    for j in k:
        wor.append(j)
maxLength = max(len(x) for x in wor) 
print('Characters: ',cha)
print('words: ',len(wor))
print('lines: ',len(lin))
print('Vowels: ',vow)
print('Consonants: ',cons)
print('Largest Word length: ',maxLength)
