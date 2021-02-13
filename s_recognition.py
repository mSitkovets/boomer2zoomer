import requests
import os
from dotenv import load_dotenv, find_dotenv
import speech_recognition as sr
from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv(find_dotenv())

r = sr.Recognizer()
speech = sr.Microphone()
authenticator = IAMAuthenticator(os.environ.get("IBMAPI_KEY"))
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url(os.environ.get("IBM_URL"))

with speech as source:
    print("say something!!…")
    audio_file = r.adjust_for_ambient_noise(source)
    audio_file = r.listen(source)
speech_recognition_results = speech_to_text.recognize(audio=audio_file.get_wav_data(), content_type='audio/wav').get_result()
print(json.dumps(speech_recognition_results, indent=2))