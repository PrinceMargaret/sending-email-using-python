__author__="Prince"

import smtplib   #if module not found use >>>>>>>>>>>>>>>  pip install smtplib

#=============================================================================================================
#editable part
From, App_password="senderemail@gmail.com", "sender_app_password"     # this detail used for login in smtp.gmail.com server
To="recieveremail@gmail.com"          #give email where message you want send reciever email
Subject="PrinceMargaret"           #write your own subject PrinceMargaret only for example
Compose_email=" Hi , how are you?"   #write what you want message 
#==============================================================================================================

with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(From,App_password)
    smtp.sendmail(From,To,f"Subject:{Subject} \n\n {Compose_email}")