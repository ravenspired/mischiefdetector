#this script sends email to web service

import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "mischiefservice@gmail.com"
receiver_email = "mischiefservice@gmail.com"
password = "scifairproj!"
message = """\
Subject: Violation

user 'avoronov2022' has violated the TOS."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)