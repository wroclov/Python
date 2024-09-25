
# never up and running, two versions, it would require some api_key, account password, etc.
import requests

def send_email_with_mailgun(api_key: str, domain: str, recipient_email: str, subject: str, body: str):
    """
    Sends an email using Mailgun's API without specifying your own email.

    Parameters:
    - api_key (str): Your Mailgun API key.
    - domain (str): Your Mailgun domain.
    - recipient_email (str): The recipient's email address.
    - subject (str): The subject of the email.
    - body (str): The body content of the email.
    """
    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={
            "from": f"Mailgun Sandbox <mailgun@{domain}>",
            "to": recipient_email,
            "subject": subject,
            "text": body
        })

# Example usage
api_key = "your_mailgun_api_key"
domain = "your_mailgun_domain"
recipient = "recipient_email@example.com"
subject = "Test Email"
body = "This is the body of the email."

response = send_email_with_mailgun(api_key, domain, recipient, subject, body)
print(f"Response: {response.status_code}, {response.text}")


#### or
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Create the message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    # Attach the body with the message instance
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the Gmail server (SMTP)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(sender_email, sender_password)

        # Convert the message to a string and send it
        server.sendmail(sender_email, recipient_email, message.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

    finally:
        server.quit()

# Example usage:
send_email(
    sender_email='your_email@gmail.com',
    sender_password='your_password',
    recipient_email='recipient_email@example.com',
    subject='Test Email',
    body='This is a test email sent from Python.'
)
