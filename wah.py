#palindrome program
word = str(input("Please enter a word to check if it is a palindrome: "))
def reverse(wstring):
    global palindrome
    reverseword = word[::-1]
    if word in reverseword:
        palindrome = True
    else:
        palindrome = False
        return reverseword
reverse(word)
if palindrome == True:
    print("Your word, {}, is a palindrome!".format(word))
else:
    print("Your word, {}, is not a palindrome. :( backwards it is: {}".format(word, reverse(word)))