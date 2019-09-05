import random

answerlist = ["fruit", "candy", "pizza", "butter", "cake", "pastry", "icecream","ramen"]
# let _ _ _ _ _ tell how many letters are in each word
# make sure the number_of_letter_per_word match the index of each word chosen at random
random.shuffle(answerlist)

answer = list(answerlist[0])

display = []
used = []
display.extend(answer)
used.extend(display)



for i in range(len(display)):
    display[i] = "_"
print(' '.join(display))
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
# make restart happen on its own 