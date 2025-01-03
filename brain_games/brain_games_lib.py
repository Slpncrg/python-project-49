import prompt


def start():    
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def lose_text(answer, corrected, name):
    print(f"'{answer}' is wrong answer ;(. "
          f"Correct answer was '{corrected}'.")
    print(f"Let's try again, {name}!")


def get_answer(question):
    return prompt.string(f'Question: {question}\nYour answer: ')
     

def main():
    start()


if __name__ == "__main__":
	main()