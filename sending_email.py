import os
import smtplib

EMAIL_ADDRESS = os.environ.get('PERSONAL_BOT_EMAIL')
EMAIL_PASSWORD = os.environ.get('PERSONAL_BOT_PASS')

TARGET_EMAIL = os.environ.get('TARGET_EMAIL')

print("start")
with smtplib.SMTP('smtp.gmail.com', 587) as smtp_1:
    smtp_1.ehlo()
    smtp_1.starttls()
    smtp_1.ehlo()

    smtp_1.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Test'
    body = 'This is me learning how to use email(smtplib) in python'

    message = f'Subject: {subject}\n\n{body}'

    smtp_1.sendmail(EMAIL_ADDRESS, TARGET_EMAIL , message)
    print("Email Sent")
