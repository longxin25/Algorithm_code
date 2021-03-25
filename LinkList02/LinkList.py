

class Node:

    def __init__(self, data=None, next_node=None) -> None:
        # 数据域
        self.__data = data
        # 指针域
        self.__next = next_node

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

class SingleLinklist:

    def __init__(self) -> None:
        # 头结点
        self.__head = Node()

    def insert_from_head(self, node):
        # 空链表（只有头结点）
        if self.__head.next == None:
            self.__head.next = node
        # 非空链表
        else:
            # 插入到第一个结点前面
            node.next = self.__head.next
            # 头结点指针指向新结点
            self.__head.next = node

    def insert_from_tail(self, node):
        temp = self.__head
        # 从前向后遍历，查找尾结点
        while temp.next != None:
            temp = temp.next
        # 尾结点的下一个结点设为待插入结点
        temp.next = node

    def find_by_value(self, value):
        # 当前待查找结点
        temp = self.__head
        # TODO 修复头结点的搜索问题
        while temp.next != None:
            if temp.next.data == value:
                # 返回的是目标结点的前一个结点！
                return temp
            else:
                temp = temp.next
        # 没找到
        return

    def delete_by_value(self, value):
        pre_node = self.find_by_value(value)
        pre_node.next = pre_node.next.next

    def insert_before_node(self, value, node):
        pre_node = self.find_by_value(value)
        # 特别注意：顺序不能颠倒，必须先把node挂上再移动上一个结点的指针，否则会造成指针丢失
        node.next = pre_node.next
        pre_node.next = node

    def insert_behind_node(self, value, node):
        pre_node = self.find_by_value(value)
        node.next = pre_node.next.next
        pre_node.next.next = node

    def travel(self):
        temp = self.__head
        while temp.next != None:
            print('{} '.format(temp.next.data), end='')
            temp = temp.next
        print('\n')

if __name__ == '__main__':
    s = SingleLinklist()
    s.insert_from_head(Node(1))
    s.insert_from_tail(Node(2))
    s.travel()
    s.insert_before_node(2, Node(3))
    s.travel()
    s.insert_behind_node(3, Node(4))
    s.travel()
    s.delete_by_value(1)
    s.travel()