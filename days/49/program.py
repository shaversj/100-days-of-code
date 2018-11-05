

def FirstFactorial(num):

    factorial = 1
    for i in reversed(range(1, num, 2)):
        total = num*i
        factorial = factorial * total
        num -= 2

    return factorial


print(FirstFactorial(8))
