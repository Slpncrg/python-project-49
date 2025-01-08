from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def create():
    question = randint(1, 100)
    correct = "yes" if question % 2 == 0 else "no"
    return question, correct


if __name__ == "__main__":
	create()
