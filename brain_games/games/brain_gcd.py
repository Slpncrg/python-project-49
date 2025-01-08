from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def create():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    
    temp_num1 = num1
    temp_num2 = num2

    k = 1
    while temp_num1 != 0 and temp_num2 != 0:
        while temp_num1 % 2 == 0 and temp_num2 % 2 == 0:
            temp_num1 //= 2
            temp_num2 //= 2
            k *= 2
        while temp_num1 % 2 == 0: 
            temp_num1 //= 2
        while temp_num2 % 2 == 0: 
            temp_num2 //= 2
        if temp_num1 >= temp_num2: 
            temp_num1 -= temp_num2
        else: 
            temp_num2 -= temp_num1
    correct = str(temp_num2 * k)
    
    return str(f"{num1} {num2}"), correct


if __name__ == "__main__":
	create()
