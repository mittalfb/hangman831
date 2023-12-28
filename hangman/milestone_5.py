import random
class Hangman:
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word)
        self.list_of_guesses = []
 
    def check_guess(self,guess):
        #Convert the guessed letter to lower case
        guess = guess.lower()

        #Create an if statement that checks if the guess is in the word
        if guess in self.word:
            #in the body of the if statement, print a message saying "Good guess! {guess} is in the word."
            print(f"Good guess! '{guess}' is in the word.")
            
            #in the if block, replace the corresponding "_" in the word_guessed with the guess
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess

                    
            #Outside the for-loop, reduce the variable num_letters by 1
            self.num_letters -= 1 
            
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
       #Create a while loop and set the condition to True
        while True:
            #Ask the user to guess a letter and assign this to a variable called guess
            guess = input('guess a letter: ')

            #Create an if statement that runs if the guess is NOT a single alphabetical character
            if not guess.isalpha() or len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character.')

            #Create an elif statement that checks if the guess is already in the list_of_guesses
            elif guess in self.list_of_guesses:
                #In the body of the elif statement, print a message saying "You already tried that letter!"
                print("You already tried that letter!")

            else:
                # Call check_guess method
                self.check_guess(guess)
                
                # Append guess to list_of_guesses
                self.list_of_guesses.append(guess)  
                
                # Break out of the loop after a valid guess
                break  


    # TODO Create a function called play_game that takes word_list as a parameter
    def play_game(self):
        
        #Create a variable called num_lives and assign it to 5
        num_lives = self.num_lives
        
        #Create an instance of the Hangman class.
        game = Hangman(word_list, num_lives)

        #Create a while loop and set the condition to True
        while True:
            #Check if the num_lives is 0. If it is, that means the game has ended and the user lost. Print a message saying 'You lost!'
            if game.num_lives == 0:
                print('You lost!')
                break
            
            #check if the num_letters is greater than 0. In this case, to continue the game, call the ask_for_input method.
            elif self.num_letters > 0:
                self.ask_for_input()
            else:
                #If the num_lives is not 0 and the num_letters is not greater than 0, that means the user has won the game. Print a message saying 'Congratulations. You won the game!'
                print('Congratulations. You won the game!')
                break


word_list = ['banana', 'mango', 'peach', 'kiwi', 'grapefruit']

game = Hangman(word_list, 5)
game.play_game()
