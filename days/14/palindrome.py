def is_palindrome(data: str):
    """
    Receives a string and checks to see if it is a palindrome. Returns 'Yes' if a palindrome and 'No' if not a palindrome.

    >>>is_palindrome(bob)
    Yes
    >>>is_palindrome(anna)
    Yes
    >>>is_palindrome(lucky)
    No
    """
    data = data.lower()

    if data == data[::-1]:
        return('Yes')
    else:
        return('No')


if __name__ == "__main__":
    data = input('Check if a word is a palindrome: '"")
    print(is_palindrome(data))
