import datetime

from chatgpt import ai, chat
from sites import site
from speak import speak, takecommand, wish_me
from spotify import spotify
from vscode import opencode
from whapp import whatsapp
from yt import yt

if __name__ == '__main__':
    wish_me()
    while True:
        query = takecommand().lower()
        if 'sam' in query:
            query = query.replace("edwin", "")
            if 'site' in query:
                site(query)

            if 'play music' in query:
                spotify()

            elif 'what are you' in query:
                spotify()

            elif 'using artificial intelligence' in query:
                ai(query)

            elif 'open youtube' in query:
                yt()

            elif 'open code' in query:
                opencode()

            elif 'open spotify' in query:
                spotify()

            elif 'whatsapp message' in query:
                whatsapp()

            elif "time".lower() in query.lower():
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is{strfTime}")

            elif 'exit' in query:
                speak("have a good day mate, see you later")
                exit()

            elif 'stop' in query:
                speak("have a good day mate, see you later")
                exit()

            else:
                chat(query)
