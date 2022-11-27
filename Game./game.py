import random

points = 0
maxRange = 1
print("Welcome to the guessing game!\nDuring the play, every turn you have to choose a number.\nThe range of this number will keep increasing as the game proceeds further.\nYou will get points based on how close you were to the answer!\nLet's Begin.\n")
keepPlaying  = 1
while(keepPlaying):
    maxRange = maxRange * 10
    randNum = random.randint(0,maxRange)
    guess = int(input("Guess a number! "))
    print("Number was {}.\n".format(randNum))
    if guess == randNum: points = points + guess
    elif randNum > guess/2 and randNum < 3*guess/2 : points = points + guess/2
    print("You now have {} points.".format(points))
    keepPlaying = int(input("Would you like to keep playing?")) 
    print('\n')

print("You have cashed out with {} points.".format(points))