# @author: 22000781 - Parita Tarvani
# @description: Program No. 8. Create a basic function that returns True if the word 'dog' is contained in the input string. Don't
# worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. :
# findDog('Is there a dog here?')

def find_dog(s):
    return "dog" in s.lower()

print(find_dog("is there a dog here?"))

#output: True