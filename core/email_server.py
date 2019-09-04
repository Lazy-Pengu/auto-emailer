import smtplib
import os
import base64
import sys

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from gen_encode_pas import gen_pas
from info import file_path_builder, due_date_info, email_list
from drive_file_downloader import retrieve_file

class Emailer():
    
    def __init__(self):
        self.smtp_obj = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        self.smtp_obj.ehlo()
        
    def login(self, pause):
        try:
            path = file_path_builder("[4].txt")
            if not os.path.exists(path[0]):
                gen_pas()

            with open(path[0], 'rb') as file:
                pas = base64.b64decode(file.read()).decode('utf-8')

            self.smtp_obj.login('[5]', pas)
        except:
            print("Error Occurred")
            print('---Program Ended---')
            print('---CLOSING---')
            
            pause(2)
            sys.exit(1)
            
    def send(self, msg):
        self.smtp_obj.send_message(msg)

    def logoff(self):
        self.smtp_obj.quit()
        
    def msg_builder(name, accessed):

        msg_builder = due_date_info()
        msg_body = MIMEText(msg_builder)

        attachment = MIMEBase('application', 'octet-stream')
        file_path = retrieve_file(accessed)

        with open(file_path, 'rb') as file:
            attachment.set_payload(file.read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment', filename='[2].pdf')

        msg = MIMEMultipart()
        msg['From'] = '[6]'
        msg['To'] = email_list[name]
        msg['Subject'] = "[7]"

        msg.attach(attachment)
        msg.attach(msg_body)
        
        return msg