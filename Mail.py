import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mail:
    def __init__(self, params):
        self.port = params['port']
        self.host = params['host']
        self.add = params['add']
        self.to_add = params['to_add']
        self.title = params['title']
        self.body = params['body']

    def send_mail(self):
        try:
            msg = MIMEText(self.body)
            msg['Subject'] = self.title
            msg['From'] = self.add
            msg['Disposition-Notification-To'] = self.add
            msg['Bcc'] = self.add
            if type(self.to_add) is str:
                msg['To'] = self.to_add    
            else:
                msg['To'] = ','.join(self.to_add)
            smtp = smtplib.SMTP(self.host, self.port)
            smtp.send_message(msg = msg)
            smtp.close()
            print("送信成功")
        except BaseException as error:
            print("送信エラー")
            raise error