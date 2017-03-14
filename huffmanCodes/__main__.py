import logging
import os
import sys
import optparse

log = logging.getLogger(__name__)

class HuffTree:
    def __init__(self, p, symbol='', left=None, right=None):
        self.p = p
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''

    def setCodes(self, code=''):
        self.code = code
        if (self.left):
            print "Calling left with code " + code+"1"
            self.left.setCodes(code+"1")
        if (self.right):
            print "Calling right with code " + code+"0" + " From " + self.symbol
            self.right.setCodes(code+"0")

    def printCodes(self):
        if (self.left):
            self.left.printCodes()
        if (self.right):
            self.right.printCodes()
        else:
            print self.symbol + " - " + self.code


# Insert a pObj such that the sorting of the list is persisted
def insert_p(huffList, newTree):
    for index, huffTree in enumerate(huffList):
        if huffTree.p < newTree.p:
            huffList.insert(index, newTree)
            return
    huffList.append(newTree)
    return


def main():
    # Array is to be sorted by increasing probability.  Lowest prob will be at index 0.
    huffList = []

    # while True:
    #     inputString = raw_input("Enter probabilities as symbol=p, enter done when done\n")
    #     splitString = inputString.split('=')
    #     if inputString == "done":
    #         break
    #
    #     if len(splitString) != 2:
    #         print "Invalid Input\n"
    #         continue
    #
    #     newTree = HuffTree(symbol=splitString[0], p=float(splitString[1]))



    newTree = HuffTree(symbol="AA", p=9./16)
    insert_p(huffList, newTree)

    newTree = HuffTree(symbol="AB", p=9./64)
    insert_p(huffList, newTree)

    newTree = HuffTree(symbol="AC", p=3./64)
    insert_p(huffList, newTree)

    newTree = HuffTree(symbol="BA", p=9./64)
    insert_p(huffList, newTree)

    newTree = HuffTree(symbol="BB", p=9./256)
    insert_p(huffList, newTree)

    newTree = HuffTree(symbol="BC", p=3./256)
    insert_p(huffList, newTree)

    newTree = HuffTree(symbol="CA", p=3./64)
    insert_p(huffList, newTree)

    newTree = HuffTree(symbol="CB", p=3./256)
    insert_p(huffList, newTree)

    newTree = HuffTree(symbol="CC", p=1./256)
    insert_p(huffList, newTree)

    while len(huffList) > 1:
        lo = huffList.pop()
        hi = huffList.pop()
        newP = lo.p + hi.p
        #print "merging " + hi.symbol + " with " + lo.symbol
        combined = HuffTree(p=newP, left=hi, right=lo, symbol=hi.symbol + lo.symbol)
        #print "combined contains left=" + combined.left.symbol + " right=" + combined.right.symbol
        insert_p(huffList, combined)

    if len(huffList):
        huffList[0].setCodes()
        huffList[0].printCodes()


    return 0

if __name__ == '__main__':

    log.info('')
    sys.exit(main())
