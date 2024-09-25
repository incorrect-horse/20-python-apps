import smtplib
from email.message import EmailMessage
import imghdr
import os

host = "smtp.gmail.com"
port = 587
username = os.getenv("USER_NAME")
password = os.getenv("SEND_EMAIL")
receiver = os.getenv("EMAIL_ADDRESS")

def send_email(image_path):
    print("Email was sent!")

    email_message = EmailMessage()
    email_message["Subject"] = "Movement detected on camera"
    email_message.set_content("Some a-hole just wandered in front of the camera...")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image",
                                 subtype=imghdr.what(None, content))
    
    gmail = smtplib.SMTP(host, port)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(username, receiver, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email(image_path="images/00019.png")
