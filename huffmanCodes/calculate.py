from hufftree import HuffTree
import optparse
import math

# Insert a pObj such that the sorting of the list is persisted
def insert_p(huffList, newTree):
    for index, huffTree in enumerate(huffList):
        if huffTree.p < newTree.p:
            huffList.insert(index, newTree)
            return
    huffList.append(newTree)
    return


def createCodes(inputDict):
    # Array is to be sorted by increasing probability.  Lowest prob will be at index 0.
    huffList = []

    print inputDict.items()
    for item in inputDict.items():
        insert_p(huffList,HuffTree(symbol=item[0], p=float(item[1])))

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
        huffDict[self.symbol] = dict(code=self.code, p=self.p)

    if len(huffList):
        huffList[0].setCodes()
        huffList[0].getLeaves(printNode)
        huffList[0].getLeaves(saveToDictionary)

    averageCodeLength = 0
    entropy = 0
    for key, value in huffDict.items():
        averageCodeLength += len(value["code"]) * value["p"]
        entropy += value["p"]*math.log(1./value["p"], 2)

    print averageCodeLength
    print entropy

    return (huffDict, averageCodeLength, entropy)
