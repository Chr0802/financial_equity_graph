import math
from EntityNode import EntityNode

class EquityEdge:
    def __init__(self, headNode, tailNode, weight):
        self.__headNode = headNode
        self.__tailNode = tailNode
        self.__weight = weight

        self.visited_times = 0

        headNode.addOutEdge(self)
        tailNode.addInEdge(self)

    @property
    def headNode(self):
        return self.__headNode

    @property
    def tailNode(self):
        return self.__tailNode

    @property
    def weight(self):
        return self.__weight

    @property
    def lnWeight(self):
        return -math.log(self.__weight)

class PseudoEdge:
    def __init__(self, node):
        self.__headNode = node
        self.__tailNode = EntityNode('pseudo_root','pseudo_root')
        self.__tailNode.addInEdge(self)
        self.__weight = 1
        self.__tailNode.pre_u = 1
        self.__tailNode.u = 1
        self.__tailNode.v = 1
        self.__tailNode.w = 0

        self.visited_times = 0

    @property
    def headNode(self):
        return self.__headNode

    @property
    def tailNode(self):
        return self.__tailNode

    @property
    def weight(self):
        return self.__weight

    @property
    def lnWeight(self):
        return -math.log(self.__weight)