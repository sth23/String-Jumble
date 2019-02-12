"""
stringjumble.py
Author: Sean Healey
Credit: Tutorials, Stack Overflow

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""

# Get user input
original = input("Please enter a string of text (the bigger the better): ")
print('You entered "' + original + '". Now jumble it:')

# Create list of letters and list of words
letters_list = list(original)
words_list = original.split()

# Reverse order of all characters in string
reverse_letters = letters_list[::-1]
print(''.join(reverse_letters))

# Reverse order of words in string
reverse_words = words_list[::-1]
print(' '.join(reverse_words))

# Reverse order of letters within words, but leave words in order
reverse_words_letters = [len(words_list)]
for i in range(0,len(words_list)):
    reverse_words_letters[i] = words_list[i][::-1]
print(' '.join(reverse_words_letters))