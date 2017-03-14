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

    # def setCodes(self):
    #     while (self.left):
    #         self.left.code += '0'
    #         self.left.setCodes()
    #     while (self.right):
    #         self.right.code += '1'
    #         self.right.setCodes()

    def printCodes(self, code=''):
        if (self.left):
            self.left.printCodes(code + '1')
        if (self.right):
            self.right.printCodes(code + '0')
        else:
            print self.symbol + ' - ' + code


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

    while True:
        inputString = raw_input("Enter probabilities as symbol:p, enter done when done\n")
        splitString = inputString.split(':')
        if inputString == "done":
            break

        if len(splitString) != 2:
            print "Invalid Input\n"
            continue

        newTree = HuffTree(symbol=splitString[0], p=splitString[1])
        insert_p(huffList, newTree)

    # for item in huffList:
    #     print item.symbol

    while len(huffList) > 1:
        lo = huffList.pop()
        hi = huffList.pop()
        newP = lo.p + hi.p
        combined = HuffTree(p=newP, left=hi, right=lo)
        insert_p(huffList, combined)

    huffList[0].printCodes()
    #TODO: Run Huffman Algorithm to find codes
    return 0

if __name__ == '__main__':

    log.info('')
    sys.exit(main())
