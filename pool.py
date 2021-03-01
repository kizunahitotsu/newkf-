import os

output=open('output.txt',mode='r',encoding='UTF-8')
output_lines=output.readlines()
output.close()

newkf=open('newkf.in',mode='r',encoding='UTF-8')
newkf_lines=newkf.readlines()
newkf.close()

record_pool=open('记录结果和PC池子.txt',mode='r',encoding='UTF=8')
lines=record_pool.readlines()
record_pool.close()

turn=int(lines[0].lstrip('turn=').rstrip())+1
pool_size=int(lines[1].lstrip('pool_size=').rstrip())
#print(turn)
#print(pool_size)

PCs_name=[]
PCs=[]

for line in output_lines:
    if(line.lstrip().startswith('1: ')==True):
        start_line_newPC=output_lines.index(line)
        break
#print(start_line_newPC)
for i in range(pool_size):
    if(output_lines[start_line_newPC+i]=='\n'):
        break
    name_temp=output_lines[start_line_newPC+i].split()[-1]
    if(name_temp=='Myself'):
        name_temp=newkf_lines[2].split()[0]+'_turn'+str(turn)
    PCs_name.append(name_temp)
#print(PCs_name)

PC_new=newkf_lines[2].split()[0]
if(PC_new+'_turn'+str(turn) in PCs_name):
    temp=newkf_lines[2].lstrip(PC_new)
    PC_new+='_turn'+str(turn)+temp
    for i in range(3,11):
        PC_new+=newkf_lines[i]
    #print(PC_new)
    PCs.append(PC_new)

for line in newkf_lines:
    if(line=='PC\n'):
        start_line=newkf_lines.index(line)+2
    if(line=='ENDPC\n'):
        end_line=newkf_lines.index(line)
        break
#print(start_line)

for PC_name in PCs_name:
    for i in range(start_line,end_line):
        if(newkf_lines[i].startswith(PC_name)==True):
            PC=''
            for j in range(9):
                PC+=newkf_lines[i+j]
            PCs.append(PC)
            break
#print(PCs)
PCs_all=''
for PC_temp in PCs:
    PCs_all+=PC_temp
#print(PCs_all)

record_pool=open('记录结果和PC池子.txt',mode='w+',encoding='UTF=8')
record_pool.write('turn='+str(turn)+'\n')
record_pool.write('pool_size='+str(pool_size)+'\n\n')
record_pool.write(PCs_all)
record_pool.close()

newkf=open('newkf.in',mode='w+',encoding='UTF-8')
for line in newkf_lines:
    if(line.startswith('TESTS ')==True):
        newkf_lines[newkf_lines.index(line)]='TESTS 10\n'
for i in range(start_line,end_line):
    newkf_lines[i]=''
newkf_lines.insert(start_line,PCs_all)
for i in range(2,11):
    newkf_lines[i]=''
newkf_lines.insert(2,'LIN 400 4 8\nWISH 2 2 2 2 2 0 0\n1 1 1 1 1 1 \nNONE\nNONE\nNONE\nNONE\n0\n\n')
newkf.writelines(newkf_lines)
newkf.close()
