def linear_search(x, search_list):
    """
    Returns the index of the x if found in search_list
    Else returns -1
    """
    iterations = 0
    index = 0
    while index < len(search_list):
        iterations += 1
        if x == search_list[index]:
            print('iterations = ' + str(iterations))
            return(f'Found match at index: {index}')
        index += 1
    return -1


def binary_search(x, search_list):
    iterations = 1
    left = 0  # Determines the starting index of the list we have to search in
    # Determines the last index of the list we have to search in
    right = len(search_list)-1
    mid = (right + left)//2
    while search_list[int(mid)] != x:  # If this is not our search element
        # If the current middle element is less than x then move the left next to mid
        # Else we move right next to mid
        if search_list[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
        mid = (right + left)/2
        iterations += 1
    print(f'iterations = {str(iterations)}')
    return mid


print()
print('Linear Search Results')
print(linear_search(32, [4, 8, 45, 24, 10, 32, 9, 56]))
print()
print('Binary Search Results')
print(binary_search(32, [4, 8, 9, 10, 24, 32, 45, 56]))
