import json
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from os.path import isfile
from re import match



class EmailInformation:
    def __init__(self, sender, token, receivers, header, subject, message):
        self.sender = sender
        self.token = token
        self.receivers = receivers
        self.subject = subject
        self.header_from = header["HeaderFrom"]
        self.header_to = header["HeaderTo"]
        self.message = message

    sever_dict = {
        "qq": {"server": "smtp.qq.com", "port": 465},
        "163": {"server": "smtp.163.com", "port": 25},
        "126": {"server": "smtp.126.com", "port": 25},
        "139": {"server": "smtp.139.com", "port": 25},
        "gmail": {"server": "smtp.gmail.com", "port": 587},
        "yahoo": {"server": "smtp.mail.yahoo.com", "port": 465},
    }
    EmailSendType = ["plain", "html"]


class SendEmail:
    def __init__(self):
        self.sender = '1157723200@qq.com'
        self.token = "dyuoywcxjnluggcd"
        self.receivers = ["1157723200@qq.com",]
        self.subject = "Daily Intelligence Report"
        self.header_from = "1157723200@qq.com"
        self.header_to = "BOSS"
        self.message = 'test'


        self.server = None
        self.send_email_type = 'plain'


    def sever_login(self):

        self.sever = smtplib.SMTP_SSL(
            EmailInformation.sever_dict['qq']["server"],
            EmailInformation.sever_dict['qq']["port"],
        )
        self.sever.set_debuglevel(0)
        self.sever.login(self.sender, self.token)


    def send_email(self):
        try:
            email = MIMEText(self.message, self.send_email_type, "utf-8")
            email["From"] = Header(self.header_from)
            email["To"] = Header(self.header_to, "utf-8")
            email["Subject"] = Header(self.subject, "utf-8")
            print(email.as_string())
            self.sever.sendmail(self.sender, self.receivers, email.as_string())
            self.sever_logout()
        except Exception as e:
            print(e)

    def sever_logout(self):
        self.sever.quit()




if __name__ == "__main__":
    send = SendEmail()
    send.sever_login()
    send.send_email()
    # send.sever_logout()
    
    value_dict = {
        "receivers": ["1157723200@qq.com",],
        "sender": "1157723200@qq.com",
        "token": "dyuoywcxjnluggcd",
        "header": {"HeaderFrom": "rewrwe <1157723200@qq.com>", "HeaderTo": "BOSS"},
        "subject": "Daily Intelligence Report",
        "message": "This is a test email.",
    }