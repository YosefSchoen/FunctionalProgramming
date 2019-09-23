from itertools import accumulate

def pi(n):
    series =list(map(lambda x: 4 * (((-1)**(x + 1)) / ((2 * x) - 1)), range(1, n+1)))
    print("the sum of the series is :" + str(sum(series)))
    partialSums = list(accumulate(series))

    it = list(range(1, n + 1))
    listOfSums = zip(partialSums, it)

    return list(listOfSums)


n = int(input())
result = pi(n)
print("\n".join(map(str, result)))
