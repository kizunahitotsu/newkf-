record=open('记录.txt',mode='r',encoding='UTF-8')
record_lines=record.readlines()
record.close()

#胜率最高的PC的序号
rates=[]
for line in record_lines:
    if(line.startswith('Average Win Rate : ')==True):
        rate=round(float(line.lstrip('Average Win Rate : ').rstrip('%\n')),5)
        rates.append(rate)
index=rates.index(max(rates))

'''
#提取所有的PC
PCs=[]
line_index=0
while(line_index<len(record_lines)):
    if(record_lines[line_index].startswith('WISH ')==True):
        start_line_PC=line_index-1
        PC=''
        for i in range(9):
            PC+=record_lines[start_line_PC+i]
        PCs.append(PC)
    line_index+=1
#胜率最高的PC
#print(PCs[index])
'''
#提取胜率最高的PC
names=['LIN','MO','AI','MENG','WEI','YI']
for line in record_lines:
    if(len(line.split())>0):
        if(line.split()[0]==names[index]):
            start_line_PC=record_lines.index(line)
            PC=''
            for i in range(9):
                PC+=record_lines[start_line_PC+i]
            break

newkf=open('newkf.in',mode='r',encoding='UTF-8')
newkf_lines=newkf.readlines()
newkf.close()

#将配置改为PC
for i in range(2,11):
    newkf_lines[i]=''
newkf_lines.insert(2,PC)

#TESTS改为10000，准备rank
for line in newkf_lines:
    if(line.startswith('TESTS ')):
        newkf_lines[newkf_lines.index(line)]='TESTS 10000\n'
        break

newkf=open('newkf.in',mode='w+',encoding='UTF-8')
newkf.writelines(newkf_lines)
newkf.close()
