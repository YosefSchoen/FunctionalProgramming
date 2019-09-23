def pentaNumRangeNonTail(n1, n2, pentaNumList):
    if (n1 < n2):
        nextPentaNum = (n1 * ((3 * n1) - 1)) // 2
        pentaNumList.append(nextPentaNum)
        pentaNumRangeNonTail(n1 + 1, n2, pentaNumList)
    return


def printNonTail(n1, n2, pentaNumList, i):
    if i == 0:
        pentaNumRangeNonTail(n1, n2, pentaNumList)

    if i < n2 - n1:
        if i % 10 == 0 and i != 0:
            print("\n")
        print(pentaNumList[i], end=" ")
        printNonTail(n1, n2, pentaNumList, i + 1)
    return


x1 = int(input("enter a number"))
x2 = int(input("enter another number"))
printNonTail(x1, x2, [], 0)
