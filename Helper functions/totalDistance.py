

def totalDistance(l, DNA):

    t = 1

    n = len(DNA) / t

    total_d = 0

    for i in range(t):

        each_d = 10000
        str = ""
        for j in range(n-len(l)+1):

             temp = hamming(l, DNA[j:j+len(l)])

             if temp < each_d:
                 each_d = temp
                 str =  DNA[j:j+len(l)]

        print each_d
        print str

        total_d += each_d

    return total_d


def hamming(l, dnaStrip):

    hamming_dist = 0

    for i in range(len(l)):

        if l[i] != dnaStrip[i]:
            hamming_dist += 1

    return hamming_dist

if __name__ == "__main__":

    print "Total distance implementation for Motify finding..."

    total_Distance = 0
    l = "acgtacgt"


    DNA = [ "cctgatagacgctatctggctatccaggtacttaggtcctctgtgcgaatctatgcgtttccaaccat",
            "agtactggtgtacatttgatccatacgtacaccggcaacctgaaacaaacgctcagaaccagaagtgc",
            "aaacgttagtgcaccctctttcttcgtggctctggccaacgagggctgatgtataagacgaaaatttt",
            "agcctccgatgtaagtcatagctgtaactattacctgccacccctattacatcttacgtccatataca",
            "ctgttatacaacgcgtcatggcggggtatgcgttttggtcgtcgtacgctcgatcgttaccgtacggc" ]

    for dna in DNA:

        temp = totalDistance(l, dna)

        total_Distance += temp

    print total_Distance