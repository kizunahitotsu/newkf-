output=open('output.txt',mode='r',encoding='UTF-8')
output_lines=output.readlines()
output.close()

for line in output_lines:
    if(line=='Attribute Result:\n'):
        start_line_result=output_lines.index(line)+1
    if(line.startswith('Average Win Rate : ')==True):
        end_line_WinRate=output_lines.index(line)+1
        break

#记录算点和胜率结果
to_write=output_lines[start_line_result:end_line_WinRate+1]
record=open('记录.txt',mode='a+',encoding='UTF=8')
record.writelines(to_write)
record.close()

newkf=open('newkf.in',mode='r',encoding='UTF-8')
newkf_lines=newkf.readlines()
newkf.close()

#按照LIN,MO,AI,MENG,WEI,YI,LIN的顺序换卡
names=['LIN','MO','AI','MENG','WEI','YI','LIN']
name=newkf_lines[2].split()[0]
temp=newkf_lines[2].lstrip(name)
new_name=names[names.index(name)+1]
newkf_lines[2]=new_name+temp

newkf=open('newkf.in',mode='w+',encoding='UTF-8')
newkf.writelines(newkf_lines)
newkf.close()
