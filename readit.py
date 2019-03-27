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
        f = open('tmp','w')
        f.truncate()
        f.write(clip)
        f.close()
        os.system('bash readtmp.sh')
        pyperclip.copy('')
        print('listening...')
    time.sleep(1)
