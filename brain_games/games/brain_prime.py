from math import sqrt
from random import randint

from brain_games.scripts.brain_games_eng import start

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def create():
    num = randint(1, 100)
    i = 2
    while i <= sqrt(num):
        if num % i == 0:
            return num, "no"
        i += 1
    return num, "yes"


def main():
    start(DESCRIPTION, create)
