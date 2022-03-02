
import os
import smtplib


def send_email(subject='', text=''):
    gmail_user = os.getenv('MY_GMAIL_USER')
    gmail_pwd = os.getenv('MY_GMAIL_PWD')
    FROM = 'stanleyjjy@gmail.com'
    TO = ['yanjingyu@gmail.com']  # must be a list
    SUBJECT = subject
    TEXT = text

    # Prepare actual message

    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s

    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    try:
        with smtplib.SMTP('smtp.gmail.com:587') as server:
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            print('successfully sent the mail')
    except Exception as ex:
        print(f"failed to send mail: gmail_user: {gmail_user} {str(ex)}")