# tail, linear recursive function
def treatline(lineNr, line):
    lineList = line.split()
    def Ttreatline(resultDict, i):  #recursive call
        # base case 1
        if not lineList[i].isalpha():  # boolean function to check for legal words
            return -1
        # base case 2
        if i == len(lineList):
            result = (lineNr, resultDict)
            return result
        resultDict[lineList[i]] = createTuples(lineList[i])
        return Ttreatline(resultDict, i + 1) # tail recursion
    Ttreatline({}, 0) # first recursive call for nested function


def createTuples(word):  #create tuples receives a word and makes teh tuple
    letters = ([], [], [])
    letters[0] = list(filter(isVowel, word)) # calls helper function isVowel and filters the vowels
    letters[1] = list(filter(isBtoM, word)) # calls helper function to filter out letters from b to M
    letters[2] = list(filter(isNtoZ, word))  # calls helper function to filter out letters from N to Z
    return letters

def isVowel(char):
    vowels = "aeiouAEIOU"
    return char in vowels

def isBtoM(char):
    consonant = "bcdfghjklmBCDFGHJKLM"
    return char in consonant

def isNtoZ(char):
    consonant = "npqrstvwxyzNPQRSTVWXYZ"
    return char in consonant

# tail, linear recursive function
def treatxtfile(flname):
    def Ttreattxtfile(i, result):
        # base case
        if i == #size of the file:
            newdict = dict(result)
            return newdict
        result.append(treatline(i, #line of file))
        return Ttreattxtfile(i + 1, result) # tail recursive call
    return Ttreattxtfile(0, []) # recursive function







def occursumary(fldict):

    return

fldict = treatxtfile(#put file name)