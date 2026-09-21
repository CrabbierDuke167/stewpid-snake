# Game logic from FreeCodeCamp.org

import sys
import time
import random
import shutil
import msvcrt

from main import RenderUI

CYAN = "\033[96m"
BLUE = "\033[94m"
WHITE = "\033[97m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"
HOME = "\033[H"
CLEAR = "\033[2J"


def get_terminal_size():
    width, height = shutil.get_terminal_size()
    width -= 2
    height -= 4
    return max(width, 30), max(height, 10)


def setup_terminal():
    sys.stdout.write(HIDE_CURSOR)
    sys.stdout.write(CLEAR)
    sys.stdout.write(HOME)
    sys.stdout.flush()


def restore_terminal():
    sys.stdout.write(SHOW_CURSOR)
    sys.stdout.write(RESET)
    sys.stdout.flush()


def spawn_food(snake, width, height):
    while True:
        food = (
            random.randint(1, width - 2),
            random.randint(1, height - 2)
        )
        if food not in snake:
            return food


def handle_input(direction):
    while msvcrt.kbhit():
        key = msvcrt.getch()

        if key in (b"\x00", b"\xe0"):
            key = msvcrt.getch()

            if key == b"H" and direction != (0, 1):
                direction = (0, -1)
            elif key == b"P" and direction != (0, -1):
                direction = (0, 1)
            elif key == b"K" and direction != (1, 0):
                direction = (-1, 0)
            elif key == b"M" and direction != (-1, 0):
                direction = (1, 0)
        else:
            key = key.decode(errors="ignore").lower()

            if key == "w" and direction != (0, 1):
                direction = (0, -1)
            elif key == "s" and direction != (0, -1):
                direction = (0, 1)
            elif key == "a" and direction != (1, 0):
                direction = (-1, 0)
            elif key == "d" and direction != (-1, 0):
                direction = (1, 0)

    return direction


def render(snake, food, width, height, score_value):
    screen = [[" " for _ in range(width)] for _ in range(height)]

    for x in range(width):
        screen[0][x] = "━"
        screen[height - 1][x] = "━"

    for y in range(height):
        screen[y][0] = "┃"
        screen[y][width - 1] = "┃"

    screen[0][0] = "┏"
    screen[0][width - 1] = "┓"
    screen[height - 1][0] = "┗"
    screen[height - 1][width - 1] = "┛"

    fx, fy = food
    screen[fy][fx] = "F"

    for index, (x, y) in enumerate(snake):
        if index == 0:
            screen[y][x] = "H"
        else:
            screen[y][x] = "B"

    output = []
    output.append(f"{CYAN} SCORE {WHITE}{score_value:04d}{CYAN}   STEWPID SNAKE{RESET}")

    for row in screen:
        line = ""
        for char in row:
            if char in ("━", "┃"):
                line += f"{BLUE}{char}{RESET}"
            elif char in ("┏", "┓", "┗", "┛"):
                line += f"{CYAN}{char}{RESET}"
            elif char == "F":
                line += f"{YELLOW}█{RESET}"
            elif char == "H":
                line += f"{CYAN}█{RESET}"
            elif char == "B":
                line += f"{BLUE}█{RESET}"
            else:
                line += char
        output.append(line)

    sys.stdout.write(HOME)
    for line in output:
        sys.stdout.write(line + "\033[K\n")
    sys.stdout.flush()


WALL_DEATH_MESSAGES = [
    "Skill issue. Unbelievable skill issue.",
    "You became one with the wall.",
    "Reflexes of a turtle.",
    "That corner looked closer than it was.",
    "Did your cat walk across the keyboard?",
    "The boundary has claimed another victim.",
    "Wall: 1 | Snake: 0.",
]

SELF_DEATH_MESSAGES = [
    "You ate yourself. Impressive.",
    "The snake has discovered cannibalism.",
    "Cannibalism ain't it, chief.",
    "You turned too hard on yourself.",
    "Snake encountered its own body.",
    "Stop eating yourself, you weirdo.",
    "A tragic case of self-collision.",
]


def on_loose(game_result):
    game_result_tuple = list(game_result)

    try:
        with open('score.csv', 'r') as f:
            high_score = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        high_score = game_result_tuple[0]

    if game_result_tuple[0] > high_score:
        high_score = game_result_tuple[0]
        try:
            with open('score.csv', 'w') as f:
                f.write(str(high_score))
        except OSError:
            pass

    game_result_tuple.insert(1, high_score)
    RenderUI(game_results=game_result_tuple, state=1)


def main():
    width, height = get_terminal_size()

    snake = [
        (width // 2, height // 2),
        (width // 2 - 1, height // 2),
        (width // 2 - 2, height // 2)
    ]

    direction = (1, 0)
    food = spawn_food(snake, width, height)
    score_value = 0

    setup_terminal()

    try:
        render(snake, food, width, height, score_value)

        while True:
            direction = handle_input(direction)

            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])

            if (
                new_head[0] <= 0
                or new_head[0] >= width - 1
                or new_head[1] <= 0
                or new_head[1] >= height - 1
            ):
                cause_of_death = random.choice(WALL_DEATH_MESSAGES)
                game_result = (score_value, cause_of_death)
                on_loose(game_result)
                break

            if new_head in snake:
                cause_of_death = random.choice(SELF_DEATH_MESSAGES)
                game_result = (score_value, cause_of_death)
                on_loose(game_result)
                break

            snake.insert(0, new_head)

            if new_head == food:
                score_value += 1
                food = spawn_food(snake, width, height)
            else:
                snake.pop()

            render(snake, food, width, height, score_value)
            time.sleep(0.075)

    finally:
        restore_terminal()