Datheon Python Programming Internship

This repository contains my Python internship tasks for Datheon

Task 1: Hangman Word Guessing Game
Stores a random word from list of words
User is given 6 attempts to answer correctly
If the user guessed right it displays the victory 
If the user lost it shows on the display
  
Task 2: Stock Performance Tracker
Allows the user to enter data
Computes the loss/gain
saves data to a file

Task 3: Chatbot

Loads FAQ's from the json file using os.path.dirname so it works anywhere
Removes spaces and converts every user's input into lowercase (normalization)
Groups similar words as a pattern using regex \b(hours|open)\b
Checks for keywords on the user input and matches with the corresponding FAQ using re.findall
Notifies the user when there is no keyword - fallback handling
