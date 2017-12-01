#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-15 16:14:08
# @Author  : Xiang mingzhe

import subprocess
import os
import re

'''
ssh-add能将指定ssh-key加入ssh-agent server中 以保证在此次终端session下不用每次都输入密码

因ssh-add只是当前终端的session有效 即每次启动终端都要重新ssh-add一次
自己写了个简单的脚本(不具通用性)在终端启动时候自动执行ssh-add
感觉并没有什么卵用 只是少了每次start-ssh-agent和ssh-add两步

ssh-add原理参考:http://blog.csdn.net/fivedoumi/article/details/7515472
'''


def sshAdd():
    # 获取ssh-agnt bash命令
    # 此处并没有真正执行ssh-agent命令 只是将bash命令输出到了stdout：
    '''
    SSH_AUTH_SOCK=/tmp/ssh-Mjrhri9Z80jj/agent.9252; export SSH_AUTH_SOCK;
    SSH_AGENT_PID=6052; export SSH_AGENT_PID;
    echo Agent pid 6052;
    '''
    process = subprocess.run(
        'ssh-agent', stdout=subprocess.PIPE, encoding='utf-8')

    # 从stdout获取SSH_AUTH_SOCK SSH_AGENT_PID
    pattern = re.compile(
        'SSH_AUTH_SOCK=([^;]+).*SSH_AGENT_PID=(\d+).*', re.DOTALL)
    match = pattern.search(process.stdout)

    # 设置对应的系统环境(真正的启动了ssh-agent)
    os.environ['SSH_AUTH_SOCK'] = match.group(1)
    os.environ['SSH_AGENT_PID'] = match.group(2)

    # 执行ssh-add
    subprocess.run(r'ssh-add -k [rsa path]')


if __name__ == '__main__':
    sshAdd()
