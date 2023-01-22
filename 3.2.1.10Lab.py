'''
Estimated time
10-20 minutes

Level of difficulty
Easy

Objectives
Familiarize the student with:

using the continue statement in loops;
reflecting real-life situations in computer code.
Scenario
The continue statement is used to skip the current block and move ahead to the next iteration, without executing the statements inside the loop.

It can be used with both the while and for loops.

Your task here is very special: you must design a vowel eater! Write a program that uses:

a for loop;
the concept of conditional execution (if-elif-else)
the continue statement.
Your program must:

ask the user to enter a word;
use user_word = user_word.upper() to convert the word entered by the user to upper case;
we'll talk about the so-called string methods and the upper() method very soon - don't worry;
use conditional execution and the continue statement to "eat" the following vowels
A, E, I, O, U from the inputted word;
print the uneaten letters to the screen, each one of them on a separate line.
Test your program with the data we've provided for you.


Test data
Sample input: Gregory

Expected output:

G
R
G
R
Y

'''
# solution 

user_word = input("Enter a word: ").upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)

    
