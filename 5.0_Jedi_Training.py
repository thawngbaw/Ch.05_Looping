  #Sign your name:__Bawi Thawng___

'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = int(input("Enter a number: "))
    total += x
print("The total is:", total)
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2, 102, 2):
    print(i)




'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
num_ = 10
while num_ > -1:
    print(num_)
    num_ -= 1
print("Blast off!")




'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random

print(random.randint(1, 10))





'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
total = 0
num_zero = 0
num_positive = 0
num_negative = 0
for i in range(7):
    num_input = int(input("Enter a number: "))
    if num_input > 0:
        num_positive += 1
    elif num_input < 0:
        num_negative += 1
    else:
        num_zero += 1
    total += num_input
print()
print("total =", total)
print("number of positive =", num_positive)
print("number of negative =", num_negative)
print("number of zero =", num_zero)