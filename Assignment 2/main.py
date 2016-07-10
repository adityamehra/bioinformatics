import random
import time

X = []
L = []
#L = random.sample(range(30), 20)
width = 0

def partialDigest(L):
    print "L is", L
    global X, width
    width = max(L)
    L.remove(width)
    X = [0, width]
    place(L, X)


def place(L, X):

    if not L:
        X.sort()
        print "Output is: ", X
        return

    y = max(L)

    if issubset(y, X, L):
        X.append(y)
        removeElements(y, X, L)
        place(L, X)
        if y in X:
            X.remove(y)
        L.extend(D(y, X))

    if issubset(abs(width-y), X, L):
        X.append(abs(width-y))
        removeElements(abs(width-y), X, L)
        place(L, X)
        if abs(width-y) in X:
            X.remove(abs(width-y))
        L.extend(D(abs(width-y), X))

    return


def D(y, X):
    diff = []
    for xi in X:
        diff.append(abs(y-xi))
    return diff


def removeElements(y, X, L):
    for xi in X:
        if abs(y - xi) in L:
            L.remove(abs(y - xi))


def issubset(y, X, L):
        for xi in X:
            if abs(y-xi) not in L:
                return False
        return True

def create_multiset(lst):

        L = []

        lst1 = lst
        lst2 = lst[:]

        for x in lst1:
            lst2.remove(x)
            for y in lst2:
                L.append(abs(y-x))

        L.sort()

        return L



if __name__ == "__main__":
    print "Python implementation of partial digetive problem PDP on page 90."

    lst = random.sample(range(40), 20)

    if 0 not in lst:
        lst.append(0)

    lst.sort()

    print "X is", lst

    L = create_multiset(lst)

    begin = time.time()

    partialDigest(L)

    print "Time is ", time.time() - begin
