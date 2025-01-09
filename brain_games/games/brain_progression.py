from random import randint

from brain_games.scripts.brain_games_eng import start

DESCRIPTION = 'What number is missing in the progression?'


def create():
    number = randint(1, 100)
    step = randint(1, 100)
    qty = randint(5, 10)
    pos = randint(0, qty - 1)
    tmp_number = number

    questioin = ''
    for i in range(0, qty):
        if i == pos:
            correct = str(tmp_number)
            questioin += '..' + ' '
        else:
            questioin += str(tmp_number) + ' '
        tmp_number += step
    return questioin, correct


def main():
    start(DESCRIPTION, create)
