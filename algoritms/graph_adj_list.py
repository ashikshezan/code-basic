class Node():

    def __init__(self, n):
        self.id = n
        self.connected_to = dict()

    def __repr__(self):
        return f'{self.id} connected-> {[x for x in self.connected_to]}'

    def add_connected_node(self, node_id, weight=0):
        self.connected_to[node_id] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, node):
        return self.connected_to[node]


class Graph():

    def __init__(self):
        self.total_node = 0
        self.node_list = dict()

    def add_node(self, node_id):
        self.total_node += 1
        new_node = Node(node_id)
        self.node_list[node_id] = new_node
        return new_node

    def get_nodes(self):
        return self.node_list.keys()

    def add_edge(self, start_node_id, end_node_id, weight):
        if start_node_id not in self.node_list:
            new_node = self.add_node(start_node_id)
        if end_node_id not in self.node_list:
            new_node = self.add_node(end_node_id)
        self.node_list[start_node_id].add_connected_node(end_node_id, weight)

    def __iter__(self):
        return self.node_list.values()

    def __contains__(self, node_id):
        return node_id in self.node_list

    def __str__(self):
        return f'Total nodes: {self.total_node} values {[j for i,j in self.node_list.items()]}'


graph = Graph()
for i in range(6):
    graph.add_node(i)

graph.add_edge(0, 3, 5)
print(graph)
