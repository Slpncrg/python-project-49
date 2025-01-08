from operator import add, mul, sub
from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'
OPERATIONS = {'+': add, 
              '-': sub,
              '*': mul
            }


def create():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    operation_key = choice(list(OPERATIONS.keys()))
    question = f"{number1} {operation_key} {number2}"
    correct = f"{OPERATIONS[operation_key](number1, number2)}"
    return question, correct


if __name__ == "__main__":
	create()
