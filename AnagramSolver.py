##################################################
## GamePigeon Anagram Solver:
## A player can enter 6 letters in the interactive window, then the program would show the words found
##################################################
## Author: Ting-Han Lin
## Copyright: Copyright 2021, GamePigeon Anagram Solver
## Credits: [Raghav Gurung (https://medium.com/python-anagram-solver/python-anagram-solver-edb2646b65f8)]
## Version: 1.0.0
## Maintainer: Ting-Han Lin
## Email: tinghan@uchicago.edu
## Status: Complete
##################################################

#import modules
import pandas as pd
from collections import Counter
from tkinter import *
import textwrap


#import the all of the words, the longest word is 15 characters
dictionary = pd.read_excel('Collins Scrabble Words (2019).xlsx')

#for GamePigeon Anagram, a players has to make words from 6 letters
#and each word has to be longer than 3 letters
#so we get rid of 2 letter words and 6+ words
result_dictionary = dictionary[dictionary['List of Words'].str.len() > 2]
result_dictionary = result_dictionary[result_dictionary['List of Words'].str.len() < 7]

#convert the words from a dataframe to series
word_series=result_dictionary.squeeze()

#mystring should be a 6 character string, which is all uppercased
def searchWords(mystring, word_series):
    #declare an empty list where we put the formable words
    output = []

    #separate the 6 character string, and count the occurrence of each letter
    myletters = list(mystring)
    letters_count = Counter(myletters)

    #check if a word in dictionary can be formed with the given letters
    #reference from https://medium.com/python-anagram-solver/python-anagram-solver-edb2646b65f8
    for word in word_series:
        if not(set(list(word)) - set(myletters)):
            word_count = Counter(word)
            word_set = set()
            for key, value in Counter(word).items():
                if value <= letters_count[key]:
                    word_set.add(key)
                if word_set == set(list(word)):
                    output.append(word)
                    
    output.sort() #sorts by alphabetical order
    output.sort(key=len, reverse=True) #sorts by descending length
    return output

#convert list to string
def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))

#click event
def myClick():
    userInput = ent.get()
    
    if (userInput.isalpha() == False) or (len(userInput) > 6 or len(userInput) < 6):
        message['text'] = "Please enter 6 letters!"
    else:
        userInput = userInput.upper()
        answer=searchWords(userInput, word_series)
        
        if len(answer) == 0: 
            message['text'] = "No word is found!"
        else:
            answer = listToString(answer)
            message['text'] = textwrap.fill(answer, width=60)

#initialize an interactive window using tkinter
root= Tk()
root.geometry("600x450")  
root.title('Anagram Solver')  

instruct = Label(root, text = "Please enter 6 letters in the box below!")
instruct.pack() 
    
ent = Entry(root, width=50, bd=10)
ent.pack()    
    
myButton = Button(root, text="Enter 6 Letters", command = myClick)
myButton.pack()

message = Label(root, text = "")
message.pack() 

root.mainloop()

