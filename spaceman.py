import random

answerlist = ["fruit", "candy", "pizza", "butter", "cake", "pastry"]

random.shuffle(answerlist)

answer = list(answerlist[0])

display = []
used = []
display.extend(answer)
# used.extend(display)



for i in range(len(display)):
    display[i] = "_"
print(' '.join(display))
print()

print("CONGATS YOU PLAYED SPACEMAN!")


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