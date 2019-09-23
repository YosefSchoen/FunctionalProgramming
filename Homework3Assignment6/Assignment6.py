from itertools import accumulate

def pi(n):
    series = list(map(lambda x: 4 * (((-1)**(x + 1)) / ((2 * x) - 1)), range(1, n+1)))
    print("the sum of the series is :" + str(sum(series)))
    partialSums = list(accumulate(series))

    it = list(range(1, n + 1))
    listOfSums = zip(partialSums, it)

    return list(listOfSums)


def piTail(n):
    def Tpi(n, i, result):
        if i > n:
            return result
        nextElement = 4 * (((-1)**(i + 1)) / ((2 * i) - 1))
        if i > 1:
            nextElement = (nextElement + result[i - 2])
        result.append(nextElement)
        return Tpi(n, i + 1, result)
    return zipRecursion(Tpi(n, 1, []))


def zipRecursion(n):
    def Tzip(n, i, result):
        if i == len(n):
            return result
        result.append((n[i], i))
        return Tzip(n, i + 1, result)
    return Tzip(n, 1, [])


n = int(input())
result1 = pi(n)
result2 = piTail(n)

print("\n".join(map(str, result1)))
print("\n".join(map(str, result2)))
