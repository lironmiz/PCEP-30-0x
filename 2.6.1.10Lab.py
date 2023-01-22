'''
Estimated time
20 minutes

Level of difficulty
Intermediate

Objectives
becoming familiar with the concept of numbers, operators and arithmetic operations in Python;
understanding the precedence and associativity of Python operators, as well as the proper use of parentheses.
Scenario
Your task is to complete the code in order to evaluate the following expression:


The result should be assigned to y. Be careful - watch the operators and keep their priorities in mind. Don't hesitate to use as many parentheses as you need.

You can use additional variables to shorten the expression (but it's not necessary). Test your code carefully.


Test Data
Sample input: 1

Expected output:

y = 0.6000000000000001

Sample input: 10

Expected output:

y = 0.09901951266867294

Sample input: 100

Expected output:

y = 0.009999000199950014

Sample input: -5

Expected output:

y = -0.19258202567760344

'''

# solution 

x = float(input("Enter value for x: "))

y = 1 / ( x + ( 1 / ( x + (1 / ( x + 1 / x)))))

print("y =", y)
