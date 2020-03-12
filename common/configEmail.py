# -*- coding: utf-8 -*-

import os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import readConfig
import smtplib
from common.log import MyLog

getlog = MyLog.getLog()
log = getlog.logger

localReadConfig = readConfig.ReadConfig()


class conEmail:
    def __init__(self):
        global shost, sUser, sPassword, sport, fromUser, toUser, subject, text, attachfile, on_off
        shost = localReadConfig.get_email("mail_host")
        sUser = localReadConfig.get_email("mail_user")
        sPassword = localReadConfig.get_email("mail_pass")
        sport = localReadConfig.get_email("mail_port")
        fromUser = localReadConfig.get_email("sender")
        # toUser = list(localReadConfig.get_email("receiver").__str__().split(";"))
        toUser = localReadConfig.get_email("receiver")
        subject = localReadConfig.get_email("subject")
        text = localReadConfig.get_email("content")
        on_off = int(localReadConfig.get_email("on_off"))

    def read_read_file(self, result_file):
        with open(result_file, 'rb') as f:
            self.result_content = f.read()
        return self.result_content

    def configEmail(self, attach_Path):
        text_result = self.read_read_file(attach_Path)
        msg = MIMEMultipart()
        # 组织头信息
        msg['From'] = fromUser
        msg['TO'] = toUser
        msg['subject'] = Header(subject, "utf-8")

        # 组织文本信息，邮件正文信息
        msgtext = MIMEText(text_result, _subtype='html', _charset='utf-8')
        msg.attach(msgtext)

        # 构造附件（如果有多个附件，则我们需要以此方式对附件进行增加）
        attachName = os.path.split(attach_Path)[-1]
        attachPart = MIMEApplication(open(attach_Path, 'rb').read())
        attachPart.add_header('Content-Disposition', 'attachment', filename=os.path.split(attach_Path)[-1])
        msg.attach(attachPart)
        log.info("add {} to email attachment".format(attachName))
        return msg

    def sendMail(self, email_attach):
        msg = self.configEmail(email_attach)
        smtp = smtplib.SMTP()
        if on_off == 1:
            try:
                smtp.connect(host=shost, port=sport)
                smtp.login(user=sUser, password=sPassword)
                smtp.sendmail(from_addr=fromUser, to_addrs=toUser, msg=msg.as_string())
                log.info("Test Result <{0}> has sent to \"{1}\"".format(email_attach, msg['TO']))
            except smtp.SMTPException as e:
                log.error("Test Result sent Failed. ")
                log.error(e)

            finally:
                smtp.quit()
        elif on_off == 0:
            log.info('''
                  Not Send E-mail(Electronic Mail).
                  you need to set "on_off" value is "1" in config.ini if you want to send this email, 
                  ("on_off" value is 0: Not send)''')
