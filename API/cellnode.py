class Node():

    def __init__(self, obstacle=False, r=0, c=0):

        """
        Initializes the node.
        :param obstacle: Whether node is walkable or not
        :param r: Row location.
        :param c: Column location
        :param weight: length of each cell: 1, unit squares in grid

        """

        self.obstacle = obstacle
        self.r = r
        self.c = c
        self.visited = False

        #self.neighbours = []
        self.neighbours = {} # Dictionary of neighbour node : edge weight

        self.weight = 0


        self.cleanup()

    def visit(self):
        self.visited = True
        return

    def __lt__(self, next):
        return self.weight < next.weight


    """def create_neighbours(self):
        self.neighbours = []"""

    #def adde(self,node):
    #    self.neighbours.append(node)
    def adde(self,node,ed):
        self.neighbours[node]=ed

    def edge_len(self,node):
        return self.neighbours.get(node)

    def cleanup(self):
        self.visited = False
        self.neighbours.clear()

    def __str__(self):
        """
         toString method.
        :return: The tiles information as string.
        """
        return 'r' + str(self.r) + '\t' + 'c=' + str(self.c)

        """self.h = 0.0  # cost from current node to the goal
        self.g = 0.0  # cost from the start node to current node
        self.f = 0.0  # distance from start to this point (f = g + h )

        self.opened = 0
        self.closed = False

        # used for backtracking to the start point
        self.parent = None"""
