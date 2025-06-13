
import math
import random


def main():
    while True:
        try:
            nmin = int(input('Minimal integer: '))
            nmax = int(input('Maximal integer: '))
            if nmin >= nmax:
                raise ValueError
            break
        except ValueError:
            print('Please enter valid numbers.')
            continue
    secret = random.randint(nmin, nmax)
    while True:
        try:
            message = f'Guess the number between {nmin} and {nmax}: '
            n = int(input(message))
            if not (nmin <= n <= nmax):
                raise ValueError
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
