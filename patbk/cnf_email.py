import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class cnf:
    __init__(self,)#hs_name,email
    def send_email(sender_email, receiver_email, subject, message):
        # SMTP server configuration
        smtp_server = 'smtp.example.com'
        smtp_port = 587  # Change it according to your SMTP server
        
        # Email account credentials
        email_username = 'your_email@example.com'
        email_password = 'your_email_password'
        
        # Create a MIMEText object to represent the email
        email_body = MIMEText(message, 'plain')
        
        # Create a MIMEMultipart object to represent the email
        email = MIMEMultipart()
        email.attach(email_body)
        email['From'] = sender_email
        email['To'] = receiver_email
        email['Subject'] = subject
        
        try:
            # Connect to the SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            # Login to your email account
            server.login(email_username, email_password)
            # Send the email
            server.sendmail(sender_email, receiver_email, email.as_string())
            # Close the connection
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print("Error: Unable to send email.")
            print(e)

    # Example usage:
    sender_email = 'your_email@example.com'
    receiver_email = 'recipient@example.com'
    subject = 'Email Confirmation'
    message = 'This is a confirmation email. Your registration is successful.'
    send_email(sender_email, receiver_email, subject, message)
