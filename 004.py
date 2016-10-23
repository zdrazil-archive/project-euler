# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def reverse_word(word):
    pal_array = []
    word = str(word)
    word_length = len(word)
    reversed_word = ""

    for letter in range(word_length):
        pal_array.append(word[word_length-letter-1])

    for letter in pal_array:
        reversed_word += letter

    return reversed_word

def ispalindrome(number):
    reversed_word = int(reverse_word(number))

    if reversed_word == number:
        return True
    else:
        return False

first_num = 999
second_num = 999
biggest_num = 0

for number1 in range(100, 1000):

    for number2 in range(100, 1000):
        equal_num = number1 * number2

        if ispalindrome(equal_num) and (equal_num > biggest_num):
            biggest_num = equal_num

print(biggest_num)



