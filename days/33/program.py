"""
Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

"""
while True:
    try:
        number = input("Please enter an integer: " "")
        number = int(number)
        break
    except ValueError:
        print(
            f'You entered {number}, which is not a valid integer. Please try again.')

number_dict = {}
i = 1
for i in range(1, number + 1):
    number_dict[i] = i * i
    i += 1

print(number_dict)
