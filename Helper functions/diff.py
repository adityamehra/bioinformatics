def D(y, X):
    print "D"
    diff = []
    for xi in X:
        diff.append(abs(y-xi))
    print "diff ", diff


if __name__ == "__main__":
    print "Python implementation of partial digestive problem PDP on page 90."

    D(7, [0, 2, 10])
