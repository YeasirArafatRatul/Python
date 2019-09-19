import random


print("\t***WELCOME***")
print("\n\tGuess The Number Between 0 to 10:")
print("\n\tPress Q To Quit:")
score = 0


while True:
    randomnum = random.randint(0,10)
    guess = input("Number:")
    if guess == 'Q':
        print("\tGame Over")
        break
    if int(guess)== randomnum:
        score += 10
        print("\nscore:",score)
    else:
        print("wrong guess")
        print("The number was:",randomnum)
        print("Try again:")
