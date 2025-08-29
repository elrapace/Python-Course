import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Luca'
email['to'] = 'nicoangeli2002@gmail.com'
email['subject'] = 'You won 1,000,00 dollars!' 

email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smpt.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email , mio account gmail', 'password, mio account gmail')
    smtp.send_message(email)
    print('all good boss!')