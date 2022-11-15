import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import csv
from random import randint
from time import sleep



def send_mail(fromaddr, frompasswd, toaddr, msg_subject, msg_body, file_path):
    try:
        msg = MIMEMultipart()
        print("[+] Message Object Created")
    except:
        print("[-] Error in Creating Message Object")
        return

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = msg_subject

    body = msg_body

    msg.attach(MIMEText(body, 'plain'))

    filename = file_path
    attachment = open(filename, "rb")

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    try:
        msg.attach(p)
        print("[+] File Attached")
    except:
        print("[-] Error in Attaching file")
        return

    try:
        # s = smtplib.SMTP('smtp.gmail.com', 587)
        s = smtplib.SMTP('stud.iitp.ac.in', 587)
        print("[+] SMTP Session Created")
    except:
        print("[-] Error in creating SMTP session")
        return

    s.starttls()

    try:
        s.login(fromaddr, frompasswd)
        print("[+] Login Successful")
    except:
        print("[-] Login Failed")

    text = msg.as_string()

    try:
        s.sendmail(fromaddr, toaddr, text)
        print("[+] Mail Sent successfully")
    except:
        print('[-] Mail not sent')

    s.quit()


def isEmail(x):
    if ('@' in x) and ('.' in x):
        return True
    else:
        return False



def main_mail(to):
    FROM_ADDR = "nitesh_2001me42@iitp.ac.in"#input Email username
    FROM_PASSWD = "***"#input Email password

    Subject = "Tutorial 6  "
    Body ='''
    Sir please find the attachment

    Thanking You.
     
    --
    Nitesh Srivastava
    2001ME42
    '''
    file_path="output\\attendance_report_consolidated.xlsx"
    if(len(to)==0):
        print("No email address provided. So no mail sent.")
    else:
    #what a ever is the limit of your sending mails, like gmail has 500.
       send_mail(FROM_ADDR, FROM_PASSWD, to, Subject, Body, file_path)
