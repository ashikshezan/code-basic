from collections import UserDict


class Node(UserDict):

    def __init__(self):
        super().__init__(self)
        self.color = False
        self.id = id(self)
        self.distance = 0

    def __setitem__(self, key, weight=None):
        self.data[str(key)] = weight

    def __repr__(self):
        items = str(self.data.keys())
        return f'Node {self.id} --> {items[11:-2]}'
        # return self.id


class Graph(UserDict):

    def __setitem__(self, key, value):
        if isinstance(value, Node):
            self.data[key] = value
            self.data[key].id = key
        else:
            raise ValueError('Graph takes only Node instances')

    def add_edge(self, from_node, to_node, weight=0):
        if to_node and from_node in self.data:
            self.data[from_node][to_node] = weight

    def remove_edge(self, from_node, to_node):
        if to_node and from_node in self.data:
            del self.data[from_node][to_node]


def graph_sample():
    graph = Graph()
    for i in range(1, 8):
        graph[str(i)] = Node()
    graph.add_edge('1', '2')
    graph.add_edge('1', '3')
    graph.add_edge('1', '5')
    graph.add_edge('2', '6')
    graph.add_edge('2', '4')
    graph.add_edge('3', '4')
    graph.add_edge('3', '7')
    graph.add_edge('5', '4')
    # graph.add_edge('6', '8')
    # graph.add_edge('8', '9')
    # graph.add_edge('7', '10')
    return graph


def bfs(graph, start_node):
    import queue
    for i in graph:
        graph[i].color = False
    result = []
    q = queue.Queue()
    start_node.distance = 0
    q.put(start_node)
    result.append(start_node)
    while(not q.empty()):
        temp = q.get()
        for i in temp:
            if not graph[i].color:
                graph[i].color = True
                q.put(graph[i])
                result.append(graph[i])
                graph[i].distance += temp.distance+1
            temp.color = True
    for i in result:
        print(f'{i}-->{i.distance}')
    print(len(result))


def dfs(graph):
    result = []
    for i in graph:
        graph[i].color = False

    def dfs_nodes():
        for i in graph:
            if not graph[i].color:
                dfs_visit(graph, graph[i])

    def dfs_visit(graph, node):
        node.color = True
        for i in node:
            if not graph[i].color:
                dfs_visit(graph, graph[i])
        result.append(node)
    dfs_nodes()
    for i in result:
        print(i)


def knight_tour(graph, start):
    for i in graph:
        graph[i].color = False

    stack.append(start)
    result = []
    stack = [start]
    limit = 0

    def dfs_nodes():
        while limit <= len(graph):
            if not graph[i].color:
                dfs_visit(graph, start)

    def dfs_visit(graph, node):
        node.color = True
        for i in node:
            if not graph[i].color:
                dfs_visit(graph, stack[-1])
        result.append(node)
    dfs_nodes()
    for i in result:
        print(i)


if __name__ == "__main__":
    g = Graph()
    graph = graph_sample()

    dfs(graph)
    print('=========')
    bfs(graph, graph['1'])
