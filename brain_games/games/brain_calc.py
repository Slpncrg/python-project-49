import sys

sys.path.insert(0, '/home/user/python-project-49/brain_games')
from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'

def create():
    operations = ['+', '-', '*']
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    operation = choice(operations)

    question = f"{number1} {operation} {number2}"
    correct = str(eval(question))
    return question, correct


if __name__ == "__main__":
	create()
