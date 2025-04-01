import smtplib
from email.message import EmailMessage
PASSWORD ="uidd liob tsan vsmn"
SENDER = "Balazspy@gmail.com"
def send_email(image_path):
    email_message = EmailMessage()
    email_message['Subject'] = "A new object was detected."
    email_message.set_content("A new object has appeared before the camera.")

    with open(image_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content, maintype='image', subtype='png')

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, SENDER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path=r"C:\Users\balaz\Downloads\Új mappa\m.jpeg")