

class Stack:

    def __init__(self, capacity) -> None:
        self.__data = []
        self.__top = -1
        self.__capacity = capacity

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def top(self):
        return self.__top

    @top.setter
    def top(self, top):
        self.__top = top

    def push(self, value):
        if self.get_length() >= self.__capacity:
            return
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        if self.get_length() == 0:
            return
        value = self.data[self.top]
        del self.data[self.top]
        self.top -= 1
        return value

    def get_top(self):
        if self.top == -1:
            return
        return self.data[self.top]

    def get_length(self):
        i = 0
        while self.data[i]:
            i += 1
        return i
    