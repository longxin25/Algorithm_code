

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


class Queue:

    def __init__(self) -> None:
        self.__head = Node()
        self.__tail = Node()

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, head):
        self.__head = head

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, tail):
        self.__tail = tail

    def enqueue(self, node):
        if self.tail.next == None:
            self.head.next = node
            self.tail.next = node
        else:
            self.tail.next.next = node
            self.tail.next = node

    def dequeue(self):
        if self.tail.next == None:
            return
        else:
            value = self.head.next.data
            self.head.next = self.head.next.next
            return value

    def travel(self):
        temp = self.head
        while temp.next != None:
            print('{} '.format(temp.next.data), end='')
            temp = temp.next
        print('\n')


if __name__ == '__main__':
    q = Queue()
    origin_data = [4, 2, 3, 1, 8]
    for data in origin_data:
        q.enqueue(Node(data))
    q.travel()
    for j in range(0, 5):
        print('{} '.format(q.dequeue()), end='')