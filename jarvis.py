import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import datetime
import os
import sys
import smtplib
from news import speak_news, getNewsUrl
from OCR import OCR
from diction import translate
from helpers import speak, weather, takeCommand, cpu, joke, screenshot
from youtube import youtube
from sys import platform
import getpass
import cv2

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# print(voices[0].id)


class Jarvis:
    def __init__(self) -> None:
        self.chrome_path = os.getenv("CHROME_PATH")
        if not self.chrome_path:
            if platform == "linux" or platform == "linux2":
                self.chrome_path = "/usr/bin/google-chrome"
            elif platform == "darwin":
                self.chrome_path = "open -a /Applications/Google\\ Chrome.app"
            elif platform == "win32":
                self.chrome_path = (
                    "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                )
            else:
                print("Unsupported OS")
                exit(1)
        webbrowser.register(
            "chrome", None, webbrowser.BackgroundBrowser(self.chrome_path)
        )

    def wishMe(self) -> None:
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning SIR")
        elif hour >= 12 and hour < 18:
            speak("Good Afternoon SIR")

        else:
            speak("Good Evening SIR")

        weather()
        speak("I am JARVIS. Please tell me how can I help you SIR?")

    def sendEmail(self, to, content) -> None:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        user = os.getenv("EMAIL_USER")
        password = os.getenv("EMAIL_PASS")
        server.login(user, password)
        server.sendmail(user, to, content)
        server.close()

    def _handle_wikipedia(self, query):
        speak("Searching Wikipedia....")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    def _change_voice(self, query):
        if "female" in query:
            engine.setProperty("voice", voices[1].id)
        else:
            engine.setProperty("voice", voices[0].id)
        speak("Hello Sir, I have switched my voice. How is it?")

    def _play_music(self):
        music_file = os.getenv("MUSIC_FILE", "D:\\RoiNa.mp3")
        os.startfile(music_file)

    def _search(self):
        speak("What do you want to search for?")
        search = takeCommand()
        url = "https://google.com/search?q=" + search
        webbrowser.get("chrome").open_new_tab(url)
        speak("Here is What I found for" + search)

    def _location(self):
        speak("What is the location?")
        location = takeCommand()
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get("chrome").open_new_tab(url)
        speak("Here is the location " + location)

    def _your_master(self):
        if platform == "win32" or "darwin":
            speak("Gaurav is my master. He created me couple of days ago")
        elif platform == "linux" or platform == "linux2":
            name = getpass.getuser()
            speak(name, "is my master. He is running me right now")

    def _open_code(self):
        if platform == "win32":
            os.startfile(
                "C:\\Users\\gs935\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            )
        elif platform == "linux" or platform == "linux2" or "darwin":
            os.system("code .")

    def _shutdown(self):
        if platform == "win32":
            os.system("shutdown /p /f")
        elif platform == "linux" or platform == "linux2" or "darwin":
            os.system("poweroff")

    def _remember_that(self):
        speak("what should i remember sir")
        rememberMessage = takeCommand()
        speak("you said me to remember" + rememberMessage)
        remember = open("data.txt", "w")
        remember.write(rememberMessage)
        remember.close()

    def _do_you_remember(self):
        remember = open("data.txt", "r")
        speak("you said me to remember that" + remember.read())

    def _dictionary(self):
        speak("What you want to search in your intelligent dictionary?")
        translate(takeCommand())

    def _news(self):
        speak("Ofcourse sir..")
        speak_news()
        speak("Do you want to read the full news...")
        test = takeCommand()
        if "yes" in test:
            speak("Ok Sir, Opening browser...")
            webbrowser.open(getNewsUrl())
            speak("You can now read the full news from this website.")
        else:
            speak("No Problem Sir")

    def _email_to_gaurav(self):
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "email"
            self.sendEmail(to, content)
            speak("Email has been sent!")

        except Exception:
            speak("Sorry sir, Not able to send email at the moment")

    def execute_query(self, query):
        actions = {
            "wikipedia": lambda: self._handle_wikipedia(query),
            "youtube downloader": lambda: exec(open("youtube_downloader.py").read()),
            "voice": lambda: self._change_voice(query),
            "jarvis are you there": lambda: speak("Yes Sir, at your service"),
            "jarvis who made you": lambda: speak("Yes Sir, my master build me in AI"),
            "open youtube": lambda: webbrowser.get("chrome").open_new_tab("https://youtube.com"),
            "open amazon": lambda: webbrowser.get("chrome").open_new_tab("https://amazon.com"),
            "cpu": cpu,
            "joke": joke,
            "screenshot": lambda: (speak("taking screenshot"), screenshot()),
            "open google": lambda: webbrowser.get("chrome").open_new_tab("https://google.com"),
            "open stackoverflow": lambda: webbrowser.get("chrome").open_new_tab("https://stackoverflow.com"),
            "play music": self._play_music,
            "search youtube": lambda: (speak("What you want to search on Youtube?"), youtube(takeCommand())),
            "the time": lambda: speak(f"Sir, the time is {datetime.datetime.now().strftime('%H:%M:%S')}"),
            "search": self._search,
            "location": self._location,
            "your master": self._your_master,
            "your name": lambda: speak("My name is JARVIS"),
            "who made you": lambda: speak("I was created by my AI master in 2021"),
            "stands for": lambda: speak("J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM"),
            "open code": self._open_code,
            "shutdown": self._shutdown,
            "your friend": lambda: speak("My friends are Google assisstant alexa and siri"),
            "github": lambda: webbrowser.get("chrome").open_new_tab("https://github.com/gauravsingh9356"),
            "remember that": self._remember_that,
            "do you remember anything": self._do_you_remember,
            "sleep": lambda: sys.exit(),
            "dictionary": self._dictionary,
            "news": self._news,
            "email to gaurav": self._email_to_gaurav,
        }

        for key, action in actions.items():
            if key in query:
                action()
                break


def wakeUpJARVIS():
    bot_ = Jarvis()
    bot_.wishMe()
    while True:
        query = takeCommand().lower()
        bot_.execute_query(query)


if __name__ == "__main__":

    recognizer = (
        cv2.face.LBPHFaceRecognizer_create()
    )  # Local Binary Patterns Histograms
    recognizer.read("./Face-Recognition/trainer/trainer.yml")  # load trained model
    cascadePath = "./Face-Recognition/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(
        cascadePath
    )  # initializing haar cascade for object detection approach

    font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type

    id = 2  # number of persons you want to Recognize

    names = ["", "Gaurav"]  # names, leave first empty bcz counter starts from 0

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW to remove warning
    cam.set(3, 640)  # set video FrameWidht
    cam.set(4, 480)  # set video FrameHeight

    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    # flag = True

    while True:

        ret, img = cam.read()  # read the frames using the above created object

        converted_image = cv2.cvtColor(
            img, cv2.COLOR_BGR2GRAY
        )  # The function converts an input image from one color space to another

        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for x, y, w, h in faces:

            cv2.rectangle(
                img, (x, y), (x + w, y + h), (0, 255, 0), 2
            )  # used to draw a rectangle on any image

            id, accuracy = recognizer.predict(
                converted_image[y : y + h, x : x + w]
            )  # to predict on every single image

            # Check if accuracy is less them 100 ==> "0" is perfect match
            if accuracy < 100:

                # Do a bit of cleanup
                speak("Optical Face Recognition Done. Welcome")
                cam.release()
                cv2.destroyAllWindows()
                wakeUpJARVIS()
            else:
                speak("Optical Face Recognition Failed")
                break
