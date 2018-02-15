import random
guessTaken = 0
number = random.randint(0, 10)
while guessTaken < 11:
        print('Guess the number between 0 and 10')
        guess = input()
        guess = int(guess)
        guessTaken = guessTaken + 1
        if guess != number:
                print ('Your guess is wrong. Try again')
        if guess == number:
                print('You have guess correctly.')
                break


