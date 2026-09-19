import os
import sys
import time
import textwrap

# imports from ui_utils.py
from ui_utils import clear, game_over_print

# Global vars
game_title = textwrap.dedent("""
▄▄─▄ ▄▄   ▄▄─▄ ▄▄   ▄ ▄▄─▄ ▄▄    ▄      ▄▄─▄ ▄▄─▄ ▄▄─▄ ▄▄ ▄ ▄▄─▄
▀▀─▄ ▄█─  ▄█─▀ ▄█ █ █ ▄█─▀ ▄▄ ▄▄─█      ▀▀─▄ ▄█ █ ▄▄─█ ▄█─▄ ▄█─▀
██ █ ██ █ ██ █ ██ █ █ ██   ██ ▄█ █      ██ █ ██ █ ██ █ ██ █ ██ █
▀▀─▀ ▀▀─▀ ▀▀─▀ ▀▀─▀─▀ ▀▀   ▀▀ ▀▀─▀      ▀▀─▀ ▀▀ ▀ ▀▀─▀ ▀▀ ▀ ▀▀─▀
""")

RED = "\033[91m"
RESET = "\033[0m"




def RenderUI(state=0):
    clear()
    width = 90
    # state: home
    if state == 0:
        clear()
        try:
            print('━' * width)
            for line in game_title.strip().splitlines():
                print(RED+line.center(width)+RESET)
            print('━' * width + "\n\n")

            userInp = input("When ever you are Ready -> ")
            game_over_print(score=(0, 0, 'Too Lazy To Input Anything . . . ')) if not userInp else None
            print('━' * width)

        except Exception as e:
            print('Error in state 0', e)


    # state gameover
    if state == 1:
        clear()
        try:
            print('━' * width)
            game_over_print()
            print('━' * width)

        except Exception as e:
            print('Error in state 1', e)


    # state game(running)
    if state == 2:
        clear()
        



if __name__ == '__main__':
    RenderUI()