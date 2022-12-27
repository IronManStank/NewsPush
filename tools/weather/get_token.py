#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: get_token.py

import os
from tools.error import TokenNotFoundError


def get_token(t_or_p: str) -> str:
    '''
    获取API的token，可以是一个文件的路径，也可以是token本身

    如果找不到token，则会引起 TokenNotFoundError
    '''
    try:
        if os.path.isfile(t_or_p):
            with open(t_or_p, 'r', encoding='utf-8') as f:
                return f.read().strip()
        else:
            return t_or_p.strip()
    except Exception as e:
        raise TokenNotFoundError(f'无法读取token, Err: {e}')
