import sys

sys.path.insert(0, '/home/user/python-project-49/brain_games')
import brain_games_lib
import games.brain_calc as calc


def main():
    brain_games_lib.start(calc)


if __name__ == "__main__":
	main()

    