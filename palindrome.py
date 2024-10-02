
def is_palindrome(text:str) ->bool:
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("Never odd or even"))

