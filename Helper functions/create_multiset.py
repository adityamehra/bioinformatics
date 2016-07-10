import random

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

    lst = random.sample(range(30), 10 )

    if 0 not in lst:
        lst.append(0)

    lst.sort()

    print "List with cut points: ", lst

    L = create_multiset(lst)

    print "L is ", L
