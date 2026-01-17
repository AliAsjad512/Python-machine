# Problem: Reverse a string
def reverse_string(s):
    # Method 1: Using slicing
    return s[::-1]

def reverse_string_loop(s):
    # Method 2: Using loop
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Test
text = "Python Programming"
print(f"Original: {text}")
print(f"Reversed (slicing): {reverse_string(text)}")
print(f"Reversed (loop): {reverse_string_loop(text)}")