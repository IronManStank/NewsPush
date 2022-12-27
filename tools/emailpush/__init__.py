#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: __init__.py

__all__ = [
    'get_email_info',
    'send_email'
]

from .emailserver import get_email_info, send_email
