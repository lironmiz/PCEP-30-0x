'''
Estimated time
5 minutes

Level of difficulty
Very easy

Objectives
Familiarize the student with:

using basic instructions related to lists;
creating and modifying lists.
Scenario
There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.

Your task is to:

write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
write a line of code that removes the last element from the list (Step 2)
write a line of code that prints the length of the existing list (Step 3).
Ready for this challenge?

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

# Step 2: write a line of code that removes the last element from the list.

# Step 3: write a line of code that prints the length of the existing list.

print(hat_list)

'''
hat_list = [1, 2, 3, 4, 5]

# Step 1:
hat_list[2] = int(input("Enter a number to replace the middle element: "))

# Step 2:
hat_list.pop()

# Step 3:
print(len(hat_list))

print(hat_list)
