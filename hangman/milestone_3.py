randomly_chosen_word = "mango"

# Step 1: Create a while loop and set the condition to True. Setting the condition to True ensures that the code runs continuously.

while True:
    # Step 2: Ask the user to guess a letter and assign this to a variable called guess.
    guess = input("Guess a letter: ")

    # Step 3: Check that the guess is a single alphabetical character.
    if len(guess) == 1 and guess.isalpha():
        
        # Step 1: Create an if statement that checks if the guess is in the word
        if guess in randomly_chosen_word:
            
            # Step 2: Print "Good guess", if the letter is in the randomly selected word
            print(f"Good guess! '{guess}' is in the word.")
        else:
            
            # Step 3: If not true, print "Sorry guess is not in word"
            print(f"Sorry, '{guess}' is not in the word. Try again.")
        # Step 4:If the guess passes the checks, break out of the loop.
        break
    
    else:
        # Step 5: If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."
        print("Invalid letter. Please, enter a single alphabetical character.")
        



