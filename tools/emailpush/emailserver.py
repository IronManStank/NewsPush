import json
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from os.path import isfile
from re import match
# from tools.error import *


def update_value(value_dict: dict, key: str, single: bool = True, default=None) -> None:
    """A function to update a dict value.

    Args:
        value_dict (dict): Information to be updated.
        key (str): Information key.
        single (bool, optional): A udpate switch. Defaults to True.
        default (_type_, optional): Return None when the dict is invalid. Defaults to None.

    Returns:
        info: Return None, or the value of the key.
    """
    try:
        if single:
            return value_dict[key][0]
        else:
            return value_dict[key]
    except:
        return default


def get_cline_info(value_dict: dict)-> dict:
    """Get mail parameters from the command line dictionary.

    Args:
        value_dict (dict): The command line dictionary.

    Returns:
        _type_: Return info dict.
    """    
    template_dict = {
        "header": {"HeaderFrom": "Personal Intelligence System", "HeaderTo": "BOSS"},
        "subject": "Daily Intelligence Report",
        "message": "This is a test email.",
    }
    # Try to get the template, which is the local configuration file.
    # The idea is that local profiles store complete or incomplete mail configurations.
    # update it with the command line argument.
    try:
        if isfile("./email_config.json"):
            with open("./email_config.json", "r", encoding="utf-8") as fr:
                template_dict.update(json.load(fr))
    except:
        print("无法读取配置文件")

    # None or str.
    receivers = update_value(value_dict, "receivers")
    if receivers is not None:
        receivers = receivers.split(",")

    temp = {
        "sender": update_value(value_dict, "sender")
        or update_value(template_dict, "sender", False),
        "token": update_value(value_dict, "etoken")
        or update_value(template_dict, "token", False),
        "receivers": receivers or update_value(template_dict, "receivers", False),
        "header": {
            "HeaderFrom": update_value(value_dict, "hfrom")
            or update_value(template_dict, "header", False)["HeaderFrom"],
            "HeaderTo": update_value(value_dict, "hto")
            or update_value(template_dict, "header", False)["HeaderTo"],
        },
        "subject": update_value(value_dict, "subject")
        or update_value(template_dict, "subject", False),
        "message": update_value(value_dict, "message")
        or update_value(template_dict, "message", False),
    }
    return temp


class EmailInformation:
    """Construct the mailbox information base structure.
    """    
    def __init__(self, sender, token, receivers, header, subject, message):

        try:
            sender = sender.replace(' ', '_')
            self.sender = sender
            self.token = token
            self.receivers = receivers
            self.subject = subject
            self.header_from = header["HeaderFrom"]
            self.header_to = header["HeaderTo"]
            self.message = message
        except:
            raise EmailFormatError("邮件信息格式错误,请检查配置以及更新模板！")


    sever_dict = {
        "qq": {"server": "smtp.qq.com", "port": 465},
        "163": {"server": "smtp.163.com", "port": 465},
        "126": {"server": "smtp.126.com", "port": 25},
        "139": {"server": "smtp.139.com", "port": 25},
        "gmail": {"server": "smtp.gmail.com", "port": 587},
        "yahoo": {"server": "smtp.mail.yahoo.com", "port": 465},
    }
    EmailSendType = ["plain", "html"]


class SendEmail:
    def __init__(self, emailinfo: EmailInformation):
        self.sender = emailinfo.sender
        self.token = emailinfo.token
        self.receivers = emailinfo.receivers
        self.subject = emailinfo.subject
        self.header_from = emailinfo.header_from
        self.header_to = emailinfo.header_to
        self.message = emailinfo.message

        self.server = None
        self.send_email_type = emailinfo.EmailSendType[1]

    @staticmethod
    def recognize_email_type(sender: str):
        """_summary_
        Verify sender email compliance
        Args:
            sender (str): sender email

        Returns:
            Error or sender_type
        """
        try:
            rule = r"^[a-zA-Z0-9_-]+@([a-zA-Z0-9]+)\.com$"
            if match(rule, sender):
                return match(rule, sender)[1]
            else:
                raise EmailTypeError("邮箱类型错误")
        except Exception as e:
            print(e)
            return False

    def sever_login(self)->None:
        """Login server"""
        result = self.recognize_email_type(self.sender)
        if result:
            try:
                self.sever = smtplib.SMTP_SSL(
                    EmailInformation.sever_dict[result]["server"],
                    EmailInformation.sever_dict[result]["port"],
                )
                self.sever.set_debuglevel(0)
                self.sever.login(self.sender, self.token)

            except Exception as e:
                raise EmailServerLoginError(f"邮箱服务器登录失败, Err: {e}")
        else:
            raise EmailFormatError("邮箱格式解析错误！")


    def send_email(self):
        try:
            email = MIMEText(self.message, self.send_email_type, "utf-8")
            email["From"] = Header(self.header_from)
            
            email["To"] = Header(self.header_to, "utf-8")
            email["Subject"] = Header(self.subject, "utf-8")

            self.sever.sendmail(self.sender, self.receivers, email.as_string())
            self.sever_logout()
        except Exception as e:
            raise EmailSendError(f"邮件发送失败, Err: {e}")
            # raise e

    def sever_logout(self):
        self.sever.quit()


def send_email(info: dict, content_or_path: str):
    """
    尝试发送邮件，如果失败会引起错误的
    """
    if isfile(content_or_path):
        try:
            with open(content_or_path, "r", encoding="utf-8") as f:
                send = f.read()
        except Exception as e:
            raise EmailFormatError(f"无法从文件获取邮件内容, Err: {e}")

    else:
        message = content_or_path

    info["message"] = message

    email_info = EmailInformation(**info)
    send = SendEmail(email_info)
    try:
        send.sever_login()
        send.send_email()
        print("邮件发送成功")
    except Exception as e:
        raise EmailSendError(f"发送邮件失败: {e}")
        # raise e
    finally:
        try:
            send.sever_logout()
        except:
            pass


if __name__ == "__main__":

    send_email(info=value_dict, content_or_path="test")
