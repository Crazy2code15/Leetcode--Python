import random
randNumber = random.randint(1, 100)
# print(randNumber)
userGuess = None
guesses=0

while(userGuess!=randNumber):
    userGuess = int(input('Enter your guess:'))
    guesses+=1
    if(userGuess==randNumber):
        print("guessed right!")
    else:
        if(userGuess>randNumber):
            print('guessed wrong! enter a smaller number')
        else:
            print('guessed wrong! enter a larger number')
   
    
print(f"you guessed the number in {guesses} guesses")
with open("score.txt","r") as f:
    score = int(f.read())

if (guesses < score):
    print("you have just broken the high score!")
    with open("score.txt","w") as f:
        f.write(str(guesses))