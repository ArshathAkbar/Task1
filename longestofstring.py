def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def longestPalindrome(s):
    n = len(s)
    if n <= 1:  # Edge case for strings of length 0 or 1
        return s

    start = 0
    maxLength = 1

    for i in range(n):
        # Odd length palindrome
        palindrome = expandAroundCenter(s, i, i)
        if len(palindrome) > maxLength:
            maxLength = len(palindrome)
            start = i - (len(palindrome) - 1) // 2

        # Even length palindrome
        palindrome = expandAroundCenter(s, i, i + 1)
        if len(palindrome) > maxLength:
            maxLength = len(palindrome)
            start = i - (len(palindrome) - 1) // 2

    return s[start:start + maxLength]

input_str = input("Enter a string: ")
print("The longest palindromic substring is:", longestPalindrome(input_str))