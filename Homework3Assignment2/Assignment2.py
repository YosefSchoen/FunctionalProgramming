def sumDigitsNonTail(n):
    if n < 10:
        return n

    return (n % 10) + sumDigitsNonTail(n // 10)


def sumDigitsTail(n):
    def Tsum(n, result):
        if n == 0:
            return result
        return Tsum(n // 10, (n % 10) + result)
    return Tsum(n, 0)


def main():
    n = int(input("Enter a number"))
    print(sumDigitsNonTail(n))
    print(sumDigitsTail(n))
