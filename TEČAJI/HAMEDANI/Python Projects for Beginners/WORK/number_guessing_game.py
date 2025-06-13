
import random


def main():
    secret = random.randint(1, 100)
    while True:
        try:
            n = int(input('Guess the number between 1 and 100: '))
            if not (1 <= n <= 100):
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
