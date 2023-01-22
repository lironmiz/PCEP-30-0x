'''
Estimated time
5-10 minutes

Level of difficulty
Very Easy

Objectives
becoming familiar with the the input() function;
becoming familiar with comparison operators in Python.
Scenario
Using one of the comparison operators in Python, write a simple two-line program
that takes the parameter n as input, which is an integer, and prints False if n is
less than 100, and True if n is greater than or equal to 100.

Don't create any if blocks (we're going to talk about them very soon). Test your code
using the data we've provided for you.

Test Data

Sample input: 55

Expected output: False

Sample input: 99

Expected output: False

Sample input: 100

Expected output: True

Sample input: 101

Expected output: True

Sample input: -5

Expected output: False

Sample input: +123

Expected output: True

'''

# solution 

n = int(input())
print(n >= 100)
