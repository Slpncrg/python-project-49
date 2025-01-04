import prompt


def start(game):    
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.DESCRIPTION)
    for i in range(0, 3):
        (question, correct) = game.create()
        answer = prompt.string(f'Question: {question}\nYour answer: ')
        if answer.lower() == correct:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")  


if __name__ == "__main__":
	start()