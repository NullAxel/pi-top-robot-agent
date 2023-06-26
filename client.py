from pynput import keyboard
import requests
from time import sleep

IP = "pi-top.local"
PORT = 9999
URI = f"http://{IP}:{PORT}"
stopped = False
keys = ["a",
        "b",
        "x",
        "y",
        keyboard.Key.up,
        keyboard.Key.down,
        keyboard.Key.left,
        keyboard.Key.right,
       ]
keys_status = {"a": False,
               "b": False,
               "x": False,
               "y": False,
               keyboard.Key.up: False,
               keyboard.Key.down: False,
               keyboard.Key.left: False,
               keyboard.Key.right: False,
              }


def on_press(key):
    try:
        k = key.char
        if k in keys:
            keys_status[k] = True
    except AttributeError:
        k = key
        if k in keys:
            keys_status[k] = True
    

def on_release(key):
    try:
        k = key.char
        if k in keys:
            keys_status[k] = False
    except AttributeError:
        k = key
        if k in keys:
            keys_status[k] = False


# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

while not stopped:
    sleep(0.15)
    if keys_status[keyboard.Key.up] == True:
        requests.get(URI + "/v2/w/0.15")
    if keys_status[keyboard.Key.down] == True:
        requests.get(URI + "/v2/s/0.15")
    if keys_status[keyboard.Key.left] == True:
        requests.get(URI + "/v2/a/0.15")
    if keys_status[keyboard.Key.right] == True:
        requests.get(URI + "/v2/d/0.15")