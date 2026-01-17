# Problem: Check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Test
print(is_palindrome("racecar"))      # True
print(is_palindrome("Hello"))        # False
print(is_palindrome("A man a plan")) # False
print(is_palindrome("A man a plan a canal Panama")) # True