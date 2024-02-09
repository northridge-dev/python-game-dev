import os

BANNER = """
 __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.
|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |
|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |
|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |
|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |
|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|

                                      +---+
                                      |   |
                                      O   |
                                     /|\  |
                                     / \  |
                                       =====

"""

zero_misses = """
  +---+
      |
      |
      |
    ====="""


one_misses = """
  +---+
  O   |
      |
      |
    ====="""

two_misses = """
  +---+
  O   |
  |   |
      |
    ====="""

three_misses = """
  +---+
  O   |
 /|   |
      |
    ====="""

four_misses = """
  +---+
  O   |
 /|\  |
      |
    ====="""

five_misses = """
  +---+
  O   |
 /|\  |
 /    |
    ====="""

game_over = """
  +---+
  O   |
 /|\  |
 / \  |
    ====="""

HANGMAN_PICS = [
    zero_misses,
    one_misses,
    two_misses,
    three_misses,
    four_misses,
    five_misses,
    game_over,
]


def print_title():
    _, terminal_height = os.get_terminal_size()

    banner_height = BANNER.count("\n") + 1
    padding = (terminal_height - banner_height) // 2

    os.system("clear")
    print("\n" * padding)
    print(BANNER)
    print("\n" * padding)
