#Given a positive integer, return its binary representation (output using integer datatype).

def digit_to_bin(n):
    n=int(input("enter a number"))
    b=""
    while n!=0:
        a=n%2
        n=n//2
        b+=str(a)
    return b[::-1]
x=digit_to_bin(n)
print(x)