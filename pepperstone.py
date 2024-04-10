from functions import (speak,takeCommand,wishMe)
from brain import chat
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case
        res = chat.send_message(query)
        speak(res.text)