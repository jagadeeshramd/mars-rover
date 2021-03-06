import math

from bfs_pf import bfs
from dijkstra_pf import dijkstra
from astar_manhattan_pf import *
from cellnode import Node


class Graph():

    def __init__(self, h, w, olist, start, end):
        """
        An undirected graph is generated to depict the grid. Adjacency list
        representation. Stores the nodes as vertices in a nodes dictionary
        where the (row, col) is the key to the node in the grid.
        Adds edges to neighbours from each node.
        Edges not added to cells that are obstacles.
        :param h: Height of grid
        :param w: Width of grid
        :param olist: List of tuples of (r,c) coordinates of obstacle cells in grid
        :param start: Start node
        :param end: Goal node
        """
        self.height = h
        self.width = w

        self.nodes = {}
        self.nodelist = []
        self.olist=[]
        for (i,j) in olist:
            self.olist.append((int(j),int(i)))
        #self.olist = olist  # list of nodes that are obstacles

        self.start = Node(False, int(start[1]), int(start[0]))
        # Put the cell node in a dictionary with
        self.nodes[self.start.r, self.start.c] = self.start
        # coord as keys and append in nodelist.
        self.nodelist.append(self.start)

        self.end = Node(False, int(end[1]), int(end[0]))
        # Put the cell node in a dictionary with
        self.nodes[self.end.r, self.end.c] = self.end
        # coord as keys and append in nodelist.
        self.nodelist.append(self.end)

        self.add_vertices()
        self.add_neighbours()

    def isinside(self, r, c):
        return 0 <= r < self.height and 0 <= c < self.width

    def iswalkable(self, r, c):
        # checks if the cell is inside grid and if it is not obstacle (walkable
        # or not)
        return (self.isinside(r, c) and (not(self.nodes[r, c].obstacle)))

    def add_neighbours(self):
        for key, node1 in self.nodes.items():
            r, c = key

            if not self.iswalkable(node1.r,node1.c):
                continue

            if self.iswalkable(r-1, c):                     # Above
                node2 = self.nodes[r-1, c]
                ed=self.calc_dist(node1.r,node1.c,node2.r,node2.c)
                self.add_edge(node1, node2, ed)

            if self.iswalkable(r+1, c):
                node2 = self.nodes[r+1, c]
                ed=self.calc_dist(node1.r,node1.c,node2.r,node2.c)
                self.add_edge(node1, node2, ed)                # Below

            if self.iswalkable(r, c+1):
                node2 = self.nodes[r, c+1]
                ed=self.calc_dist(node1.r,node1.c,node2.r,node2.c)
                self.add_edge(node1, node2, ed)               # Right

            if self.iswalkable(r, c-1):
                node2 = self.nodes[r, c-1]
                ed=self.calc_dist(node1.r,node1.c,node2.r,node2.c)
                self.add_edge(node1, node2, ed)                # Left

            if self.iswalkable(r-1, c-1) and (self.iswalkable(r,c-1) or self.iswalkable(r-1,c)):                 # Upper Left diagonal
                node2 = self.nodes[r-1, c-1]
                ed=self.calc_dist(node1.r,node1.c,node2.r,node2.c)
                self.add_edge(node1, node2, ed)

            if self.iswalkable(r-1, c+1) and (self.iswalkable(r-1,c) or self.iswalkable(r,c+1)):                # Upper Right diagonal
                node2 = self.nodes[r-1, c+1]
                ed=self.calc_dist(node1.r,node1.c,node2.r,node2.c)
                self.add_edge(node1, node2, ed)

            if self.iswalkable(r+1, c-1) and (self.iswalkable(r,c-1) or self.iswalkable(r+1,c)):                # Lower Left diagonal
                node2 = self.nodes[r+1, c-1]
                ed=self.calc_dist(node1.r,node1.c,node2.r,node2.c)
                self.add_edge(node1, node2, ed)

            if self.iswalkable(r+1, c+1) and (self.iswalkable(r,c+1) or self.iswalkable(r+1,c)):                # Lower Right diagonal
                node2 = self.nodes[r+1, c+1]
                ed=self.calc_dist(node1.r,node1.c,node2.r,node2.c)
                self.add_edge(node1, node2, ed)

        return





    def add_edge(self, node1, node2, ed):
        node1.adde(node2,ed)
        node2.adde(node1,ed)
        return

    def add_vertices(self):
        for r in range(self.height):
            for c in range(self.width):
                if (r,c) == (self.start.r,self.start.c) or (r,c) == (self.end.r,self.end.c):
                    continue

                if (r, c) in self.olist:  # checking if obstacle or not
                    o = True
                else:
                    o = False
                n = Node(o, r, c)  # Makes a cell node.
                self.nodes[r,c] = n  # Put the cell node in a dictionary with
                # coord as keys and append in nodelist.
                self.nodelist.append(n)
        return

    def cleanup(self):
        for node in self.nodes.values():
            node.cleanup()

    def calc_dist(self,r1,c1,r2,c2,diag=0):
        d=0
        if diag == 0 :
            d = math.sqrt(pow((r2 - r1), 2) + pow((c2 - c1), 2))
        else:
            d=abs(r2-r1)+abs(c2-c1)
        return d







    """
    The following function needs to be written in a new file (app.py) with django
    or flask web framework for javascript - python connection
    Need to create graph object
    """

    def run_algorithm(self, algo):
        """
        The algorithm we are gonna run. BFS, Dijkstra, DFS etc.
        :param start: Start node
        :param end: Goal node
        :return: int total cost
        """
        if algo == "bfs":
            # Sets all necessary lists and
            (succ, prev, hbn) = bfs(self.start, self.end)
        # and dictionaries for bfs,
            if not succ:
                return None

            path = reconstruct_path(prev, self.start, self.end)
            # and sums the total cost of the
            #plength = len(path)-1   # calculated path.
            plength = 0
            for i in range(len(path)-1):
                r1,c1 = path[i]
                r2,c2 = path[i+1]
                plength+=self.calc_dist(r1,c1,r2,c2)
            pl=round(plength,2)
            #print("Path length: ", pl)
            #print("\n", path)
            path_n=[]
            for (i,j) in path:
                path_n.append((j,i))


        elif algo == "d":
            # Sets all necessary lists and
            (succ, prev, csf, hbn) = dijkstra(self.start, self.end)
        # and dictionaries for dijkstra,
            if not succ:
                return None

            path = reconstruct_path(prev, self.start, self.end)
            # and sums the total cost of the
            plength = csf[self.end]
            pl=round(plength,2)
            # calculated path.
            #print("Path length: ", plength)
            #print("\n", path)
            path_n=[]
            for (i,j) in path:
                path_n.append((j,i))

        elif algo == "a":
            # Sets all necessary lists and
            (succ, prev, csf, hbn) = a_star(self.start, self.end)
        # and dictionaries for a* pathfinder,
            if not succ:
                return None

            plength = csf[self.end]
            pl=round(plength,2)
            # and sums the total cost of the
            #print("Path length: ", plength)
            # calculated path.
            path = reconstruct_path(prev, self.start, self.end)
            #print("\n", path)
            path_n=[]
            for (i,j) in path:
                path_n.append((j,i))

        return pl, path_n


def reconstruct_path(previous, start, end):
    """
    Reconstructs the previous dictionary to be a list of nodes
    we can traverse and draw later.
    :param previous: dictionary
    :param start: Tile
    :param end: Tile
    :return: List path
    """
    curr = end
    path = [(curr.r, curr.c)]
    while curr != start:
        curr = previous[curr]
        path.append((curr.r, curr.c))
    # path.append(start)
    path.reverse()

    return path
