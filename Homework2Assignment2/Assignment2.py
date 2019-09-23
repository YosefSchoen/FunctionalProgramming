def sumDigits1(n):
    findDigits = lambda k: (n // 10**k) % 10
    ourDigits = list(map(findDigits, range(len(str(n)), -1, -1)))
    return sum(ourDigits)



def sumDigits2(n):
    ourSum = sum(map(int, str(n)))
    return ourSum


def main():
    n = int(input("Enter a number"))
    print(sumDigits1(n))
    print(sumDigits2(n))

