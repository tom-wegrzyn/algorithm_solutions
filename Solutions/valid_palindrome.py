def valid_palindrome(s: str) -> bool:
    """
    Takes in a string and determines if it's a valid palindrome.

    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
    non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters
    and numbers.

    Parameters
    ----------
    s : str
        The string which can potentially be a palindrome.

    Returns
    ----------
    bool
        True or false depending on if the string is a valid palindrome.
    """
    x = ""

    if len(s) == 0:
        return True

    for char in s:
        if char.isalnum():
            x += char

    if x.lower() == x[::-1].lower():
        return True

    return False
