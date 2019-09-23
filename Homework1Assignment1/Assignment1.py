
def checkIfLegal (x, y, z):
    if x + y < z:
        return False
    if x + z < y:
        return False
    if y + z < x:
        return False
    return True


a = input()
b = input()
c = input()

a = float(a)
b = float(b)
c = float(c)

if checkIfLegal(a, b, c):
    print("they are correct triangle sides’ lengths")
else:
    print("they are in error")
