import os
import smtplib
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PSWD = os.getenv("PASSWORD")


def main():
    you = me

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Script Complete"
    msg["From"] = me
    msg["To"] = you

    mail.sendmail(me, you, msg.as_string())

    print("Mail sent successfully to")
    print(you)
    del msg


if __name__ == "__main__":
    me = EMAIL

    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(me, PSWD)

    main()

    mail.quit()
