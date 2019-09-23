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


n = int(input("Enter a Number"))
print(reverseNonTail(list(str(n)), 0))
print(reverseTail(str(n)))
