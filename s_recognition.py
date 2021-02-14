import requests
import os
from dotenv import load_dotenv, find_dotenv
import speech_recognition as sr
from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv(find_dotenv())

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

headers = {
    'x-rapidapi-key': os.environ.get("RAPIDAPI_KEY"),
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
    }

slang_words = ["hood", "lit", "boomer"]

def get_urban_meaning(word):    #call urban dictionary with speech
    try:
        querystring = {"term": word}
        response = requests.request("GET", url, headers=headers, params=querystring)
        data_fetched_json = json.loads(response.text)
        word_meaning = data_fetched_json["list"][0]['definition']
        return word_meaning
    except:
        print("empty word error")


r = sr.Recognizer()
# speech = sr.Microphone()
# authenticator = IAMAuthenticator(os.environ.get("IBMAPI_KEY"))
# speech_to_text = SpeechToTextV1(
#     authenticator=authenticator
# )


# speech_to_text.set_service_url(os.environ.get("IBM_URL"))


with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)

# with speech as source:
#     print("say something!!…")
#     audio_file = r.adjust_for_ambient_noise(source)
#     audio_file = r.listen(source)
# speech_recognition_results = speech_to_text.recognize(audio=audio_file.get_wav_data(), content_type='audio/wav').get_result()

# json_object = json.dumps(text, indent=2)
# print(json_object)
# json_raw = json.loads(json_object)

# extracted_speech = json_raw["results"][0]["alternatives"][0]["transcript"]
text = text.lower().split(" ")[0:-1]
print(text)

for word in text:
    if "*" in word:
        print("profanity!")
    elif word == "dog":
        print("calling someone dawgg could be inappropriate")
    elif word in slang_words:
        print(get_urban_meaning(word))






