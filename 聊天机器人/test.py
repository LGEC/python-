#!/usr/bin/python3
import os,sys

fp = os.open('test.txt',os.O_RDWR)

print('文件内容：',fp)

os.write(fp,str.encode('你好啊！'))

os.close(fp)

print('文件已关闭')