from palindrome import is_palindrome


def test_is_palindrom():
    assert is_palindrome('anna') == 'Yes'
    assert is_palindrome('Anna') == 'Yes'
    assert is_palindrome('lucky') == 'No'
    assert is_palindrome('Make my day!') == 'No'
    assert is_palindrome('bob') == 'Yes'
    assert is_palindrome('something') == 'No'
