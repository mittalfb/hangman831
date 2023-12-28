import random

#Create a list containing the names of your 5 favorite fruits and assign this list to a variable called word_list.
word_list = ['banana', 'peach', 'mango', 'kiwi', 'grapefruit']

#Print out the newly created list to the standard output (screen).
print(word_list)

#Create the random.choice method and pass the word_list variable into the choice method.

def choice(wor_list):
    #Assign the randomly generated word to a variable called word.
    word = random.choice(word_list)
    
    #Print out word to the standard output. 
    print(word)

choice(word_list)


    