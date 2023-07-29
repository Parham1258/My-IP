# My IP
vercel = False
import os
from flask import Flask, request, make_response
if not vercel: from waitress import serve

def clear_console(): #Credits: Doci Team
    if os.name in ["nt", "dos"]: #Check OS Name
        try: os.system("cls")
        except: pass
    else:
        try: os.system("clear")
        except: pass
    return

def change_title(title: str): #Credits: Doci Team
    if os.name in ["nt", "dos"]: #Check OS Name
        try: os.system("title "+title)
        except: pass
    return

class color: #Credits: Doci Team
    Red = "\033[91m"
    Green = "\033[92m"
    Blue = "\033[94m"
    Cyan = "\033[96m"
    White = "\033[97m"
    Yellow = "\033[93m"
    Magenta = "\033[95m"
    Grey = "\033[90m"
    Black = "\033[90m"
    Default = "\033[99m"

change_title("My IP")
clear_console()

app = Flask("My IP", template_folder="Templates")
@app.route("/api")
def API():
    resp = make_response(request.remote_addr)
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp, 200
if not vercel: serve(app, host="0.0.0.0", port=80)