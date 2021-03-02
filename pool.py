import os

settings=open('settings.txt',mode='r',encoding='UTF-8')
settings_lines=settings.readlines()
settings.close()

output=open('output.txt',mode='r',encoding='UTF-8')
output_lines=output.readlines()
output.close()

newkf=open('newkf.in',mode='r',encoding='UTF-8')
newkf_lines=newkf.readlines()
newkf.close()

record_pool=open('记录结果和PC池子.txt',mode='r',encoding='UTF=8')
record_pool_lines=record_pool.readlines()
record_pool.close()

turn=int(record_pool_lines[0].lstrip('turn=').rstrip())+1
pool_size=int(settings_lines[9].lstrip('pool_size=').rstrip())

PCs_name=[]
PCs=[]

for line in output_lines:
    if(line.lstrip().startswith('1:')==True):
        start_line_rank=output_lines.index(line)
        break

#胜率最高的一组的PC名，其中若Myself在内则更名
for i in range(pool_size):
    if(output_lines[start_line_rank+i]=='\n'):
        break
    name_temp=output_lines[start_line_rank+i].split()[-1]
    if(name_temp=='Myself'):
        name_temp=newkf_lines[2].split()[0]+'_turn'+str(turn)
    PCs_name.append(name_temp)

#如果Myself在胜率最高的一组里，则加入PCs
PC_new=newkf_lines[2].split()[0]
if(PC_new+'_turn'+str(turn) in PCs_name):
    temp=newkf_lines[2].lstrip(PC_new)
    PC_new+='_turn'+str(turn)+temp
    for i in range(3,11):
        PC_new+=newkf_lines[i]
    PCs.append(PC_new)

for line in newkf_lines:
    if(line=='PC\n'):
        start_line_PCs=newkf_lines.index(line)+2
    if(line=='ENDPC\n'):
        end_line_PCs=newkf_lines.index(line)
        break

for PC_name in PCs_name:
    for i in range(start_line_PCs,end_line_PCs):
        if(newkf_lines[i].startswith(PC_name)==True):
            PC=''
            for j in range(9):
                PC+=newkf_lines[i+j]
            PCs.append(PC)
            break

PCs_all=''
for PC_temp in PCs:
    PCs_all+=PC_temp

#记录结果和PC池子
record_pool=open('记录结果和PC池子.txt',mode='w+',encoding='UTF=8')
record_pool.write('turn='+str(turn)+'\n\n')
record_pool.write(PCs_all)

index_temp=0
while(output_lines[start_line_rank+index_temp]!='\n'):
    record_pool.write(output_lines[start_line_rank+index_temp])
    index_temp+=1
record_pool.write('\n')
record_pool.close()

#若开启了recording，则将其保存至/记录 下 #不会复制，只能用这种麻烦的方法来写orz
if(settings_lines[10].rstrip()=='recording=ON'):
    record_pool=open('记录结果和PC池子.txt',mode='r',encoding='UTF=8')
    record_pool_lines.clear()
    record_pool_lines=record_pool.readlines()
    record_pool.close()
    path=os.getcwd()
    os.rename(path+'/记录结果和PC池子.txt',path+'/记录/记录结果和PC池子_turn'+str(turn)+'.txt')
    record_pool=open('记录结果和PC池子.txt',mode='w+',encoding='UTF=8')
    record_pool.writelines(record_pool_lines)
    record_pool.close()

#清空output.txt
output=open('output.txt',mode='w+',encoding='UTF-8')
output_lines=output.readlines()
output.close()

#重置newkf.in
newkf=open('newkf.in',mode='w+',encoding='UTF-8')
#重置TESTS
TESTS=settings_lines[5]
for line in newkf_lines:
    if(line.startswith('TESTS ')==True):
        newkf_lines[newkf_lines.index(line)]=TESTS
#重置PC池子
for i in range(start_line_PCs,end_line_PCs):
    newkf_lines[i]=''
newkf_lines.insert(start_line_PCs,PCs_all)
#重置Myself信息
level=settings_lines[1].lstrip('level=')
WISH=settings_lines[2]
for i in range(2,11):
    newkf_lines[i]=''
newkf_lines.insert(2,'LIN '+level+WISH+'1 1 1 1 1 1 \nNONE\nNONE\nNONE\nNONE\n0\n\n')
newkf.writelines(newkf_lines)
newkf.close()
