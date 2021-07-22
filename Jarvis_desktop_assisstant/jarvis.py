import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import credentials as cr


# 'sapi5' is used here to use computer voice
engine = pyttsx3.init('sapi5')
class RegisterClass:
    def __init__(self):

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)


        # there are 2 voices in PC [0] is male and [1] is female

def speak(audio):
        engine.say(audio)
        engine.runAndWait()


def wishMe():
    '''
    It is a function  which tells jarvis to greet user with good mornin
    ,afternoon or good evening.
    :return:
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        pyttsx3.speak('Good Morning!')
    elif hour >= 12 and hour < 18:
        pyttsx3.speak('Good Afternoon!')
    else:
        pyttsx3.speak('Good Evening!')
    pyttsx3.speak('I am Jarvis Sir, Please tell me how may I help you')


def takeCommand():
    '''
    It takes microphone input from the user and return string output.
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening......')
        r.pause_threshold = 0.8  # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
    try:
        print('Recognizing....')
        query = r.recognize_google(audio,
                                           language='en-in')  # Performs speech recognition on ``audio_data`` (an ``AudioData`` instance), using the Google Speech Recognition API.
        print(f'User said: {query}\n')
    except Exception as ex:
        print(ex)

        speak('Say that again please......')
        print('Say that again please......')
        return "None"
    return query


def send_mail():
    rx = {email}
    sub = 'This is mail from Jarvis'
    msg =   f'''Hi ,This is a demo mail from jarvis
    Thank you!!!'''

    mailer = smtplib.SMTP('smtp.gmail.com', 587)
    mailer.ehlo()
    mailer.starttls()
    mailer.login(cr.auth['user_name'], cr.auth['password'])


    email_body = '\r\n'.join(['To:%s' % rx, 'From:%s' % (cr.auth['user_name']),
                                      'Subject:%s' % sub, '', msg])

    mailer.sendmail(cr.auth['user_name'], rx, email_body)
    # print('Email sent')



if __name__ == '__main__':
    speak('Initializing Jarvis....')
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing task based on query

        # for getting information from wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        # for opening youtube
        elif 'open youtube' in query:
            speak('Opening Youtube.....')
            webbrowser.open('youtube.com')

        # for opening google
        elif 'open google' in query:
            speak('Opening Google.....')
            webbrowser.open('google.com')

        # for opening github
        elif 'open github' in query:
            speak('Opening github.....')
            webbrowser.open('github.com')

        #To play music
        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            speak('Playing songs......')
            os.startfile(os.path.join(music_dir, songs[15]))

        # To check current time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir,The Time is {strTime}')


        # opening python idle
        elif 'open python idle' in query:
            codepath = "C:\\Users\\Amit\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\idlelib\\idle.pyw"
            speak('Opening python IDLE')
            os.startfile(codepath)

        elif 'send email' in query:
            try:
                email = input('Enter reciever email id :')
                speak('What should I say')
                content = takeCommand()
                send_mail()
                speak('Email Sent Successfully')
            except Exception as ex:
                print(ex)
                speak('Sorry ,I am not able to send this email')

        elif 'exit' in query:
            speak('OK sir')
            speak('Thank you for using me...')
            speak('bye')
            quit()


