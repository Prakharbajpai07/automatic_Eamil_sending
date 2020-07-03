import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Prakhar Bajpai'
email['to'] = 'Email'
email['subject'] = 'you won 300000 prakhar'
email.set_content('I am invatable')

with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("email", "password")
        smtp.send_message(email)
        print("all good boss")
