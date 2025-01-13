import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv
import os

load_dotenv()

def send_email(to_email, subject, message):
    # Email credentials
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('APP_PASSWORD')

    # Create email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))


    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.close()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == '__main__':
    # recepient_email = os.getenv('SENDER_EMAIL')
    emails = ['tackletalha@gmail.com', 'talharjframe@gmail.com', 'bugf636@gmail.com']
    subject = 'Test Subject'
    message = 'This is a test message from talha'
    
    for email in emails:
        send_email(email, subject, message)
