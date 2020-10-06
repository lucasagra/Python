"""
Author  : https://github.com/lucasagra
Date    : October 05, 2020

This is a implementation to the minimum broadcast time problem
(for a tree data structure)
Given a tree, how many steps does it take to a signal broadcast from
a defined root to all vertices.
Each step, each vertex can send the signal to one neighbour
"""


class Graph:
    def __init__(self, root):
        self.root = root
        self.edges = dict()

    def add_edge(self, u, w):
        """
        Add undirected edge between vertices u, w
        """
        if self.edges.get(w) is not None:
            self.edges[w].append(u)
        else:
            self.edges[w] = [u]

        if self.edges.get(u) is not None:
            self.edges[u].append(w)
        else:
            self.edges[u] = [w]

    def set_root(self, root):
        self.root = root

    @staticmethod
    def mbt_parent(ls) -> int:
        """
        Calculate minimum number of moves given a list of children mbt
        :param ls: list of children mbt
        :return: parent mbt

        >>> t = Graph(0)
        >>> t.mbt_parent([1, 1, 1])
        3
        >>> t.mbt_parent([3, 2, 1])
        3
        >>> t.mbt_parent([3, 3, 3])
        5
        >>> t.mbt_parent([10, 10, 10, 3, 3, 3, 3, 3])
        12
        """
        ls = sorted(ls, reverse=True)
        size = len(ls)

        dif = []
        for i in range(size):
            dif.append(size - i - ls[i])

        if min(dif) <= 0:
            return size + abs(min(dif))
        else:
            return max(ls)

    def get_mbt(self, v, visited) -> int:
        """
            :param v: current vertex
            :param visited: set of visited vertices
            :return: recursively returns minimum number of steps from the initial
                     vertex to broadcast the signal through the tree
        """
        visited.add(v)
        children = len(self.edges[v]) - 1
        if v != self.root and children == 0:
            return 1

        return 1 + self.mbt_parent(
            [
                self.get_mbt(vertex, visited)
                for vertex in self.edges[v]
                if vertex not in visited
            ]
        )

    def mbt(self) -> int:
        visited = set()
        return self.get_mbt(self.root, visited) - 1


if __name__ == "__main__":

    tree = Graph(16)

    tree.add_edge(1, 4)
    tree.add_edge(1, 3)
    tree.add_edge(2, 7)
    tree.add_edge(2, 12)
    tree.add_edge(3, 8)
    tree.add_edge(5, 17)
    tree.add_edge(6, 19)
    tree.add_edge(5, 13)
    tree.add_edge(6, 20)
    tree.add_edge(7, 10)
    tree.add_edge(7, 13)
    tree.add_edge(8, 12)
    tree.add_edge(8, 18)
    tree.add_edge(9, 22)
    tree.add_edge(11, 16)
    tree.add_edge(11, 14)
    tree.add_edge(14, 21)
    tree.add_edge(15, 18)
    tree.add_edge(15, 22)
    tree.add_edge(18, 20)
    tree.add_edge(21, 22)

    print(tree.mbt())

    tree.set_root(18)
    print(tree.mbt())
