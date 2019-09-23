def addTail(n):
    def Tm(n, i, result):
        if i >= n:
            return result
        nextElement = i / (i + 1)
        if i > 0:
            nextElement = nextElement + result[i - 1]
        result.append(nextElement)
        return Tm(n, i + 1, result)
    return zipRecursion(Tm(n, 0, []))


def addNonTail(n, i, result):
    if i < n:
        result.append(partialSum(i, 0))
        return addNonTail(n, i + 1, result)
    return zipRecursion(result)


def partialSum(n, i):
    if i <= n:
        return partialSum(n, i + 1) + (i / (i + 1))
    return 0


def zipRecursion(n):
    def Tzip(n, i, result):
        if i == len(n):
            return result
        result.append((n[i], i))
        return Tzip(n, i + 1, result)
    return Tzip(n, 0, [])


n = int(input())
print(addTail(n))
print(addNonTail(n, 0, []))
