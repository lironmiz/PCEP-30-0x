'''
Estimated time
10-15 minutes

Level of difficulty
Easy

Objectives
Familiarize the student with:

projecting and writing parameterized functions;
utilizing the return statement;
testing the functions.
Scenario
Your task is to write and test a function which takes one argument (a year) and returns True if the year is a leap year, or False otherwise.

The seed of the function is already sown in the skeleton code in the editor.

Note: we've also prepared a short testing code, which you can use to test your function.

The code uses two lists - one with the test data, and the other containing the expected results. The code will tell you if any of your results are invalid
'''

# solution 

def is_year_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
    else:
            return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
