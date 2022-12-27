import smtplib
from email.mime.text import MIMEText
from email.header import Header
from re import match
from tools.error import EmailFormatError, EmailServerLoginError, EmailSendError
from os.path import isfile


class EmailInformation():
    def __init__(self, sender, token, receivers, header, subject, message):
        self.sender = sender
        self.token = token
        self.receivers = receivers
        self.subject = subject
        self.header_from = header['HeaderFrom']
        self.header_to = header['HeaderTo']
        self.message = message

    sever_dict = {
        'qq':       {'server': 'smtp.qq.com',           'port': 465},
        '163':      {'server': 'smtp.163.com',          'port': 25},
        '126':      {'server': 'smtp.126.com',          'port': 25},
        '139':      {'server': 'smtp.139.com',          'port': 25},
        'gmail':    {'server': 'smtp.gmail.com',        'port': 587},
        'yahoo':    {'server': 'smtp.mail.yahoo.com',   'port': 465}
    }
    EmailSendType = ['plain', 'html']


class SendEmail():

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
                raise EmailServerLoginError(f'邮箱服务器登录失败, Err: {e}')
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
            raise EmailSendError(f'邮件发送失败, Err: {e}')

    def sever_logout(self):
        self.sever.quit()


def send_email(info: dict, content_or_path: str):
    '''
    尝试发送邮件，如果失败会引起错误的
    '''
    if isfile(content_or_path):
        try:
            with open(content_or_path, 'r', encoding='utf-8') as f:
                send = f.read()
        except Exception as e:
            raise EmailFormatError(f'无法获取邮件内容, Err: {e}')

    else:
        send = content_or_path

    info['message'] = send

    email_info = EmailInformation(**info)
    send = SendEmail(email_info)
    try:
        send.sever_login()
        send.send_email()
        print('邮件发送成功')
    except Exception as e:
        raise EmailSendError(f'发送邮件失败: {e}')
    finally:
        try:
            send.sever_logout()
        except:
            pass


if __name__ == '__main__':
    info = {'sender': '1157723200@qq.com', 'token': 'mqrsefodflqejcji', 'receivers': ['1157723200@qq.com', 'azureqaq@icloud.com'], 'header': {
        'HeaderFrom': 'Personal Intelligence System', 'HeaderTo': 'BOSS'}, 'subject': 'Email test', 'message': 'This is a test email.'}
    with open('test.html', 'r', encoding='utf-8') as f:
        send = f.read()
        info['message'] = send

    email_info = EmailInformation(**info)
    send = SendEmail(email_info)
    try:
        send.sever_login()
        send.send_email()
    except Exception as e:
        print(e)
    finally:
        send.sever_logout()
