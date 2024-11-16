import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Store names and emails in a dictionary
participants = {
    'Alice': 'alice@example.com',
    'Bob': 'bob@example.com',
    'Charlie': 'charlie@example.com',
    # Add more participants here
}

# Function to send email
def send_email(recipient, subject, body):
    sender_email = "your_email@example.com"
    sender_password = "your_email_password"
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, recipient, text)
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Error sending email to {recipient}: {e}")

# Function to assign Secret Santa
def assign_secret_santa(participants):
    names = list(participants.keys())
    random.shuffle(names)
    
    # Pair each person with a random Secret Santa
    assignments = {}
    for i in range(len(names)):
        assignments[names[i]] = names[(i + 1) % len(names)]  # To ensure no one is their own Secret Santa
    return assignments

# Function to create and send the gift assignment email
def send_secret_santa_emails(assignments, participants):
    for person, santa in assignments.items():
        recipient_email = participants[person]
        subject = "Your Secret Santa Assignment"
        body = f"Hello {person},\n\nYou are the Secret Santa for {santa}! Please buy them a gift.\n\nHappy Holidays!"
        send_email(recipient_email, subject, body)

# Assign Secret Santa and send emails
assignments = assign_secret_santa(participants)
send_secret_santa_emails(assignments, participants)