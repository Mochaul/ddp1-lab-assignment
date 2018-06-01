## File name : lab02b.py
## using simultaneous assignments to sort data

# five variable with given values
number1 = 23
number2 = 7
number3 = 3
number4 = -6
number5 = 19
print("Initial data: ")
print(number1,number2,number3,number4,number5)
# the output expected: 23 7 3 -6 19

# simultaneous assignment to swap the values
# off the variavles; two variables at a time
number1,number4 = number4,number1
number2,number3 = number3,number2
number4,number5 = number5,number4


# display the sorted values
print("Sorted data, from smallest to largest: ")
print(number1,number2,number3,number4,number5)

# the output expected: -6 3 7 19 23
