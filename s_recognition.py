import requests
import os
from dotenv import load_dotenv, find_dotenv
import speech_recognition as sr
from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from urban_dict import pop_up_window, get_urban_meaning

load_dotenv(find_dotenv())

slang_words = ["poggers", "lit", "boomer"]

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
        pop_up_window("profanity!")
    elif word == "dog":
        pop_up_window("calling someone dawgg could be inappropriate")
    elif word in slang_words:
        get_urban_meaning(word)






