from math import sqrt
from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def create():
    num = randint(1, 100)
    i = 2
    while i <= sqrt(num):
        if num % i == 0:
            return num, "no"
        i += 1
    return num, "yes"


if __name__ == "__main__":
	create()
