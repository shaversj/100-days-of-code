"""
The idea here is to capture whatever the user copies to the clipboard (think CTRL C) and "store" it in some way such that the user can see the history of everything they've copied for later reference.

https://pybit.es/codechallenge54.html
"""

import pyperclip
import datetime

clip_board = []
count = 0
while True:
    answer = input(
        'Enter [Y] to copy contents.\nEnter [N] to print history.\nEnter [B] to break.\n Enter your answer[Y], [N] or [B]: '"")
    if answer == 'Y':
        count += 1
        d = datetime.datetime.now()
        d = d.strftime("%Y-%m-%d %H:%M")
        copy = pyperclip.paste()
        clip_board.append([d, copy])
    elif answer == 'N':
        for num, value in enumerate(clip_board):
            print(f'{num}: Date: {value[0]} Content: {value[1]}')
    elif answer == 'B':
        print()
        print('Good Bye!')
        print()
        break
