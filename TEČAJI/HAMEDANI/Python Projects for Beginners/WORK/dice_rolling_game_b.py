
import random


def main():
    n = int(input('How many dice do you want to roll? '))
    while True:
        roll = input('Roll the dice? (yes/no): ').lower()
        if roll == 'y':
            iii = '('
            for x in range(n):
                i = random.randint(1, 6)
                iii += f'{i}, '
            iii = iii[:-2]
            iii += ')'
            print(iii)
        elif roll == 'n':
            print('Thanks for playing!')
            break
        else:
            print('Invalid choice!')


if __name__ == "__main__":
    main()
