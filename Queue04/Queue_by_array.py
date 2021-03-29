

class Queue:
    
    def __init__(self, capacity) -> None:
        self.__data = []
        self.__capacity = capacity
        self.__head = 0
        self.__tail = 0

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

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

    def enqueue(self, value):
        if self.tail == self.__capacity:
            if self.head == 0:
                return
            else:
                # 数据搬移
                for i in range(0, self.tail - self.head):
                    self.data[i] = self.data[i + self.head]
                self.tail = self.tail - self.head
                self.head = 0

        self.data[self.tail] = value
        self.tail += 1

    def dequeue(self):
        if self.head == self.tail:
            return
        value = self.data[self.head]
        self.head += 1
        return value