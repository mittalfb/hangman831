import random

#TODO Task 1

# Step 1: Create a list containing the names of your 5 favorite fruits and assign this list to a variable called word_list.
word_list = ['banana', 'peach', 'mango', 'kiwi', 'grapefruit']

# Step 2: Print out the newly created list to the standard output (screen).
print(word_list)


# TODO Task 2
# Step 1: Create the random.choice method and pass the word_list variable into the choice method.

def choice(wor_list):
    #Step 2: Assign the randomly generated word to a variable called word.
    word = random.choice(word_list)
    
    #Step 3: Print out word to the standard output. 
    print(word)

choice(word_list)

# TODO Task 3

#Using the input function, ask the user to enter a single letter.

guess = input("Enter a single letter: ")

# TODO Task 4

# Step 1: Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
if len(guess) == 1 and guess.isalpha():
    # Step 2: Print a message for a valid input
    print("Good guess!")
else:
    # Step 3: Print a message for an invalid input
    print("Oops! That is not a valid input.")