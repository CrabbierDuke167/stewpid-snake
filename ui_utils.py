# function definitions for various ui elements and processes
import time, sys, os, textwrap

# vars
CYAN = "\033[96m"
WHITE = "\033[97m"
BLUE = "\033[94m"
RESET = "\033[0m"

# cls fn
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# print game over text and quit program
def game_over_print(score=(), delay=0.001):
    width = 100
    game_over = textwrap.dedent("""
    ┏┓┏┓┳┳┓┏┓  ┏┓┓┏┏┓┳┓
    ┃┓┣┫┃┃┃┣   ┃┃┃┃┣ ┣┫
    ┗┛┛┗┛ ┗┗┛  ┗┛┗┛┗┛┛┗
    """)

    print(CYAN + game_over + RESET)

    format_ = (
        f"{WHITE}SCORE:{RESET} {score[0]}\n"
        f"{WHITE}BEST RUN:{RESET} {score[1]}\n"
        f"{BLUE}CAUSE OF DEATH:{RESET} {score[-1]}\n"
        f'\n"python main.py" to restart the game\n\n'
        f"{'━' * width}"
    )

    print(format_)
    sys.exit()

