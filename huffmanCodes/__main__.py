import logging
import os
import sys
import optparse
import math
# from huffmanCodes.server import app
from flask import Flask, render_template
from hufftree import HuffTree
log = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def error_404(notfound_exception):
    return index()

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
        combined = HuffTree(p=newP, left=hi, right=lo, symbol=hi.symbol + lo.symbol)
        insert_p(huffList, combined)

    def printNode(self):
        print self.symbol + " - " + self.code

    huffDict = dict()
    def saveToDictionary(self):
        huffDict[self.symbol] = (self.code, self.p)

    if len(huffList):
        huffList[0].setCodes()
        huffList[0].getLeaves(printNode)
        huffList[0].getLeaves(saveToDictionary)

    averageCodeLength = 0
    entropy = 0
    for key, value in huffDict.items():
        averageCodeLength += len(value[0]) * value[1]
        entropy += value[1]*math.log(1./value[1], 2)

    print averageCodeLength
    print entropy

    return 0

if __name__ == '__main__':

    app.run(host=os.getenv('HOST', 'localhost'),
            port=int(os.getenv('PORT', '8080')),
            debug=bool(os.getenv('DEBUG_ON', '1')))
