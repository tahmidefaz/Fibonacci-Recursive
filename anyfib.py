#############################################################################
# Author: Tahmid Efaz
# Date: 11/23/16
# Purpose: Given two numbers of a sequence, it will compute the
#          nth fib term of the sequence
# Speciality: option to override python's built in maximum recursion depth
#############################################################################

import sys
sys.setrecursionlimit(10000)        # override python's default recursion depth (Change this number as needed)


def anyfib(n2,n1,t):
    '''
    Given two numbers (n1 and n2) it will compute the fib number
    based on the term
    '''

    if t == 0:
        return n2
    else:
        return anyfib(n2+n1,n2,t-1)          #adds the two previous number and uses recursion


def main():
    n1 = abs(int(raw_input("Enter the first number in the series: ")))
    n2 = abs(int(raw_input("Enter the second number of the series: ")))
    num = abs(int(raw_input("Which fibonacci term you want to compute?(*Term starts from 0) : ")))
    fib = anyfib(n1,n2, num)
    print "Result from minifib is: " + str(fib)

main()
