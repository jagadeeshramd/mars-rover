from queues_adt import PriorityQueue


def dijkstra(start, end):
    """
    Dijkstra's algorithm. Takes a start node and end node, and uses
    its neighbour list to traverse the graph.
    Uses the heapq queue in queues.py.
    :param start: Node
    :param end: Node
    :return: previous, dictionary with all nodes as key, and where we came from (parent node) as value.
             cost_so_far, dictionary with tiles as key, and their cost so far as value.
             success, True or False. If the algorithm found the end tile or not.
             has_been_next, list over tiles that has been considered as the next tile.
    """
    q = PriorityQueue()
    q.put(start, 0)
    success = False
    previous = {start: None}
    cost_so_far = {start: 0}
    has_been_next = []
    new_cost = 0

    while not q.empty():
        currnode = q.pop()
        currnode.visit()
        if currnode == end:
            success = True
            break

        for nextnode in currnode.neighbours:
            if nextnode not in has_been_next:
                has_been_next.append(nextnode)
            #new_cost = cost_so_far[currnode] + nextnode.weight
            new_cost = cost_so_far[currnode] + currnode.edge_len(nextnode)
            nextnode.weight+=new_cost
            #print(nextnode.weight)
            if nextnode not in cost_so_far.keys() or new_cost < cost_so_far[nextnode]:
                cost_so_far[nextnode] = new_cost
                priority = new_cost
                q.put(nextnode, priority)
                previous[nextnode] = currnode

    return success, previous, cost_so_far, has_been_next
