import smtplib
from email.message import EmailMessage

# Inputs
to = input('Enter the To Address: ')
sub = input('Enter The Subject: ')
cont = input('Enter the Content: ')

# Creating the email message
email = EmailMessage()
email['from'] = 'Roshan P Mathew'
email['to'] = to
email['subject'] = sub
email.set_content(cont)

try:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        
        # Using the correct login credentials
        smtp.login('pythondummy03@gmail.com', 'pythonprogram')
        
        smtp.send_message(email)
        print("Email sent successfully")
except smtplib.SMTPAuthenticationError:
    print("Authentication error: Please check your email and password or enable 'Less secure app access' in your Google account settings.")
except Exception as e:
    print(f"An error occurred: {e}")
