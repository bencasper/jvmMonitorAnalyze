from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import logging
import smtplib
from os import listdir
from os.path import isfile, join, basename
from time import strftime, gmtime

from conf_parse import parse_conf, mk_log_dir


__author__ = 'ben'
mk_log_dir()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig()


class EmailSend(object):
    def __init__(self):
        conf_json = parse_conf()
        mail_json = conf_json['mail_conf']
        if mail_json is not None:
            self.send_from = mail_json['send_from']
            logger.info("send_from: %s", self.send_from)
            self.mail_server = mail_json['mail_server']
            logger.info("mail_server: %s", self.mail_server)
            self.passwd = mail_json['passwd']
            logger.info("passwd: %s", self.passwd)
            self.send_to = mail_json['send_to']
            logger.info("send_to: %s", mail_json['send_to'])


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
            logger.error('smtp connect error')
        except smtplib.SMTPAuthenticationError:
            logger.error('smtp authentication error')

    def write_email(self):
        attach_path = '/letv/logs/monitor'
        attach_files = [join(attach_path, f) for f in listdir(attach_path) if isfile(join(attach_path, f))]
        self.send_email('server upload monitor', 'this is a email send by ptyhon', attach_files)
        logger.info("send email at %s",strftime("%Y-%m-%d %H:%M:%S", gmtime()))


if __name__ == "__main__":
    EmailSend().write_email()