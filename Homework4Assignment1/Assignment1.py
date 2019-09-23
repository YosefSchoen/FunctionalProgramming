import Targil4input
import statistics


# This function will take the 2 lists from Targil4inputs and make 1 big list according to the prompt.
def myStudList(list1, list2):
    # size of each list
    sizeOne = len(list1)
    sizeTwo = len(list2)

    # each element will be built here
    def TmyStudList(result, i):
        # sizeTwo is the size of the teachersName list
        if i == sizeTwo:
            return result

        # createLElements will build each element according to the prompt
        result.append(createLElement(list1, list2, sizeOne, [], i))
        return TmyStudList(result, i + 1)

    # L is the list the prompt required
    L = TmyStudList([], 0)

    # D is the dictionary version of L
    D = myStudDict(L)
    return D


def createLElement(list1, list2, sizeOne, result, i):
    # teachers class is the name of the class that teacher teaches
    subject = list2[i][1]

    # each element in L is comprised of a teacher and a list of students in that teachers class
    Li = [teacher(list2, i), studentsList(list1, sizeOne, subject)]
    return Li



def teacher(list2, i):
    # return correct teacher
    return list2[i][0]


def studentsList(list1, sizeOne, subject):
    studentsInClass = findStudents(list1, sizeOne, subject, [], 0)
    size = len(studentsInClass)

    if size == 0:
        students = [[0], (0, 0)]

    else:
        # students is comprised of a list of Ids and a grade of the class
        students = [idsList(studentsInClass, size, [], 0), gradesTuple(studentsInClass, size, (), 0)]
    return students


# findStudents will put the students who take teachersClass into a list
def findStudents(list1, sizeOne, subject, result, i):
    if i == sizeOne:
        return result

    if list1[i][2] == subject:
        result.append(list1[i])

    return findStudents(list1, sizeOne, subject, result, i + 1)


# idList will return a list of all of the ids of the students in studentsInClass
def idsList(studentsInClass, size, result, i):
    if i == size:
        return result

    result.append(studentsInClass[i][0])
    return idsList(studentsInClass, size, result, i + 1)


# gradeTuple will build a tuple of the class's average and standard deviation
def gradesTuple(studentsInClass, size, result, i):
    if i == size:
        return result

    # grade is comprised of an average and a standard deviation
    grades = (average(studentsInClass, size, 0, 0), standardDeviation(studentsInClass, size))
    return grades


def average(studentsInClass, size, result, i):
    if i == size:
        return result / size

    result = result + studentsInClass[i][1]
    return average(studentsInClass, size, result, i + 1)


def standardDeviation(studentsInClass, size):
    grades = findGrades(studentsInClass, size, [], 0)

    if len(grades) > 1:
        return statistics.stdev(grades)

    return 0


def findGrades(studentsInClass, size, result, i):
    if i == size:
        return result

    result.append(studentsInClass[i][1])
    return findGrades(studentsInClass, size, result, i + 1)

#
def myStudDict(myList):
    D = {}
    size = len(myList)

    def TmyStudDict(result, i):
        if i == size:
            return result

        result[getKey(myList, i)] = getItem(myList, i)
        return TmyStudDict(result, i + 1)

    return TmyStudDict(D, 0)


def getKey(myList, i):
    return myList[i][0]


def getItem(myList, i):
    sizeofIds = len(myList[i][1][0])
    classGrade = myList[i][1][1]
    classAvg = classGrade[0]
    classStdev = classGrade[1]

    item = getIds(myList, sizeofIds, [], i, 0)
    item.append(classAvg)
    item.append(classStdev)

    return item


def getIds(myList, sizeofIds, result, i, j):
    if j == sizeofIds:
        return result

    result.append(myList[i][1][0][j])
    return getIds(myList, sizeofIds, result, i,  j + 1)


def main():
    print(myStudList(Targil4input.jctMarks, Targil4input.teacherName))
