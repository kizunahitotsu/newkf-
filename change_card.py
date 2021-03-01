import os

newkf=open('newkf.in',mode='r',encoding='UTF-8')
lines=newkf.readlines()
newkf.close()

'''
for line in lines:
    print(line,end='')
'''

change=''
if(lines[2]=='LIN 400 4 8\n'):
    change='MO 400 4 8\n'
if(lines[2]=='MO 400 4 8\n'):
    change='AI 400 4 8\n'
if(lines[2]=='AI 400 4 8\n'):
    change='MENG 400 4 8\n'
if(lines[2]=='MENG 400 4 8\n'):
    change='WEI 400 4 8\n'
if(lines[2]=='WEI 400 4 8\n'):
    change='LIN 400 4 8\n'
lines[2]=change

'''
for line in lines:
    print(line,end='')
'''

newkf=open('newkf.in',mode='w+',encoding='UTF-8')
newkf.writelines(lines)
newkf.close()
