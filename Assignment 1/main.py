# Name: Aditya Mehra
# Assignment #: Assignment 1
# A#: A02189413


import random
import time
from random import randint

#http://stackoverflow.com/questions/22257249/how-do-i-reverse-a-sublist-in-a-list-in-place
#http://www.csbio.unc.edu/mcmillan/Media/breakpointReversalSort.txt

def hasBreakpoints(sequence):
    """ This functions verifies if the sequence has breakpoints or not, 
        returns True if sequnces have breakpoints """
    for i in xrange(1, len(sequence)):
        if (sequence[i] != sequence[i-1] + 1):
            return True
    return False

def getStrips(seq):
    """ find contained intervals where sequence is ordered, and return intervals
    in as lists, increasing and decreasing. Single elements are considered
    decreasing. "Contained" excludes the first and last interval. """
    deltas = [seq[i+1] - seq[i] for i in xrange(len(seq)-1)]
    increasing = list()
    decreasing = list()
    start = 0
    for i, diff in enumerate(deltas):
        if (abs(diff) == 1) and (diff == deltas[start]):
            continue
        if (start > 0):
            if deltas[start] == 1:
                increasing.append((start, i+1))
            else:
                decreasing.append((start, i+1))
        start = i+1
    return increasing, decreasing

def pickReversal(seq, strips):
    """ test each decreasing interval to see if it leads to a reversal that
    removes two breakpoints, otherwise, return a reversal that removes only one """
    reversal = (-1, None)
    left = [i for i, j in strips]
    right = [j for i, j in strips]
    for i in left:
        for j in right:
            if (i >= j-1):
                # skip invalid intervals and
                # those with only one element
                continue
            breakpointsRemoved = 0
            if (abs(seq[j-1] - seq[i-1]) == 1):
                # reversal will remove left breakpoint
                breakpointsRemoved += 1
            if (abs(seq[j] - seq[i]) == 1):
                # reversal will remove right breakpoint
                breakpointsRemoved += 1
            if (breakpointsRemoved > reversal[0]):
                reversal = (breakpointsRemoved, (i,j))
    return reversal[1]

def doReversal(seq,(i,j)):
    return seq[:i] + [element for element in reversed(seq[i:j])] + seq[j:]

def improvedBreakpointReversalSort(seq):
    flips = 0
    begin = time.time()
    while hasBreakpoints(seq):
        increasing, decreasing = getStrips(seq)
        if len(decreasing) > 0:
            reversal = pickReversal(seq, increasing+decreasing)
        else:
            reversal = increasing[0]
        print seq, "reversal", reversal
        seq = doReversal(seq,reversal)
	flips += 1
    print "Sorted sequene is: ", seq
    print "Time taken by algorithm is: ", time.time() - begin
    print "Number of flips by Algorithm: ", flips
    return

def flipSequence(times):
    #n is length of the sequence and is set as 1000.
    n = 1000
    #sequene holds permutation alongwith 0 and n.
    sequence = [0] + range(1,n) + [n]
    print "Original sequence is:", sequence
    while times > 0:
        s = randint(1, n-1)
        print "Start of flip for", times, "flip is", s
        e = randint(s, n-1)
        print "End of flip for", times, "flip is", e
        subsequence = sequence[s:e+1]
        subsequence.reverse()
        sequence[s:e+1] = subsequence
        times -= 1
        s = 0
        e = 0
	print "Flipped sequence is:", sequence
    return sequence
     

if __name__ == "__main__":
    print "Python implementation of breakpoint reversal sort on page 135"
    
    sequence = flipSequence(700)
    improvedBreakpointReversalSort(sequence)