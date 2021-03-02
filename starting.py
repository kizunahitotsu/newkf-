settings=open('settings.txt',mode='r',encoding='UTF-8')
settings_lines=settings.readlines()
settings.close()

newkf=open('newkf.in',mode='r',encoding='UTF-8')
newkf_lines=newkf.readlines()
newkf.close()

guanghuan=settings_lines[0].lstrip('guanghuan=')
level=settings_lines[1].lstrip('level=')
WISH=settings_lines[2]
level_GEAR=settings_lines[3].lstrip('level_GEAR=')
THREADS=settings_lines[4]
TESTS=settings_lines[5]
SEEDMAX=settings_lines[6]
DEFENDER=settings_lines[7]
VERBOSE=settings_lines[8]

newkf=open('newkf.in',mode='w+',encoding='UTF-8')
newkf_lines[0]=guanghuan
newkf_lines[2]='LIN '+level
newkf_lines[3]=WISH
newkf_lines[4]='1 1 1 1 1 1\n'
newkf_lines[5]='NONE\n'
newkf_lines[6]='NONE\n'
newkf_lines[7]='NONE\n'
newkf_lines[8]='NONE\n'
newkf_lines[9]='0\n'

for line in newkf_lines:
    if(line=='GEAR\n'):
        start_line_GEAR=newkf_lines.index(line)+2
    if(line=='ENDGEAR\n'):
        end_line_GEAR=newkf_lines.index(line)
        break

for i in range(start_line_GEAR,end_line_GEAR-1):
    temp=newkf_lines[i].split()[0]
    newkf_lines[i]=temp+' '+level_GEAR

newkf_lines[end_line_GEAR+2]=THREADS
newkf_lines[end_line_GEAR+3]=TESTS
newkf_lines[end_line_GEAR+6]=SEEDMAX
newkf_lines[end_line_GEAR+8]=DEFENDER
newkf_lines[end_line_GEAR+9]=VERBOSE
newkf.writelines(newkf_lines)
newkf.close()
