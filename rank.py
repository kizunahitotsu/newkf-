import os

record=open('记录.txt',mode='r',encoding='UTF-8')
record_lines=record.readlines()
record.close()

rates=[]
for line in record_lines:
    if(line.startswith('//Average Win Rate : ')==True):
        rate=round(float(line.lstrip('//Average Win Rate : ').rstrip('%\n')),5)
        rates.append(rate)
index=rates.index(max(rates))
#print(rates,rank_rates,index)

PCs=[]
for i in range(5):
    PC=''
    for j in range(8):
        PC+=record_lines[10*i+j]
    PC+='\n'
    PCs.append(PC)
#print(PCs[index])

newkf=open('newkf.in',mode='r',encoding='UTF-8')
newkf_lines=newkf.readlines()
newkf.close()

for i in range(2,11):
    newkf_lines[i]=''
newkf_lines.insert(2,PCs[index])

for line in newkf_lines:
    if(line.startswith('TESTS ')):
        newkf_lines[newkf_lines.index(line)]='TESTS 10000\n'

newkf=open('newkf.in',mode='w+',encoding='UTF-8')
newkf.writelines(newkf_lines)
newkf.close()
