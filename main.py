import os
import sys
import time
import textwrap

# imports from ui_utils.py
from ui_utils import clear, game_over_print
import game

# Global vars
game_title = textwrap.dedent("""
.▄▄ · ▄▄▄▄▄▄▄▄ .▄▄▌ ▐ ▄▌ ▄▄▄·▪  ·▄▄▄▄      .▄▄ ·  ▐ ▄  ▄▄▄· ▄ •▄ ▄▄▄ .
▐█ ▀. •██  ▀▄.▀·██· █▌▐█▐█ ▄███ ██▪ ██     ▐█ ▀. •█▌▐█▐█ ▀█ █▌▄▌▪▀▄.▀·
▄▀▀▀█▄ ▐█.▪▐▀▀▪▄██▪▐█▐▐▌ ██▀·▐█·▐█· ▐█▌    ▄▀▀▀█▄▐█▐▐▌▄█▀▀█ ▐▀▀▄·▐▀▀▪▄
▐█▄▪▐█ ▐█▌·▐█▄▄▌▐█▌██▐█▌▐█▪·•▐█▌██. ██     ▐█▄▪▐███▐█▌▐█ ▪▐▌▐█.█▌▐█▄▄▌
 ▀▀▀▀  ▀▀▀  ▀▀▀  ▀▀▀▀ ▀▪.▀   ▀▀▀▀▀▀▀▀•      ▀▀▀▀ ▀▀ █▪ ▀  ▀ ·▀  ▀ ▀▀▀         
""")

RED = "\033[91m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def RenderUI(state=0, game_results=()):
    clear()
    width = 100
    # state: home
    if state == 0:
        clear()
        try:
            print(f"{CYAN}╔" + "═" * (width - 2) + f"╗{RESET}")
            for line in game_title.strip().splitlines():
                print(f"{CYAN}║{RESET}" + RED + line.center(width - 2) + RESET + f"{CYAN}║{RESET}")
            print(f"{CYAN}╠" + "═" * (width - 2) + f"╣{RESET}")
            
            prompt_box = f" [?] When ever you are Ready -> "
            print(f"{CYAN}║{RESET}" + prompt_box.ljust(width - 2) + f"{CYAN}║{RESET}")
            print(f"{CYAN}╚" + "═" * (width - 2) + f"╝{RESET}")

            try:
                print("\033[A\033[A", end="")
                print(f"{CYAN}║{RESET}" + f" {GREEN}[?] When ever you are Ready ->{RESET} ", end="")
                userInp = input().lower().strip()
            except KeyboardInterrupt:
                print(f"\n\n{RED}Byee . . .{RESET}")
                sys.exit()
                
            game_over_print(score=(0, 0, 'Too Lazy To Input Anything . . . ')) if not userInp else None
            sys.exit() if userInp.lower().strip() in 'nnonooqquitnah' else None
            state = 2
            
            print(f"{CYAN}╔" + "═" * (width - 2) + f"╗{RESET}")
            print(f"{CYAN}║{RESET}" + f"{YELLOW} Starting Game... Please Wait...{RESET}".center(width + 8) + f"{CYAN}║{RESET}")
            print(f"{CYAN}╚" + "═" * (width - 2) + f"╝{RESET}")
            time.sleep(0.5)

        except Exception as e:
            print(f'{RED}Error in state 0{RESET}', e)

    # state gameover
    if state == 1:
        clear()
        try:
            print(f"{RED}╔" + "═" * (width - 2) + f"╗{RESET}")
            game_over_print(game_results)
            print(f"{RED}╚" + "═" * (width - 2) + f"╝{RESET}")

        except Exception as e:
            print(f'{RED}Error in state 1{RESET}', e)

    # state game(running)
    if state == 2:
        clear()
        game.main()

if __name__ == '__main__':
    RenderUI()