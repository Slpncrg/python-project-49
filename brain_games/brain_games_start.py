import prompt


def start():    
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def main():
    start()


if __name__ == "__main__":
	main()