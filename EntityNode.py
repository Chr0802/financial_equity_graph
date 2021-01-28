class EntityNode:
    def __init__(self, ID, name=None, inEdges=[], outEdges=[]):
        self.__id = ID
        self.__name = name
        self.__inEdges = set(inEdges)
        self.__outEdges = set(outEdges)

        self.key_l = 0 # 关键路径的长度
        self.w = float('inf') # 关键路径对数权重
        self.cur_w = float('inf') # 关键路径对数权重

        self.u = 0 # 该节点在当前层的持股比例累加值
        self.v = 0# 该节点持股比例累加值
        self.pre_u = 0 # 该节点在上次遍历所在层持股比例的累加值

        # for cycle detection by Topological Sorting
        self.degree_o = 0


    def addInEdge(self, edge):
        self.__inEdges.add(edge)

    def addOutEdge(self, edge):
        self.__outEdges.add(edge)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def inEdges(self):
        return list(self.__inEdges)

    @property
    def outEdges(self):
        return list(self.__outEdges)
