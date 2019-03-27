#!/usr/bin/env python3
import os
import time
import pyperclip


pyperclip.copy('')
print('readit start...')
while True:
    clip = pyperclip.paste()
    if clip != '':
        print(clip)
        f = open(os.path.realpath("~/")[:-1]+'tmp','w')
        f.truncate()
        f.write(clip)
        f.close()
        os.system('ekho -s 200 -r -25 -f ~/tmp')
        pyperclip.copy('')
        print('listening...')
    time.sleep(1)
