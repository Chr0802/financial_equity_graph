from EntityNode import EntityNode
from EquityEdge import EquityEdge, PseudoEdge

def levelOrder(root: EntityNode):
    _edge = PseudoEdge(root)
    queue, res, level = [_edge], [], 0
    while queue:
        n = len(queue)
        tmp = set()
        for i in range(n):
            edge_i = queue.pop(0)
            node_i = edge_i.headNode
            tmp.add((edge_i.tailNode.name, edge_i.headNode.name))
            for edge in  node_i.inEdges:
                queue.append(edge)
        res.append(tmp)
        level += 1
    return res


def levelOrder3(root: EntityNode):
    _edge = PseudoEdge(root)
    queue, res, level = [_edge], [], 0
    while queue:
        n = len(queue)
        node_tmp = set() # 遍历当前层时，节点的集合，用于最后更新节点pre_u,v,w
        edge_tmp = set() # 遍历当前层时，边的集合，用于计算节点在当前层的u
        for i in range(n):
            edge_i = queue.pop(0)
            node_i = edge_i.headNode
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
        for headNode in node_tmp:
            update(headNode)
        res.append(list(map(lambda x: x.name, node_tmp)))
        print('-'*20, 'level:', level, '-'*20)
        level += 1
    return res

def update(node):
    # 更新本层遍历结束后该节点的最终持股比例相关状态
    node.pre_u = node.u
    node.v = node.v + node.u
    node.u = 0
    # 更新本层遍历结束后该节点的关键路径相关状态
    node.w = node.cur_w
    print(">>>",node.name,'pre_u:',node.pre_u, 'v:',node.v)


if __name__ == '__main__':
    #添加节点
    v0 = EntityNode('0', 'v0')
    v1 = EntityNode('1', 'v1')
    v2 = EntityNode('2', 'v2')
    v3 = EntityNode('3', 'v3')
    v4 = EntityNode('4', 'v4')
    v5 = EntityNode('5', 'v5')
    v6 = EntityNode('6', 'v6')
    #添加边
    e1 = EquityEdge(v1, v0, 0.0449)
    e2 = EquityEdge(v2, v0, 0.0456)
    e3 = EquityEdge(v3, v0, 0.2083)
    e4 = EquityEdge(v4, v0, 0.0292)
    e5 = EquityEdge(v5, v0, 0.0461)
    e6 = EquityEdge(v1, v2, 0.9)
    e7 = EquityEdge(v6, v1, 0.9)
    e8 = EquityEdge(v6, v2, 0.1)
    e9 = EquityEdge(v1, v3, 0.202)
    e10 = EquityEdge(v2, v3, 0.78)

    print(levelOrder3(v0))

    for node in [v0, v1, v2, v3, v4, v5, v6]:
        print(node.name, node.v, node.w, node.key_l)