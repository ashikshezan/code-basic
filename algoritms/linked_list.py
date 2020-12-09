class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        list_representaion = str()
        if self.head is None:
            list_representaion = "List is empty!"
        else:
            temporary_node = self.head
            while temporary_node is not None:
                list_representaion += f'{temporary_node.data} -> '
                temporary_node = temporary_node.next_node
        return list_representaion

    def __len__(self):
        return self.length

    def add_at_head(self, data):
        node = Node(data=data, next_node=self.head)
        self.head = node
        self.length += 1

    def add_node_at_end(self, data):
        node = Node(data=data)  # creating a new node first
        if self.head is None:  # checking if the node is empty
            self.head = node
        else:  # if not empty
            temporary_node = self.head
            while temporary_node is None:
                temporary_node = temporary_node.next_node
            temporary_node.next_node = node

        self.length += 1  # increasing the lenght anyway

    def add_node_at_index(self, index, data):
        if index < 0 or index >= self.length:
            raise Exception("Invalide index!")
        temporary_node = self.head


lst = LinkedList()
# lst.add_node_at_index(4, 1)
lst.add_at_head(12)
lst.add_node_at_end(200)
print(len(lst))
print(lst)
