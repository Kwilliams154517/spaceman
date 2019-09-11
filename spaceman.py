from random import shuffle

answerlist = ["fruit", "candy", "pizza", "butter", "cake", "pastry", "icecream","ramen"]

shuffle(answerlist)

answer = list(answerlist[0])

display = []
used = []
# .extend allows len of list to be updated no matter how many times the list itself is updated with new words or new word being taken away 
display.extend(answer)
used.extend(display)



for i in range(len(display)):
    display[i] = "_"
print(' '.join(display))
print()
print(str(len(answer)) + " = number of letters in each word")
print()

print("WELCOME TO SPACEMAN!")
print("Theme: Food")

count = 0 

while count < len(answer):
    guess = input("Please guess a letter: ")
    guess = guess.lower()
    print(count)
    
    for i in range(len(answer)):
        if answer[i] == guess and guess in used :
            display[i] = guess
            count = count + 1 
            
            
            used.remove(guess)
    
    if guess not in display:
        print("Sorry, wrong guess")
    
    print("you have guessed: ",count,"correct letters.")
    
    print(' '.join(display))
    print()
    
print("CONGRATS YOU WIN!")
print("Wanna play again? Type python3 spaceman.py")

