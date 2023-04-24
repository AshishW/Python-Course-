
#this is incorrect way


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self, value):
        self.head = {
            "value": value,
            "next": None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1
        return self

    def print_list(self):
        linked_lst = []
        cur_node = self.head
        while cur_node != None:
            print(cur_node)
            linked_lst.append(cur_node["value"])
            cur_node = cur_node["next"]
        return LinkedList


list1 = LinkedList(1)
list1.append(10)
list1.print_list()
