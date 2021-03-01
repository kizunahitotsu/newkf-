import os

record=open('记录.txt',mode='a+',encoding='UTF=8')
output=open('output.txt',mode='r',encoding='UTF-8')

lines=output.readlines()
index=0
while(index<=len(lines)):
    line=lines[index]
    #print(line,end='')
    index+=1
    if(line=='Attribute Result:\n'):
        break

to_write=lines[index:index+8]

while(index<=len(lines)):
    line=lines[index]
    #print(line,end='')
    if(line.find('Average Win Rate : ')>=0):
        break
    index+=1

to_write.append('//'+lines[index])
to_write.append('\n')
record.writelines(to_write)

record.close()
output.close()
