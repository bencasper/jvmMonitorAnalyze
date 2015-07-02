from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import smtplib
from os import listdir
from os.path import isfile, join, basename

__author__ = 'ben'


class EmailSend(object):
    mailConfigFile = 'mail_configure.conf'

    def __init__(self):
        self.send_from = 'letvcooperate@163.com'
        self.mail_server = 'smtp.163.com'
        self.passwd = 'letvcoop_123'
        self.send_to = ['zsydn007@gmail.com','zhangpeng@letv.com']

    def email_info(self):
        # read from file to get mail info
        with open(self.mailConfigFile, 'r') as mailFile:
            pass

    def send_email(self, subject, text, files=None):
        assert isinstance(self.send_to, list)

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.send_from
        msg['To'] = COMMASPACE.join(self.send_to)
        msg['Date'] = formatdate(localtime=True)
        msg.attach(MIMEText(text))
        for f in files or []:
            with open(f, "rb") as fil:
                msg.attach(MIMEApplication(
                    fil.read(),
                    Content_Disposition='attachment; filename="%s"' % basename(f)
                ))
        try:
            mail = smtplib.SMTP(self.mail_server)
            mail.starttls()
            mail.login(self.send_from, self.passwd)
            if mail.verify(self.send_from):
                mail.sendmail(self.send_from, self.send_to, msg.as_string())
                mail.close()
        except smtplib.SMTPConnectError:
            print 'smtp connect error'
        except smtplib.SMTPAuthenticationError:
            print 'smtp authentication error'
        print 'send email successful!'

    def write_email(self):
        attach_path = '/Users/ben/PycharmProjects/jvmMonitorAnalyze/logs'
        attach_files = [join(attach_path,f) for f in listdir(attach_path) if isfile(join(attach_path, f))]
        self.send_email('server upload monitor', 'this is a email send by ptyhon', attach_files)

EmailSend().write_email()