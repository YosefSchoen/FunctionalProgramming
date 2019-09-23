def reverseNum1(n):
    return int("".join(str(n)[::-1]))


def reverseNum2(n):
    n = list(str(n))
    n.reverse()
    n = "".join(n)
    return n


def main():
    n = int(input("Enter a Number"))
    print(reverseNum1(n))
    print(reverseNum2(n))
