from hufftree import HuffTree
import math


def insert_p(huff_list, new_tree):
    # Insert a pObj such that the sorting of the list is persisted
    for index, huffTree in enumerate(huff_list):
        if huffTree.p < new_tree.p:
            huff_list.insert(index, new_tree)
            return
    huff_list.append(new_tree)
    return


def create_codes(input_dict):
    # Array is to be sorted by increasing probability.  Lowest prob will be at index 0.
    huff_list = []

    for item in input_dict.items():
        insert_p(huff_list,HuffTree(symbol=item[0], p=float(item[1])))

    while len(huff_list) > 1:
        lo = huff_list.pop()
        hi = huff_list.pop()
        new_p = lo.p + hi.p
        combined = HuffTree(p=new_p, left=hi, right=lo, symbol=hi.symbol + lo.symbol)
        insert_p(huff_list, combined)

    huff_dict = dict()

    def save_to_dictionary(self):
        huff_dict[self.symbol] = dict(code=self.code, p=self.p)

    if len(huff_list):
        huff_list[0].setCodes()
        huff_list[0].getLeaves(save_to_dictionary)

    average_code_length = 0
    entropy = 0
    for key, value in huff_dict.items():
        average_code_length += len(value["code"]) * value["p"]
        entropy += value["p"]*math.log(1./value["p"], 2)

    return huff_dict, average_code_length, entropy
