def reverse(word):
    return word[::-1]

def almostPalindrome(palindrome_word):
    rev = reverse(palindrome_word)

    if (palindrome_word == rev):
        return True
    #remove first and last character
    elif(palindrome_word[1:-1] == rev[1:-1]):
        return True
    else:
        return False


input_word = input("input palindrome word?")

ans = almostPalindrome(input_word)

if ans == 1:
    print("true")
else:
    print("false")