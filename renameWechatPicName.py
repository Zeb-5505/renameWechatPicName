# -*- coding: utf-8 -*-
import os
import time

'''
@File ：renameWechatPicName.py
@Author ：Zeb5505
@Date ：2022/06/25 09:14 
@Describe：批量把手机微信的图片名（时间戳）转换为正常时间格式（保存时间）
'''

while(1):
    path = input('请输入文件夹路径：')
    # 获取该目录下所有文件，存入列表中
    fileList = os.listdir(path)
    i = 0

    for inner_file in fileList:
        # 获取旧文件名（就是路径+文件名）
        old_name = path + os.sep + inner_file  # os.sep添加系统分隔符
        if os.path.isdir(old_name):  # 如果是目录则跳过
            continue


        if len(inner_file) > 20:

            if inner_file[0:8] == "mmexport" and inner_file[8] == "1":
                surfix = inner_file[-4:]
                timeStamp = inner_file[8:-7]
                timeArray = time.localtime(int(timeStamp))
                timeStr = time.strftime("%Y%m%d-%H%M%S", timeArray)

                # 设置新文件名
                new_name = path + os.sep + "mmexport" + timeStr + surfix
                os.rename(old_name, new_name)  # 用os模块中的rename方法对文件改名
                i+=1

    print("共修改了%d项文件名" %(i))
    flag = input("是否再次重命名？(Y/N)")
    if(flag != "Y" or flag != "y"):
        break