

class Array:

    def __init__(self, capacity: int) -> None:
        # 数据
        self.__data = []
        # 容量
        self.__capacity = capacity

    def find(self, index: int) -> object:
        try:
            return self.__data[index]
        except IndexError:
            return None

    def delete(self, index: int) -> bool:
        try:
            self.__data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: int) -> bool:
        # 溢出
        if len(self.__data) >= self.__capacity:
            return False
        else:
            self.__data.insert(index, value)
            return True

    def print_all(self) -> None:
        for item in self.__data:
            print(item)
