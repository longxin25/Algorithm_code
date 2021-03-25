

class Node:

    def __init__(self, data=None, next=None) -> None:
        self.__data = data
        self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

class Stack:

    def __init__(self) -> None:
        self.__top = Node()

    @property
    def top(self):
        return self.__top

    @top.setter
    def top(self, top):
        self.__top = top

    def push(self, node):
        # 空栈（只有头结点）
        if self.top.next == None:
            self.top.next = node
        else:
            node.next = self.top.next
            self.top.next = node

    def pop(self):
        if self.top.next == None:
            return
        else:
            value = self.top.next.data
            self.top.next = self.top.next.next
            return value

            
