import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        if attachment_path:
            if os.path.exists(attachment_path):
                file_extension = os.path.splitext(attachment_path)[1].lower()
                if file_extension in ['.png', '.jpg', '.jpeg']:
                    with open(attachment_path, 'rb') as attachment:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename={os.path.basename(attachment_path)}'
                    )
                    msg.attach(part)
                else:
                    print("Error: Only PNG, JPG, and JPEG files are allowed as attachments.")
                    return
            else:
                print("Error: The attachment file does not exist.")
                return

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

def main():
    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password: ")
    recipient_email = "hr@ignitershub.com"
    subject = "Challenge 3 Completed"

    name = input("Enter your name: ")
    semester = input("Enter your semester: ")
    branch = input("Enter your branch: ")
    roll_number = input("Enter your roll number: ")

    body = f"Name: {name}\nSemester: {semester}\nBranch: {branch}\nRoll Number: {roll_number}"

    attachment_path = input("Enter the path to the image attachment: ")

    send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path)

if __name__ == "__main__":
    main()
