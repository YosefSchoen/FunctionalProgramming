myInputList = eval(input("enter a list of integer numbers, strings, tuples, and lists"))
print(myInputList)

myTuples = []
myNestedElement = []
myNumbers = []
myStrings = []

for item in myInputList:
    if isinstance(item, tuple):
        myTuples.append(item)

    elif isinstance(item, list):
        myNestedElement.extend(item)

    elif isinstance(item, int):
        myNumbers.append(item)

    elif isinstance(item, str):
        myStrings.append(item)

print("list of tuples", myTuples, "\n")
print("tuple of nested elements", tuple(myNestedElement), "\n")
print("tuple of integers", tuple(myNumbers), "\n")
print("list of strings", myStrings, "\n")







