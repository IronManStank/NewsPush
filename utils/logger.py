#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: logger.py
# 说明:
# 时间: 2022/02/02 15:49:18
# 版本: 1.0

__all__ = ['logger']

import logging
from logging.handlers import RotatingFileHandler
from os.path import isdir  # , exists
from os import mkdir

# 我的简单logger

__log_path = './log/applog.log'
if not isdir('./log'):
    mkdir('./log')

MB = 1048576

# 记录器
logger = logging.getLogger('applog')
logger.setLevel(logging.DEBUG)

# 处理器
# 控制台
__conhandler = logging.StreamHandler()
__conhandler.setLevel(logging.DEBUG)
# 文件
__filehandler = RotatingFileHandler(
    filename=__log_path, backupCount=10, encoding='utf-8', mode='a+', maxBytes=0.1*MB)
__filehandler.setLevel(logging.INFO)

# 格式化器
# 终端输出
__con_ft = logging.Formatter(
    fmt=r'%(asctime)s|%(levelname)-8s|%(filename)s:[%(lineno)3s]| %(message)s', datefmt=r'%H:%M:%S')
# 文件输出
__file_ft = logging.Formatter(
    fmt=r'%(asctime)s|%(levelname)-8s|%(filename)s:[%(lineno)3s]| %(message)s', datefmt=r'%Y-%m-%d %H:%M:%S')


# 绑定
__conhandler.setFormatter(__con_ft)
__filehandler.setFormatter(__file_ft)

logger.addHandler(__conhandler)
logger.addHandler(__filehandler)


# logger = __logger

