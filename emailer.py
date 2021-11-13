import os
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send(file, recipient):
	'''Sends an email with file attached to recipient'''
	# TODO: implement this
	subject = "PDF Manager File Conversion"
	body = "Thank you for using the PDF Manager software! The file you had converted is converted is attached to this " \
		   "email. Please do not reply to this email as it's not monitored. If you have any questions or concerns about " \
		   "your please contact us at pdf.manager.help@gmail.com" \
	EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
	EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

	message = MIMEMultipart()
	message["From"] = EMAIL_ADDRESS
	message["To"] = recipient
	message["Subject"] = subject
	message.attach(MIMEText(body, "plain"))

	with open(file, "rb") as attachment:
		part = MIMEBase("application", "octet-stream")
		part.set_payload(attachment.read())

	encoders.encode_base64(part)

	part.add_header(
		"Content-Disposition",
		f"attachment; filename= {file}",
	)

	message.attach(part)
	text = message.as_string()

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
		server.sendmail(EMAIL_ADDRESS, recipient, text)