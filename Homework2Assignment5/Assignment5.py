from itertools import accumulate

def m(n):
    j = list(map(lambda x: x / (x + 1), range(1, n + 1)))
    print(sum(j))
    partialSums = list(accumulate(j))

    it = list(range(1, n + 1))
    result = zip(partialSums, it)
    return list(result)


def main():
    n = int(input())
    print(m(n))


