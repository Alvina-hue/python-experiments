string = input("Enter a string: ")
print("The string is:",string)

old = input("Enter character to replace: ")
new = input("Enter new character: ")

replaced = string.replace(old, new)
print("After replacement:", replaced)

reverse = string[::-1]
print("Reversed string:", reverse)

if string == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

ch = input("Enter a character to count: ")
print("Character frequency:", string.count(ch))

word = input("Enter a word to count: ")
words = string.split()
print("Word frequency:", words.count(word))