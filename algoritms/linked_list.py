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
        return list_representaion[:-4]  # just cutting the last arrow sign

    def __len__(self):
        return self.length

    def __iter__(self):
        temporary_node = self.head
        while temporary_node is not None:
            yield temporary_node
            temporary_node = temporary_node.next_node

    def add_at_head(self, data):
        node = Node(data=data, next_node=self.head)
        self.head = node
        self.update_list_length()

    def add_node_at_end(self, data):
        node = Node(data=data)  # creating a new node first
        if self.head is None:  # checking if the node is empty
            self.head = node
        else:  # if not empty
            temporary_node = self.head
            while temporary_node is None:
                temporary_node = temporary_node.next_node
            temporary_node.next_node = node

        self.update_list_length()  # increasing the lenght anyway

    def add_node_at_index(self, index, data):
        self.validate_index(index)
        new_node = Node(data=data)
        temporary_node = self.head
        for i, node in enumerate(self):
            if i == index - 1:
                new_node.next_node = node.next_node
                node.next_node = new_node
                break

        self.update_list_length()

    def remove_node_at_index(self, index):
        self.validate_index(index)
        for i, node in enumerate(self):
            if i == index - 1:
                node.next_node = node.next_node.next_node
                break
        self.update_list_length(0)

    def update_list_length(self, add=1):
        if add:
            self.length += 1
        if not add:
            self.length -= 1

    def validate_index(self, index):
        if index < 0 or index >= self.length:
            raise Exception("Index is out of range")
        else:
            return True


lst = LinkedList()
# lst.add_node_at_index(4, 1)
lst.add_at_head(12)
lst.add_node_at_end(200)
lst.add_node_at_index(1, 12)
lst.add_node_at_index(2, 199)
lst.add_node_at_index(2, 222)
print(len(lst))
print(lst)
lst.remove_node_at_index(3)
print(lst)
print(len(lst))
# for i in lst:
# print(i.data)
