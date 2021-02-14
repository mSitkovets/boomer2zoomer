import requests
import os
from dotenv import load_dotenv, find_dotenv

import tkinter as tk
from tkinter import *
import json

load_dotenv(find_dotenv())

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

querystring = {"term": "yeet"}

headers = {
    'x-rapidapi-key': os.environ.get("RAPIDAPI_KEY"),
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

result = json.loads(response.text)
definition=result["list"][0]["definition"]
print(definition)

# tkinter window
r = tk.Tk()
r.title("Definition")

l = Label(r, text=definition, justify=LEFT, wraplength=1000)
button = tk.Button(r, text="Close", width=20, command=r.destroy)
l.pack()
button.pack()
#add fonts, window sizing / margins

r.mainloop() #run the window