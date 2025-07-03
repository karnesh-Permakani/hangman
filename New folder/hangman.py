import random
import word
import graph
stages=graph.stages
s=word.word_list
lo=graph.logo
print(lo)
randomChosenString = random.choice(s)
chosenStringCount=len(randomChosenString)
print(f"Find the animal or bird name it contain {chosenStringCount} words")



#print(string)

end_game= False
lives=6

string=[]
for chosenLetter in range(chosenStringCount):
    string +='_'
print(string)

while (end_game!=False):
    guessChar=input("\nenter the gusses letter:")
    for chosenLetter in range(chosenStringCount):
       letter=randomChosenString[chosenLetter]
       #print(f"Current position: {l}\n Current letter: {letter}\n Guessed letter: {guss}")
       if guessChar==letter:
          string[chosenLetter]=letter
    

    if guessChar not in randomChosenString:
        lives-=1
        if lives==0:
            end_game=True
            print("you lose.")

    print(f"{' '.join(string)}")        

    if '_' not in string:
        end_game=True
        print("you win")

    print(stages[lives])
print(f'Pssst, the solution is {randomChosenString}.')