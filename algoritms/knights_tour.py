from graph import Graph, Node, dfs, bfs

graph = Graph()
for i in range(16):
    graph[str(i)] = Node()
count = 0


def knight_graph(board_size):
    for row in range(board_size):
        for col in range(board_size):
            node_id = generate_node(row, col, board_size)
            new_moves = calculate_valid_moves(row, col, board_size)
            for coord in new_moves:
                move_id = generate_node(coord[0], coord[1], board_size)
                graph.add_edge(node_id, move_id)


def generate_node(row, col, board_size):
    id = str((row * board_size) + col)
    return id


def calculate_valid_moves(row, col, size):
    new_moves = []
    valid_moves = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]

    for coord in valid_moves:
        x = row + coord[0]
        y = col + coord[1]

        if valid_coord(x, size) and valid_coord(y, size):
            new_moves.append((x, y))
    return new_moves


def valid_coord(x, size):
    if x >= 0 and x < size:
        return True
    else:
        return False


knight_graph(4)

# for i in graph:
#     print(graph[i])

# bfs(graph, graph['12'])
dfs(graph, graph['0'])
