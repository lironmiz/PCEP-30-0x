'''
Estimated time
5 minutes

Level of difficulty
Very Easy

Objectives
becoming familiar with the concept of comments in Python;
using and not using comments;
replacing comments with code;
experimenting with Python code.
Scenario
The code in the editor contains comments. Try to improve it: add or remove comments 
where you find it appropriate (yes, sometimes removing a comment can make the code more readable),
and change variable names where you think this will improve code comprehension.

NOTE

Comments are very important. They are used not only to make your programs easier to understand,
but also to disable those pieces of code that are currently not needed
(e.g., when you need to test some parts of your code only, and ignore other). 
Good programmers describe each important piece of code, and give self-commenting names to variables
as sometimes it is simply much better to leave information in the code.

It's good to use readable variable names, and sometimes it's better to divide your code
into named pieces (e.g., functions). In some situations, it's a good idea
to write the steps of computations in a clearer way.

One more thing: it may happen that a comment contains a wrong or incorrect piece of information 
you should never do that on purpose!

''' 

# solution 

#this program computes the number of seconds in a given number of hours

num_of_hour = 3 # number of hours
SECONDS_IN_HOUR = 3600 # number of seconds in 1 hour

print("Hours: ", num_of_hour) 
print("Seconds in Hours: ", num_of_hour * SECONDS_IN_HOUR ) # printing the number of seconds in a given number of hours

print("Goodbye")

