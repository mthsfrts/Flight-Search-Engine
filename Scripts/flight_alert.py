# Libraries
import smtplib
from email.message import EmailMessage
from OAuth_Google import OAuth
from main import client_email

# Auth Object

passwrd = OAuth.get_token()


# Main Class
class FlightAlert:
    """This class is responsible for send sms every time that the threshold is passed"""

    @staticmethod
    def send_alert(subject, message):

        # Variables
        sender = 'flightdeals.espresso@gmail.com'
        receiver = f'{client_email}'

        # Alert
        alert = EmailMessage()
        alert.set_content(message)
        alert['from'] = sender
        alert['to'] = receiver
        alert['subject'] = subject

        # Server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, passwrd)

        server.send_message(alert)
        server.quit()

