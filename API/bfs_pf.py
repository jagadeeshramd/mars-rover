from queues_adt import Queue


def bfs(start, end):
    """
    Breadth first search. Takes a start node and end node, and uses
    its neighbour list to traverse the graph.
    Uses the LIFO queue in queues.py.
    :param start: Node
    :param end: Node
    :return: previous, dictionary with all nodes, and where we came from
             (parent) to this node.
             success, True or False. If the algorithm found the end node or not
             has_been_next, list of nodes that have been considered as the next node.
    """
    q = Queue()
    q.add(start)
    previous = {start: None}
    success = False
    has_been_next = []

    while not q.empty():
        currnode = q.pop()
        currnode.visit()
        if currnode == end:
            success = True
            break

        for nextnode in currnode.neighbours.keys():
            if nextnode not in has_been_next:
                has_been_next.append(nextnode)
            if nextnode not in previous:
                q.add(nextnode)
                previous[nextnode] = currnode

    return success, previous, has_been_next
