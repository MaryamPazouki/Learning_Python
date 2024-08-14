import random, stdio

Range = 10
secret = random.randrange(1, Range + 1)

guess = 0

while secret != guess:
    print('what is your guess')
    guess = stdio.readint()
    if guess < secret:
        print('too low')
    elif guess > secret:
        print('too high')
    else:
        print('you win')
