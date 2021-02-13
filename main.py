import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

querystring = {"term":"wat"}

headers = {
    'x-rapidapi-key': os.environ.get("RAPIDAPI_KEY"),
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

