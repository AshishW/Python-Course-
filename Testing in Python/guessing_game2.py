from random import randint
import sys
# generate a number 1~10
answer = randint(1, 10)

# input from user?
# check that input is a number 1~10
def guessed_correctly(guess, answer):
    try:
        if  0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                return True
        else:
            print('hey bozo, I said 1~10')
            return False
    except:
        return False
if __name__ == '__main__':
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            # if  0 < guess < 11:
            #     if guess == answer:
            #         print('you are a genius!')
            #         break
            # else:
            right_guess = guessed_correctly(guess, answer)
            if(right_guess):
                break
        except ValueError:
            print('please enter a number')
            continue