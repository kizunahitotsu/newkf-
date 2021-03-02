import os

settings=open('settings.txt',mode='r',encoding='UTF-8')
settings_lines=settings.readlines()
settings.close()

#若开启了recording，且记录.txt不为空，则将其保存至/记录 下
if(settings_lines[10].rstrip()=='recording=ON'):
    record=open('记录.txt',mode='r',encoding='UTF-8')
    record_lines=record.readlines()
    record.close()
    if(len(record_lines)>0):
        record_pool=open('记录结果和PC池子.txt',mode='r',encoding='UTF=8')
        record_pool_lines=record_pool.readlines()
        record_pool.close()
        turn=int(record_pool_lines[0].lstrip('turn=').rstrip())

        path=os.getcwd()
        os.rename(path+'/记录.txt',path+'/记录/记录_turn'+str(turn)+'.txt')

record=open('记录.txt',mode='w+',encoding='UTF-8')
record.close()
