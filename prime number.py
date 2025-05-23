def prime(n):
    if n % 2 == 0:
        return False
    else:
        return True
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return false
        else:
            return true
num= int(input("enter a number: "))
if prime(num):
    print("number is prime")
else:
    print("number is not prime")
