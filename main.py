import random
import ascii_art as aa
import words_list as wl

#Print the hangman logo onto the screen
print(aa.logo)
#Initial game status False - Not Over
game_status = False
#Number of lives available initially 
lives = len(aa.stages) - 1

#Pick a random word from the words list
random_word = random.choice(wl.word_list)
word_length = len(random_word)

#List to store the guessed words
display = []
for _ in range(word_length):
    display.append('_')
    
#Run the loop until the game status is not True
while not game_status:
    guess = input("Guess a letter: ").lower()
    
    #Clear the console screen
    wl.cls()
    
    #If the character is already guessed by the user
    if guess in display:
        print(f"You have already guessed {guess}")
     
    #If the word guessed by the user is in the chosen word then replace the space with the letter   
    for position in range(word_length):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    
    #If the letter guessed by the user is not in the chosen word then decrement the lives by 1
    if guess not in random_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_status = True
            print("You Lose.")
            print("The correct word was : " + random_word)
    
    #Check whether all the spaces are filled or not to update the game status      
    if not "_" in display:
        game_status = True
        print("You Win.")
    
    #Print the current status of the game using the ascii art of the hangman
    print(aa.stages[lives])