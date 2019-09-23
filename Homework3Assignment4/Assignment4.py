def reverseTail(n):
    def Treverse(n, i, result):
        if i >= 0:
            result = result + n[i]
            return Treverse(n, i - 1, result)
        return int(result)
    return Treverse(n, len(n) - 1, "")


def reverseNonTail(n, i):
    l = len(n) - 1
    if i < (l + 1) // 2:
        temp = n[i]
        n[i] = n[l - i]
        n[l - i] = temp
        return reverseNonTail(n, i + 1)
    return int("".join(n))


def isPalindromeTail(n, i):
    if n == reverseTail(str(n)):
        return True
    return False


def isPalindromeNonTail(n, i):
    if n == reverseNonTail(list(str(n)), i):
        return True
    return False


n = int(input("Enter a number"))

if isPalindromeTail(n, 0):
    print("It is a palindrome!!")

else:
    print("It is not a palindrome")


if isPalindromeNonTail(n, 0):
    print("It is a palindrome!!")

else:
    print("It is not a palindrome")



