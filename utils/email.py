#!/usr/bin/env python3

"""
发送邮件
"""

from . import info
from typing import Optional
import base64

class SenderCOnfig(object):
    """
    发件人设置
    """

    def __init__(self,
         sender_email: str,
         pwd: str,
         host: str,
         port: int,
         sender_name: Optional[str] = None):
        """
        初始化一个发件人默认配置
        """
        self.senderi_email = sender_email
        self.sender_name = sender_name or sender_email
        # 使用 base64 编码
        self.sender_name_base64 = base64.b64encode(self.sender_name.encode("utf-8")).decode("utf-8")
        


def send_email():
    """
    快速发送邮件
    """
    pass

