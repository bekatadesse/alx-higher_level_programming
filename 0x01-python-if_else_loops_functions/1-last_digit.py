from random import randint 


number = randint(-10000, 10000)

num = int(str(number)[-1])

if number < 0:
    num *= -1


if num < 6 and num:
    res = "less than 6 and not 0"
elif num==0: 
    res = "is 0"
elif num > 5:
    res = "greater than 5"

msg = f"Last digit of {number} is {num} and {res}"

print(msg)
