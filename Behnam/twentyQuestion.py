import sys
import random
# import stdio

n = 20
number = random.randint(1, 1000000)
print(number)
print("I'm thinking for a number between 1 to 1000000 can you find it?")
for i in range(n):
    print("what is your guest? %d" %i)
    guess = int(input())
    if guess > number:
        print("too high")
    elif guess < number:
        print("too low")
    elif guess == number:
        print("You win")
        break
if i == n:
    print("You lose")