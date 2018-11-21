from functools import reduce

"Sum the values of a list"


def sum_list(a):

    return sum(a)


def sum_list_v2(a):
    new_list = []
    for x in a:
        # checks if x is a list. If it is, we know that its a nested list.
        if isinstance(x, list):
            new_list.extend(x)
        else:
            new_list.append(x)

    # print(new_list)

    return sum(new_list)


def sum_list_v3(a):
    answer = 0
    for x in a:
        # checks if x is a list. If it is, we know that its a nested list.
        if isinstance(x, list):
            answer += sum(x)
        else:
            answer += x

    return answer



def sum_list_v4(a):

    if type(a) != list:
        return a
    if a == []:
        return 0

    return sum_list_v4(a[0]) + sum_list_v4(a[1:])


print(sum_list_v2([1, 2, 3, [2, 3], 4, 5, 6, [10, 11, 12, 13]]))
print(sum_list_v3([1, 2, 3, [2, 3], 4, 5, 6, [10, 11, 12, 13]]))
print(sum_list([1, 2, 3, 4, 5]))
print(sum_list_v4([1, 2, 3, 4, 5, [9, 10]]))


print(reduce((lambda x, y: x + y), [1, 2, 3, 4, 5]))
