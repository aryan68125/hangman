import random
#import your custom module in your main program
#hangman_words.py is the module which contain wordList 
import hangman_words
#download and install art pip3 install art in your linux machine or mac osX then import art
from art import *
# importing the pyttsx library
import pyttsx3
Art=text2art("Hangman",font='block',chr_ignore=True) # Return ASCII text with block font
print(Art)
print("\n")
Art2 = text2art("game\n",font='block',chr_ignore=True)
print(Art2)
for i in range(0,1000):
    # initialisation
    engine = pyttsx3.init()
    #word_list=["baboon","aditya","aastha","computer","car","vineeta","maths"] #old lis for debugging only
    #randomly choose a word from the word_list
    #hangman_words.word_list is the syntax through which you can acsses your wordList in your hangman_word.py module
    r=int(random.randint(0,len(hangman_words.word_list)-1))
    chosen_word=hangman_words.word_list[r]
    print(chosen_word) #for debugging only
    #here we are going to create a list which will contain "_" in it
    #the number of "_" will be equal to the number of words in the chosen_word
    display = []
    for j in range(0,len(chosen_word)):
        display.append("_")
    print(display)   

    #the number of lives which will be lost on every wrongly guessed letter in a word
    lifeDisplay=6
    #here we want the user to be able to guess words until all the blanks are filled in the display list
    #so here we will use a while loop 
    #and also we are going to create a variable that will hold the state of the game
    end_of_game = False
    while not end_of_game:
        #ask the user to guess a word and assign that answer to the guess variable
        #make the guess in lowercase
        guess = input("Guess the letter => \n").lower()
        #checking if the guess is already in display list or not
        if guess in display:
            print("you have already guessed the Letter in the mystry word\n")
        #now we will loop through the chosen_word and check wheather the guessed letter is there or not in the chosen_word from the word_list
        #replace the "_" in the display list if guess is present in chosen_word 
        k=0 # index for display list
        for letter in chosen_word:
            if letter == guess:
                display[k]=guess
                k+=1
            else:
                k+=1
        print(display)
        print(f"life left in your little man ={lifeDisplay} \n")
               
        #reude the life by one if guess is not in chosen word
        if guess not in chosen_word:
            lifeDisplay-=1
            if lifeDisplay==0:
                print(f"life left in your little man ={lifeDisplay} \n")
                print("you could not save your little man. he was hung to death\n")
                print("you lose!!!!\n")
                engine.say(f"life left in your little man ={lifeDisplay}")
                engine.say("you could not save your little man. he was hung to death")
                engine.say("you lose!!!!")
                engine.runAndWait()
                end_of_game=True
        #now here we are going to check if the blanks are there in the display list or not 
        #if no then break the loop
        if "_" not in display:
            print("you manged to save your little man by guessing the correct word\n")
            print("CONGRACTULATIONS!!!!...the little man is grateful to you\n")
            print(f"life left in your little man ={lifeDisplay} \n")
            engine.say("you manged to save your little man by guessing the correct word")
            engine.say("CONGRACTULATIONS!!!!...the little man is grateful to you\n")
            engine.say(f"life left in your little man ={lifeDisplay}")
            engine.runAndWait()
            end_of_game=True
        
    q=input("Press q to quit the program or Press enter to continue\n")
    if q=='q' or q=='Q':
        program=text2art("Program") # Return ASCII text (default font) and default chr_ignore=True 
        print(program)
        print("\n")
        terminated=	text2art("Terminated")
        print(terminated)
        print("\n")
        break