
import random


def main():
    while True:
        roll = input('Roll the dice? (yes/no): ').lower()
        if roll == 'y':
            i1 = random.randint(1, 6)
            i2 = random.randint(1, 6)
            print(f'({i1}, {i2})')
        elif roll == 'n':
            print('Thanks for playing!')
            break
        else:
            print('Invalid choice!')


if __name__ == "__main__":
    main()
