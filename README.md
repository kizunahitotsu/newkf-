# newkf-
1.确保已安装Python，并且.py文件默认用Python启动
2.将所有文件放入与计算器相同目录中，其中覆盖newkf.in
3.正确填写settings.txt，由于还没写检验出错相关的部分，因此请按照格式填写，同样地，手动修改newkf.in时也要按照已有的示例格式，特别是空行数（starting.py会按照settings.txt里必要的信息设置newkf.in，应该是不需要手动改的）
其中：
guanghuan为光环值
level为等级 技能位 品质
WISH为许愿池的7项数值
level_GEAR为装备的等级 四项百分比 有无神秘，这个是统一填入的，如果要分别设定装备，可以把starting.py里GEAR的部分注释掉，这样starting.py就不会修改newkf.in的装备信息，但注意settings.txt里这行一定要保留
THREADS为线程数
TESTS为重复测试次数，测试程序时建议填10等较小的值
SEEDMAX为初始点数候选最大值，测试程序时建议填100w等较小的值
DEFENDER为攻防模式
VERBOSE为是否即时显示计算信息，该信息会写入output.txt，测试程序时可以开着，用VSCode等来查看txt变化，挂机迭代的时候可以关掉，这样不会一直写入output.txt
pool_size为池子内PC数，若当前PC数不满pool_size则将新的PC加入池子，若当前PC数超过pool_size则保留胜率最高的pool_size个
recording为是否将迭代过程的计算结果记录下来，若开启，请确保同目录下有 记录 文件夹！
4.确保newkf.in的PC池子内有东西，若没有可以随便丢一个没加点的PC进去（为避免可能的BUG，请随便加上个别名），注意PC到第一个PC、最后一个PC到ENDPC都有空行
5.同样地，注意GEAR到第一件装备、最后一件装备到ENDGEAR都有空行
6.编辑迭代.bat，在set a=1这一行中，设置迭代次数，测试程序时建议填1
7.运行迭代.bat，注意不要单独运行其他.py文件，重申一遍没有写检验出错相关的部分
8.要是真的出错了，在群里反馈一下BUG