import smtplib
from email.mime.text import MIMEText
from email.header import Header
from re import match


class EmailFormatError(Exception):
    ...


class EmailServerLoginError(Exception):
    ...


class EmailSendError(Exception):
    ...


class EmailInformation():
    def __init__(self, sender, token, receivers, header, subject, message):
        self.sender = sender
        self.token = token
        self.receivers = receivers
        self.subject = subject
        self.header_from = header['HeaderFrom']
        self.header_to = header['HeaderTo']
        self.message = message

    sever_dict = {'qq':     {'server': 'smtp.qq.com',           'port': 465},
                  '163':    {'server': 'smtp.163.com',          'port': 25},
                  '126':    {'server': 'smtp.126.com',          'port': 25},
                  '139':    {'server': 'smtp.139.com',          'port': 25},
                  'gmail':  {'server': 'smtp.gmail.com',        'port': 587},
                  'yahoo':  {'server': 'smtp.mail.yahoo.com',   'port': 465}
                  }
    EmailSendType = ['plain', 'html']


class SendEmail():

    def __init__(self, EmailInformation: EmailInformation):
        self.sender = EmailInformation.sender
        self.token = EmailInformation.token
        self.receivers = EmailInformation.receivers
        self.subject = EmailInformation.subject
        self.header_from = EmailInformation.header_from
        self.header_to = EmailInformation.header_to
        self.message = EmailInformation.message

        self.server = None
        self.send_email_type = EmailInformation.EmailSendType[1]

    @staticmethod
    def recognize_email_type(sender):
        rule = r'^[a-zA-Z0-9_-]+@([a-zA-Z0-9]+)\.com$'
        if match(rule, sender):
            return match(rule, sender)[1]
        else:
            return None

    def sever_login(self):
        result = self.recognize_email_type(self.sender)
        if len(result) != 0:
            try:
                self.sever = smtplib.SMTP_SSL(
                    EmailInformation.sever_dict[result]['server'], EmailInformation.sever_dict[result]['port'])
                self.sever.set_debuglevel(0)
                self.sever.login(self.sender, self.token)

            except Exception as e:
                raise EmailServerLoginError('邮箱服务器登录失败')
        else:
            raise EmailFormatError('邮箱格式错误')

    def send_email(self):
        try:
            email = MIMEText(self.message, self.send_email_type, 'utf-8')
            email['From'] = Header(self.header_from, 'utf-8')
            email['To'] = Header(self.header_to, 'utf-8')
            email['Subject'] = Header(self.subject, 'utf-8')

            self.sever.sendmail(self.sender, self.receivers, email.as_string())
            self.sever_logout()
        except Exception as e:
            raise EmailSendError('邮件发送失败')

    def sever_logout(self):
        self.sever.quit()


if __name__ == '__main__':
    info = {'sender': '1157723200@qq.com', 'token': 'mqrsefodflqejcji', 'receivers': ['1157723200@qq.com', 'azureqaq@icloud.com'], 'header': {
        'HeaderFrom': 'Personal Intelligence System', 'HeaderTo': 'BOSS'}, 'subject': 'Email test', 'message': 'This is a test email.'}
    with open('htmltest.html', 'r', encoding='utf-8') as f:
        send = f.read()
        info['message'] = send

    email_info = EmailInformation(**info)
    send = SendEmail(email_info)
    try:
        send.sever_login()
        send.send_email()
    except Exception as e:
        print(e)
        send.sever_logout()
