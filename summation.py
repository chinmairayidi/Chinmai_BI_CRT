#write a python program to read an interger value as input from the user and  find the summation of digits 
num = int(input("Enter an integer: "))
sum = 0
while num != 0:
    digit = num % 10        # to Get the last digit
    sum += digit            # Add to the summation
    num //= 10              # Remove the last digit we take quotient
print("Summation of digits:", sum)

#terinary operation
num = input("Enter an integer: ")
print("Sum of digits:", sum(int(d) if d.isdigit() else 0 for d in num))

#write a python a program to read an input as integer and print the number of even digits and odd digits in a particular number .
num = int(input("Enter an integer: "))
even_count = 0
odd_count = 0

while num != 0:
    digit = num % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num //= 10

print("Even digits count:", even_count)
print("Odd digits count:", odd_count)

#write a python a program to read an input as integer and find the summation of even digits and odd digits in a particular number.

num = int(input("Enter an integer: "))
even_sum = 0
odd_sum = 0
while num != 0:
    digit = num % 10
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
    num //= 10
print("Sum of even digits:", even_sum)
print("Sum of odd digits:", odd_sum)



#write a python a program to read an integer value as input and find number of 0's present in the user entered number .
num = int(input("Enter an integer: "))
zero_count = 0
if num == 0:
    zero_count = 1
else:
    while num != 0:
        digit = num % 10
        if digit == 0:
            zero_count += 1
        num //= 10
print("Number of zeros:", zero_count)
