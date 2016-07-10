def partialDigest(L):

    print "partialDigest"

    X = [0]

    width = max(L)

    while len(L) > 0:

        print "X is", X
        print "L is", L
        y = max(L)

        print "diff is:", diff(y, X)

        d = diff(y, X)

        if set(d).issubset(set(L)):
            X.append(y)
            L = removeElements(d, L)
        else:
            X.append(abs(width-y))
            d = diff(abs(width-y), X)
            L = removeElements(d, L)


    return X

def diff(y, X):
    d = []
    for xi in X:
        d.append(abs(y-xi))
    return d

def removeElements(d, L):
    print "remove d ", d
    print L
    for i in L:
        for j in d:
            if i == j:
                print "i is ", i
                L.remove(i)
                d.remove(i)
    return L

if __name__ == "__main__":
    print "Python implementation of partial digetive problem PDP on page 90."

    X = partialDigest([2, 2, 3, 3, 4, 5, 6, 7, 8, 10])
