from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfile
import json
from typing import List, Dict

def save_file(data: List[Dict]):
    Tk().withdraw() 
    try:
        with asksaveasfile(mode="w", defaultextension=".json") as file:
            file.write(json.dumps(data))
    except:
        print("O processo foi cancelado")

def read_file() -> List[Dict]:
    Tk().withdraw() 
    filename = askopenfilename(defaultextension=".json")
    with open(filename, "r") as file:
        return json.loads(file.read())
    
