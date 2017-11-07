#!/usr/bin/env python
# -*- coding: utf-8 -*-


from urllib.request import urlretrieve
import os

'''
文件下载
起因:本机只安装了Python2但需要下载python3。当时网络环境太差.网页下载太慢且容易崩溃。
考虑使用urllib下载。
原先采用python2 后改成python3版本
'''


def download(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('>>>>>>> %.2f %%<<<<<<<' % per)


if __name__ == '__main__':
    url = 'https://www.python.org/ftp/python/3.6.3/python-3.6.3.exe'
    fileName = os.path.join('D://', 'python-3.6.3.exe')
    urlretrieve(url, fileName, download)
