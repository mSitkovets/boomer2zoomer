import requests
import os
from dotenv import load_dotenv, find_dotenv

import tkinter as tk
from tkinter import *
import json

load_dotenv(find_dotenv())

def pop_up_window(definition, term=None):
    print('tkinter', definition)
    # tkinter window
    r = tk.Tk()
    r.title("Definition")

    t = Label(r, text=term, justify=LEFT, wraplength=1000)
    l = Label(r, text=definition, justify=LEFT, wraplength=1000)
    button = tk.Button(r, text="Close", width=20, command=r.destroy)
    t.pack()
    l.pack()
    button.pack()
    tk.mainloop()

def get_urban_meaning(term):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

    querystring = {"term": term}

    headers = {
        'x-rapidapi-key': os.environ.get("RAPIDAPI_KEY"),
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    result = json.loads(response.text)
    definition=result["list"][0]["definition"]
    pop_up_window(definition, term)

