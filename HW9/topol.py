def order(n, edge_list):
    edge_set = set([tuple(i) for i in edge_list])
    node_list = list()
    node_from_list, node_to_list = zip(*edge_set)
    source_set = set(node_from_list) - set(node_to_list)

    while len(source_set) != 0:
        node_from = source_set.pop()
        node_list.append(node_from)
        from_selection = [e for e in edge_set if e[0] == node_from]
        for edge in from_selection:
            node_to = edge[1]
            edge_set.discard(edge)
            to_selection = [e for e in edge_set if e[1] == node_to]
            if len(to_selection) == 0:
                source_set.add(node_to)

    if len(edge_set) != 0:
        return None
    else:
        return node_list

print order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
print order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
print order(4, [(0,1), (1,2), (2,1), (2,3)])
