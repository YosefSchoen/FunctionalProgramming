import eratosthenes
from pprint import pprint


def twinp(n):
    primeList = eratosthenes.napa(n + 2)
    del(primeList[0:2])

    isNextTwinPrime = list(map(lambda x: primeList[x] + 2 if primeList[x + 1] == primeList[x] + 2 else 0, range(0, len(primeList) - 1)))

    twinList = dict(zip(primeList, isNextTwinPrime))
    twinList = {x:y for (x, y) in twinList.items() if (y != 0)}
    return twinList


def main():
    n =int(input())
    pprint(twinp(n), width=1)
    return


main()
