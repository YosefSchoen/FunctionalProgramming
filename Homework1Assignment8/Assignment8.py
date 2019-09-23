N = int

def guessTest(guess = [], rand = []):
    answer = ()
    for i in range(N):
        if guess[i] == rand[i]:
            answer.append(i)
        else:
            answer.append("X")

    return answer




def main():
    myTuple = []
    randElement = int

    guessTuple = []
    guessElement = int

    N = int(input("pick a number between 3 and 9"))
    import random

    for i in range(N):
        randElement = random.randint(1, 10)
        myTuple.append(randElement)

    for i in range(N):
        guessElement = int(input("guess what number between 1 and 9 is in the tuple"))
        guessTuple.append(guessElement)

    guessTest(guessTuple, myTuple)





