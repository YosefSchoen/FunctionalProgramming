import math

def pentaNumRange(n1, n2):
    getPentaNum = lambda n: (n * ((3 * n) - 1)) // 2
    return list(map(getPentaNum, range(n1, n2)))


def print1(n1, n2):
    #n1 = int((1 + math.sqrt(1 + (12 * n1))) // 2)
    #n2 = int((1 + math.sqrt(1 + (12 *  n2))) // 2)

    pentaNum = pentaNumRange(n1, n2)
    for i in range(0, n2 - n1):
        if i % 10 == 0 and i != 0:
             print("\n")
        print(pentaNum[i], end=" ")
    return


x1 = int(input("Enter an Integer"))
x2 = int(input("Enter another Integer"))
print1(x1, x2)

