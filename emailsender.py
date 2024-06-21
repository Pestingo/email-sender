import smtplib
import os


def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        # Securely get the sender email and password from environment variables
        sender_email = os.getenv('SENDER_EMAIL')
        sender_password = os.getenv('SENDER_PASSWORD')

        if not sender_email or not sender_password:
            print("Error: Please set the SENDER_EMAIL and SENDER_PASSWORD environment variables.")
            return

        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to, content)
        server.close()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")


if __name__ == "__main__":
    to = input("Enter the email of the recipient:\n")
    content = input("Enter the content for the email:\n")
    sendEmail(to, content)
