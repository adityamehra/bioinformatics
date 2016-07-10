def removeElements(L, diff):
    for i in L:
        for j in diff:
            if i == j:
                L.remove(i)
                diff.remove(i)
    print L
    L.extend([1, 2, 3, 6])
    print L

if __name__ == "__main__":
    print "Remove elements."

    L = [1,2,2,3,3,4,5,6,6,6,7,8]
    diff = [1, 2, 3, 6])
    removeElements(L, diff) 
