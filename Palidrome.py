def solution(S):
    """
    This function takes in a string S and determines whether it can be turned into a palindrome
    by changing some of the characters to '?'. If so, it returns the modified string. If not,
    it returns "NO".
    """
    N = len(S)
    left, right = 0, N - 1  # left and right are the indices of the two characters we are
                            # currently comparing
    result = list(S)  # result is the modified string we are building

    while left < right:
        """
        If the character on the left is '?', then we need to decide what to replace it
        with. We can either replace it with the character on the right, or we can replace
        both the character on the left and the character on the right with a character that
        is guaranteed to make the string a palindrome.
        """
        print(f"Before: left={left}, right={right}, result={result}")
        if result[left] == '?':
            if result[right] == '?':
                result[left] = result[right] = 'a'
            else:
                result[left] = result[right]
        elif result[right] == '?':
            result[right] = result[left]
        print(f"After: left={left}, right={right}, result={result}")

        """
        If the characters on the left and right are not equal, then we can't make the
        string a palindrome by replacing some of the characters with '?', so we return "NO".
        """
        if result[left] != result[right]:
            return "NO"

        """
        Now we can move the left and right pointers one position to the right and to the left,
        respectively, since we have processed the characters at the current positions.
        """
        left += 1
        right -= 1

    """
    If we have processed all the characters and the string is a palindrome, then we return
    the modified string.
    """
    return ''.join(result)

# Test the function with an example
print(solution("?ab??a"))









