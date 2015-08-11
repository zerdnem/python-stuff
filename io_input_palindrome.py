def reverse(text):
    return text[::-1]

def is_palindrome(text):
    text = [c for c in text.lower() if c.isalpha()]
    return text == reverse(text)

something = raw_input("Input: ")
if is_palindrome(something):
    print "Yep"
else:
    print "Nope"
