X = []
width = 0

def partialDigest(L):

    global X
    global width
    width = max(L)
    L.remove(width)
    X = [0, width]
    print "partialDigest"
    print "width is ", width
    print "X is ", X
    if place(L):
        print "Ok"
        print X
    else:
        print "Not Ok"
        print X


def place(L):

    print "L is ", L
    print "X is ", X
    print "width is ", width

    if not L:
        return True

    y = max(L)
    print "y is ", y
    print "1. d is ", diff(y, X)
    if set(diff(y, X)).issubset(set(L)):
        X.append(y)
        L = removeElements(diff(y, X), L)
        if place(L):
            return True
        else:
            X.remove(y)
            L.extend(diff(y, X))

    print "2. d is ", diff(abs(width-y), X)
    if set(diff(abs(width-y), X)).issubset(set(L)):
        X.append(abs(width-y))
        L = removeElements(diff(abs(width-y), X), L)
        if place(L):
            return True
        else:
            X.remove(abs(width-y))
            L.extend(diff(abs(width-y), X))

    return False

def diff(y, X):
    d = []
    for xi in X:
        d.append(abs(y-xi))
    return d

def removeElements(d, L):
    for i in L:
        for j in d:
            if i == j:
                L.remove(i)
                d.remove(i)
    return L


if __name__ == "__main__":
    print "Python implementation of partial digetive problem PDP on page 90."

    partialDigest([2, 2, 3, 3, 4, 5, 6, 7, 8, 10])
