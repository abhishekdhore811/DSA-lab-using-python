class Graph:
    def __init__(self):
        self.v = 0
        self.e = 0
        self.G = [[0 for i in range(10)] for j in range(10)]

    def create(self):

        self.v = int(input("Enter no of vertices: "))
        self.e = int(input("Enter no of edges: "))

        for i in range(self.e):
            print(f"Enter Edge {i+1} with its weight: ")

            u = int(input("Enter start vertex: "))
            v = int(input("Enter end vertex: "))
            w = int(input("Enter weight: "))

            self.G[u][v] = self.G[v][u] = w

    def display(self):
        print("\nAdjacency Matrix:")

        for i in range(self.v):
            for j in range(self.v):
                print(self.G[i][j], end=" ")
            print()


class Stack:
    def __init__(self):
        self.TOP = -1
        self.st = [0] * 100

    def push(self, x):
        if self.TOP == 99:
            print("Stack Overflow")
            return

        self.TOP += 1
        self.st[self.TOP] = x

    def pop(self):
        if self.TOP == -1:
            print("Stack Underflow")
            return

        x = self.st[self.TOP]
        self.TOP -= 1
        return x


def DFS(G, start):

    visited = [False] * G.v

    S = Stack()

    S.push(start)

    print("\nDFS Traversal:")

    while S.TOP != -1:

        u = S.pop()

        if visited[u] == False:

            print(u, end=" ")

            visited[u] = True

            # Push adjacent vertices into stack
            for v in range(G.v - 1, -1, -1):

                if G.G[u][v] != 0 and visited[v] == False:
                    S.push(v)


# Main
g = Graph()

g.create()
g.display()

start = int(input("\nEnter starting vertex: "))

DFS(g, start)