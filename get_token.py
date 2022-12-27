#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: get_token.py

import sys
from error import TokenNotFoundError


def get_token() -> str:
    '''
    获取API的token，首先从命令行获取，
    如果命令行没提供，则在当前目录寻找本地文件

    如果找不到token，则会引起 TokenNotFoundError
    '''
    token = None

    try:
        token = sys.argv[1]
    except:
        try:
            with open('token.txt', 'r', encoding='utf-8') as f:
                token = f.read().strip()
        except Exception as e:
            raise TokenNotFoundError(e.__str__())

    return token
