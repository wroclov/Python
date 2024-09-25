import re

# this function was not filtering out non [a-z] characters
#def isPalindrome(word: str):
#    word = "".join(word.lower().split())
#    return word==word[::-1]


# below one will focus just on letters, omitting other characters
def isPalindrome(word: str):
    word = "".join(re.findall(r'[a-z]+', word.lower()))
    return word == word[::-1]

print(isPalindrome("okko"))
print(isPalindrome("ok k o"))
print(isPalindrome("ok k O"))

print(isPalindrome("nieds"))
print(isPalindrome("Go hang a salami, I'm a lasagna hog."))