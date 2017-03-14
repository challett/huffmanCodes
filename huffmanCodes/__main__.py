import logging
import os
import sys
import optparse

log = logging.getLogger(__name__)

def insert_p(list, pObj):
    for index, value in enumerate(list):
        if value['p'] < pObj['p']:
            list.insert(index, pObj)
            break

def main(probabilities):
    isTakingInputs = True
    probArray = []

    while True:
        inputString = raw_input("Enter probabilities as symbol:p, enter done when done\n")
        splitString = inputString.split(':')
        if inputString == "done":
            break

        if len(splitString) !== 2:
            print "Invalid Input\n"
            continue

        probArray.append(dict(
            symbol=splitString[0],
            p=float(splitString[1]),
        ))

    sortedArray = sorted(probArray, key=lambda k: -k['p'])
    #TODO: Run Huffman Algorithm to find codes
    return 0

if __name__ == '__main__':

    log.info('')
    sys.exit(main())
