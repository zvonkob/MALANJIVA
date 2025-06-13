
import math
import random


def get_range():
    while True:
        try:
            nmin = int(input('Minimal integer: '))
            nmax = int(input('Maximal integer: '))
            if nmin >= nmax:
                raise ValueError
            return nmin, nmax
        except ValueError:
            print('Please enter valid numbers.\n')
            continue


def get_max_guesses(nmin, nmax):
    nn = nmax - nmin + 1
    imax = math.log(100) / math.log(2)
    imax *= 1.20
    imax = math.ceil(imax) 
    print(f'You have {imax} guesses.')
    return imax, nn


def guess_secret_number(nmin, nmax, secret, imax):
    i = 0
    while True:
        try:
            message = f'Guess the number between {nmin} and {nmax}: '
            n = int(input(message))
            if not (nmin <= n <= nmax):
                raise ValueError
            i += 1
            if i > imax:
                print('Too many guesses!')
                print(f'The secret number was {secret}.')
                return -1
            if n < secret:
                print('Too low!')
            elif n > secret:
                print('Too high!')
            else:
                print('Congratulations! You guessed the number.')
                return i
        except ValueError:
            print('Please enter a valid number.')
            continue


def main():
    
    nmin, nmax = get_range()
    
    imax, nn = get_max_guesses(nmin, nmax)
    
    secret = random.randint(nmin, nmax)

    i_best = nn
    
    while True:
        
        i = guess_secret_number(nmin, nmax, secret, imax)
            
        if 0 < i < i_best:
            i_best = i

        print('Best score so far: {i_best}')

        cont = input('Continue? (y/n): ').lower()
        
        if cont[0] != 'y':
            break
        

if __name__ == "__main__":
    main()
