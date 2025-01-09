from random import randint

from brain_games.scripts.brain_games_eng import start

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def create():
    question = randint(1, 100)
    correct = "yes" if question % 2 == 0 else "no"
    return question, correct


def main():
    start(DESCRIPTION, create)
