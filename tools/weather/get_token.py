#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# file: get_token.py

import os

from tools.error import TokenNotFoundError


def get_token(t_or_p: str) -> str:
    """
    Get the token of Caiyun Weather API, which can be the path of a file or the token itself.
    If the token is not found, it will cause TokenNotFoundError
    """
    try:
        if os.path.isfile(t_or_p):
            with open(t_or_p, "r", encoding="utf-8") as f:
                return f.read().strip()
        else:
            return t_or_p.strip()
    except Exception as e:
        raise TokenNotFoundError(f"无法读取token, Err: {e}")
