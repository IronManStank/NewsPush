#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: __init__.py

__all__=[error, emailpush, newsservice, weather]
from .emailpush import get_email_info, send_email
from .error import *
from .newsservice import GetNews
