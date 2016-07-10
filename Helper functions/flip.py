import random
from random import randint

def flipSequence(times):
    n = 10 
    sequence = [0] + range(1,n) + [n]
    print "Original Sequence ", sequence
    while times > 0:
        s = randint(1, n)
        print s
        e = randint(s, n)
        print e
        subsequence = sequence[s:e+1]
        subsequence.reverse()
        sequence[s:e+1] = subsequence
        times -= 1
        s = 0
        e = 0
    return sequence	
     

if __name__ == "__main__":
    print "Python implementation of breakpoint reversal sort on page 135"
    
    sequence = flipSequence(1)
    print "Flipped Sequence: ", sequence