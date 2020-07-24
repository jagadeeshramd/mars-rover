from queues_adt import PriorityQueue


def heuristic(node1, node2):
    """
    Manhattan distance between two tiles.
    :param node1: Node
    :param node2: Node
    :return: int distance
    """
    (x1, y1) = (node1.r, node1.c)
    (x2, y2) = (node2.r, node2.c)
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(start, end):
    """
    A* Pathfinding algorithm. Takes a start node and end node, and uses
    their neighbour list to traverse the graph.
    Uses the heapq queue in queues.py.
    :param start: node
    :param end: node
    :return: previous, dictionary with all nodes as key, and where we came from (parent node) as value.
             cost_so_far, dictionary with nodes as key, and their cost so far as value.
             success, True or False. If the algorithm found the end node or not.
             has_been_next, list over tiles that has been considered as the next node.
    """
    q = PriorityQueue()
    q.put(start, 0)
    success = False
    previous = {start: None}
    cost_so_far = {start: 0}
    has_been_next = []

    while not q.empty():
        currnode = q.pop()
        currnode.visit()

        if currnode == end:
            success = True
            break

        for nextnode in currnode.neighbours:

            if nextnode not in has_been_next:
                has_been_next.append(nextnode)

            new_cost = cost_so_far[currnode] + currnode.edge_len(nextnode)
            nextnode.weight+=new_cost
            if nextnode not in cost_so_far.keys() or new_cost < cost_so_far[nextnode]:
                cost_so_far[nextnode] = new_cost
                priority = new_cost + heuristic(end, nextnode)
                q.put(nextnode, priority)
                previous[nextnode] = currnode

    return success, previous, cost_so_far, has_been_next
