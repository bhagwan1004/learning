#Given a positive integer, return the number of even digits in it.
def sum_even_digits(n):
    na = str(n)
    count = 0
    for digit in na:
         if int(digit) % 2 == 0:
            count += 1
    
    return count
n = int(input("Enter a positive integer: "))
x= sum_even_digits(n)
print(x)