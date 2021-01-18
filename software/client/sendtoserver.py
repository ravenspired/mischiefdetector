import email, smtplib, ssl, time

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os.path
from os import path
print("\n sendtoserver.py has been summoned.")

#Detecting a screenshot to send
if path.exists("offending_screenshot.png"):
	print("sendtoserver.py: offensive screenshot found. Sending email to authorities.")
	report()
	print("sendtoserver.py: email sent. Moving on.")
else:
	print("sendtoserver.py: no offensive screenshot found. Continuing loop.")
	#do nothing, continue the service loop



def report():
	subject = "avoronov2022: " + str(time.time())#ill change this to print the username of the device when we get more than one user.
	body = "A violation has been detected. Please review."
	sender_email = "mischiefservice@gmail.com"
	receiver_email = "mischiefservice@gmail.com"
	password = "scifairproj!"

	# Create a multipart message and set headers
	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = subject
	message["Bcc"] = receiver_email  # Recommended for mass emails, but not needed atm since the email stays in one inbox.

	# Add body to email
	message.attach(MIMEText(body, "plain"))

	filename = "offending_screenshot.png"  # In same directory as script


	with open(filename, "rb") as attachment:

	    part = MIMEBase("application", "octet-stream")
	    part.set_payload(attachment.read())

	# encrypt and encode the photograph in base64  
	encoders.encode_base64(part)

	# Add header as key/value pair to attachment part
	part.add_header(
	    "Content-Disposition",
	    f"attachment; filename= {filename}",
	)

	# Add attachment to message and convert message to string
	message.attach(part)
	text = message.as_string()

	# Log in to server using secure context and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, text)