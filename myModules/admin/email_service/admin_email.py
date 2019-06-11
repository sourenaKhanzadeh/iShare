import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    """
    This Class Will
    Send Automatic Email
    To The New User
    """
    def __init__(self, admin, password):
        self._admin = admin
        self._password = password

        self.server = self.server()

    def server(self, iD=0):
        """
        add all type of
        servers here...
        """
        if iD == 0:
            # gmail SMTP
            return smtplib.SMTP('smtp.gmail.com', 587)

    def connection(self):
        # start TLS for security
        self.server.starttls()

        # Authentication
        self.server.login(self.admin, password)

    def send_to(self, to, subject, message, attachment=None):
        msg = MIMEMultipart()
        msg['From'] = self.admin
        msg['To'] = to
        msg['Subject'] = subject
        if attachment is not None:
            # send as html
            msg.attach(MIMEText(attachment, "html"))
        else:
            msg.attach(message)

        try:
            # login server
            self.connection()

            # sending the mail
            self.server.sendmail(msg['From'], msg['To'], msg.as_string())

            print("Sent....." + msg.as_string())

            # terminating the session
            self.server.quit()

        except Exception as e:
            print("Something Went Wrong \n-------------\n" + str(e))

    @property
    def admin(self):
        return self._admin
    @property
    def password(self):
        return self._password

    @admin.setter
    def admin(self, value):
        self._admin = value
    @password.setter
    def password(self, value):
        self._password = value

username = "Your_Username"
password = "Your_Password"

to = "Enter_Email"
msg = "Enter_Message"

# attach the file html
attachment = "email-content.html"

with open(attachment, 'r') as file:
    attachment = file.read()

admin_email = Email(username, password)
# admin_email.send_to(to, "Enter_Subject", msg, attachment)
