#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# file: __init__.py

'''
天气相关
'''

__all__ = [
    'get_weather_str','get_token'
]

from .get_weather import get_weather_str
from .get_token import get_token
