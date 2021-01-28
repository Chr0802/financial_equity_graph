from EntityNode import EntityNode
from EquityEdge import EquityEdge, PseudoEdge

# 层序遍历同时利用拓扑排序得到识别出受环路影响的节点 并利用dfs识别出环路
def levelOrder3(root: EntityNode):
    _edge = PseudoEdge(root)
    queue, res, level = [_edge], [], 0
    node_dic = {_edge.tailNode.id:_edge.tailNode}
    dg_dic = {_edge.tailNode.id:0}

    while level < 100:
    # while queue:
        n = len(queue)
        node_tmp = set() # 遍历当前层时，节点的集合，用于最后更新节点pre_u,v,w
        edge_tmp = set() # 遍历当前层时，边的集合，用于计算节点在当前层的u
        for i in range(n):
            # 访问队列头的边
            edge_i = queue.pop(0)
            edge_i.visited_times += 1
            # 更新该边头节点的出度，并更新出度字典和节点索引
            node_i = edge_i.headNode
            node_i.degree_o +=1
            dg_dic[node_i.id] = node_i.degree_o
            node_dic[node_i.id] = node_i

            if edge_i.tailNode.w + edge_i.lnWeight < node_i.w:
                node_i.cur_w = min(node_i.cur_w, edge_i.tailNode.w + edge_i.lnWeight)
                node_i.key_l = level
                print(node_i.name, ":",node_i.w, node_i.key_l, level)
            if edge_i not in edge_tmp:
                node_i.u = node_i.u + edge_i.weight * edge_i.tailNode.pre_u
            print('name:',node_i.name, ' v:', node_i.v, ' u:', node_i.u, 'weight:', edge_i.weight, 'tailNode:', edge_i.tailNode.name,'tailNode.pre_u:', edge_i.tailNode.pre_u )
            node_tmp.add(edge_i.headNode)
            edge_tmp.add(edge_i)
            for edge in node_i.inEdges:
                queue.append(edge)
        # 对于本层遍历到的节点，更新他们对中心节点的累计最终持股比例v 以及本层累计的持股比例pre_u
        for headNode in node_tmp:
            update(headNode)
        # 找出出度为0的节点, “去除”该节点的入边，并更新对应头节点的出度和字典
        zero_dg_nodes = list(filter(lambda x: x[1] == 0, dg_dic.items()))
        print('dg_dic:', dg_dic)
        for (key, value) in zero_dg_nodes:
            zd_node = node_dic[key]
            print(zd_node.id, zd_node.inEdges)
            for inEdge in zd_node.inEdges:
                print('(',inEdge.tailNode.name,'<-',inEdge.headNode.name,'):',inEdge.visited_times)
                inEdge.headNode.degree_o -= inEdge.visited_times
                dg_dic[inEdge.headNode.id] = inEdge.headNode.degree_o
            dg_dic.pop(key)
        print('dg_dic:', dg_dic)
        # 找出更新之后出度为0的节点, 确定是否满足退出循环的条件
        _zero_dg_nodes = list(filter(lambda x: x[1] == 0, dg_dic.items()))
        if not (zero_dg_nodes or _zero_dg_nodes ):
            break

        res.append(list(map(lambda x: x.name, node_tmp)))
        print('-' * 20, 'level:', level, '-' * 20)
        level += 1

    canddt_set = set([node_dic[key] for key in dg_dic.keys()])
    cycles = cycleDetect(canddt_set)

    return res,cycles

def update(node):
    # 更新本层遍历结束后该节点的最终持股比例相关状态
    node.pre_u = node.u
    node.v = node.v + node.u
    node.u = 0
    # 更新本层遍历结束后该节点的关键路径相关状态
    node.w = node.cur_w
    print(">>>",node.name,'pre_u:',node.pre_u, 'v:',node.v)

# 给定受环路影响的节点集合，找出其中存在的环路
def cycleDetect(nodes):
    cycles = []
    path = []
    while nodes:
        node = nodes.pop()
        (nomal, cycle, visited) = findCycle(node)
        cycles += cycle
        path += nomal
        nodes -= visited
    return cycles

# 对于给定节点，利用dfs对其邻居节点进行遍历，找出其到叶子节点的无环路径normal、遍历过程遇到的环路cycle、遍历到的节点集合visited
def findCycle(node):
    nomal = [] # 经过环路节点的正常路径列表
    path = [] # dfs过程中的当前路径
    cycle = [] # 环路列表
    visited = set() # 已经访问过的节点集合
    def dfs(node):
        isCycle = node.name in path
        cycleIndex = path.index(node.name) if isCycle else -1
        path.append(node.name)
        visited.add(node)
        # print(path)
        if isCycle:
            cycle.append(path[cycleIndex:-1])
            # print(path, cycle)
            path.pop()
            return
        elif not node.inEdges:
            nomal.append(path[:])
            print(path,nomal)
            path.pop()
            return
        else:
            for edge in node.inEdges:
                dfs(edge.headNode)
            path.pop()
    dfs(node)
    return (nomal, cycle, visited)



if __name__ == '__main__':
    #添加节点
    v0 = EntityNode('v0', 'v0')
    v1 = EntityNode('v1', 'v1')
    v2 = EntityNode('v2', 'v2')
    v3 = EntityNode('v3', 'v3')
    v4 = EntityNode('v4', 'v4')
    v5 = EntityNode('v5', 'v5')
    v6 = EntityNode('v6', 'v6')
    v7 = EntityNode('v7', 'v7')
    v8 = EntityNode('v8', 'v8')

    v9 = EntityNode('v9', 'v9')

    #添加边
    e1 = EquityEdge(v1, v0, 0.0449)
    e2 = EquityEdge(v2, v0, 0.0456)
    e3 = EquityEdge(v3, v0, 0.2083)
    e4 = EquityEdge(v4, v0, 0.0292)
    e5 = EquityEdge(v5, v0, 0.0461)
    e6 = EquityEdge(v1, v2, 0.9)
    e7 = EquityEdge(v6, v1, 0.9)
    e11 = EquityEdge(v2, v1, 0.1) #cycle
    # e8 = EquityEdge(v6, v2, 0.1)
    e8 = EquityEdge(v2, v6, 0.1)  # cycle
    e9 = EquityEdge(v1, v3, 0.202)
    e10 = EquityEdge(v2, v3, 0.78)
    e12 = EquityEdge(v8, v7, 0.78)
    e13 = EquityEdge(v7, v4, 0.06)
    e14 = EquityEdge(v7, v5, 0.01)
    e14 = EquityEdge(v7, v1, 0.01)

    e8 = EquityEdge(v9, v6, 0.1)

    # 检验根节点对其他节点持股是否影响结果
    # _v = EntityNode('_v', '_v')
    # _e = EquityEdge(v0, _v, 0.5)

    print(levelOrder3(v0))
    # for node in [v0, v1, v2, v3, v4, v5, v6]:
    for node in [v0, v1, v2, v3, v4, v5, v6, v7, v8]:
        print(node.name, node.v, node.key_l)

    # print(findCycle(v1))



