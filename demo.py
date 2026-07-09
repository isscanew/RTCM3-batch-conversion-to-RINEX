import os
import subprocess
import time

#转换函数
def convbin_good(file_name:str,out:list):
    
    arg_format = '-r rtcm3'#rtcm3文件
    arg_out_path = '-d ' + "x:/xxx/xxx/2021/"+str(out[0])+"/"+str(out[1])+"/"+str(out[2])+"/"#输出路径，这里根据年月日时存放结果文件
    arg_file = file_name#输入文件，rtcm3
    print(arg_file)
    convbin_command = ''
    output = 0
    arg_app = 'convbin.exe'#转换工具,注意，将转换工具放在数据文件夹下
    convbin_command = ' '.join([arg_app, arg_format, "-v 3.02", arg_file, arg_out_path])#生成命令
    output = subprocess.call(convbin_command, shell=True)#将命令传给convbin.exe
    #print(arg_out_path)
    time.sleep(5)#给程序一个运行的时间
path = "x:/xx/xx/data/"#数据路径
for i in os.listdir(path):
    #month,day,hour 为月日时，后续根据这些存放结果文件到指定路径
    month = i[11:13]
    day = i[13:15]
    hour = i[15:17]
    convbin_good(i,[month,day,hour])