

def totalDistance(l, DNA):

    n = 8

    t = 8

    total_d = 0

    for i in range(t):

        each_d = 10000

        for j in range(n-len(l)+1):

             temp = hamming(l, DNA[j:j+len(l)])

             if temp < each_d:
                 each_d = temp


        total_d += each_d

    return total_d


def hamming(l, dnaStrip):

    hamming_dist = 0

    for i in range(len(l)):

        if l[i] == dnaStrip[i]:
            hamming_dist += 1

    return hamming_dist