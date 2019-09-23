def reverseNum1(n):
    return int("".join(str(n)[::-1]))


def isPalindrome(n):
    m = reverseNum1(n)

    if n == m:
        return True

    return False


n = int(input("Enter a number"))

if isPalindrome(n):
    print("It is a palindrome!!")

else:
    print("It is not a palindrome")

