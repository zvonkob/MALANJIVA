
import math
import random


def main():
    secret = random.randint(1, 100)
    imax = math.log(100) / math.log(2)
    imax = math.ceil(imax) 
    print(f'You have {imax} guesses.')
    i = 0
    while True:
        try:
            message = f'Guess the number between 1 and 100: '
            n = int(input(message))
            if not (1 <= n <= 100):
                raise ValueError
            i += 1
            if i > imax:
                print('Too many guesses!')
                print(f'The secret number was {secret}.')
                break
            if n < secret:
                print('Too low!')
            elif n > secret:
                print('Too high!')
            else:
                print('Congratulations! You guessed the number.')
                break
        except ValueError:
            print('Please enter a valid number.')
            continue


if __name__ == "__main__":
    main()
