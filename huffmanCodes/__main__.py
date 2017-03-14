import logging
import os
import sys
import optparse

log = logging.getLogger(__name__)

# Insert a pObj such that the sorting of the list is persisted
def insert_p(list, pObj):
    for index, value in enumerate(list):
        if value['p'] > pObj['p']:
            list.insert(index, pObj)
            return
    list.append(pObj)
    return


def main(probabilities):
    # Array is to be sorted by increasing probability.  Lowest prob will be at index 0.
    probArray = []

    while True:
        inputString = raw_input("Enter probabilities as symbol:p, enter done when done\n")
        splitString = inputString.split(':')
        if inputString == "done":
            break

        if len(splitString) !== 2:
            print "Invalid Input\n"
            continue
        pObj = dict(
            symbol=splitString[0],
            p=float(splitString[1]),
        )
        insert_p(probArray, pObj)

    #TODO: Run Huffman Algorithm to find codes
    return 0

if __name__ == '__main__':

    log.info('')
    sys.exit(main())
