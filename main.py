import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login('ashutoshtripathi0120@gmail.com', 'izmdtwkkmyzkaxkb')
    email = EmailMessage()
    email['From'] = 'ashutoshtripathi0120@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'dude': 'COOL_DUDE_EMAIL',
    'nadeem chaudhary': 'nadeemchaudhary808@gmail.com',
    'pradeep tiwari': 'itspradeeptripathi@gmail.com',
    'ashutosh pandey': '2008390100019@reck.ac.in',
    'anuj dubey': '2008390100014@reck.ac.in',
    'rohan sirsa': '2008390100047@reck.ac.in',
    'irene': 'irene@redvelvet.com'
}


def get_email_info():
    talk(' Het there I am an Email BOT Created by Ashutosh Tripathi ,To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    print("What is the subject of you email?")
    subject = get_info()
    talk('Tell me the text in your email')
    print('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey lazy ass. Your email is sent')
    print("Your E mail has been sent successfully")
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
