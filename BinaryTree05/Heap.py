

class Heap:
    def __init__(self, capacity) -> None:
        self.data = []
        self.capacity = capacity
        self.count = 0

    # 插入元素
    def Insert(self, value):
        if self.count == self.capacity:
            return
        self.count += 1
        self.data[self.count] = value
        # 自下而上堆化
        self.Heapify_down(self.count)
    
    # 移除堆顶元素
    def RemoveMax(self):
        if self.count == 0:
            return -1
        self.data[1] = self.data[self.count]
        self.count -= 1
        self.Heapify_up(self.count, 1)

    # 自下而上堆化
    def Heapify_down(self, i):
        # 从底部开始逐个与父节点比较，若父节点小则进行交换
        while i // 2 > 0 and self.data[i] > self.data[i // 2]:
            self.data[i], self.data[i // 2] = self.data[i // 2], self.data[i]
            i = i // 2
    
    # 自上而下堆化
    def Heapify_up(self, n, i):
        while True:
            # 左子树
            left = i * 2
            # 右子树
            right = i * 2 + 1
            # 最大元素
            largest = i
            # 左子树存在且更大
            if left <= n and self.data[largest] < self.data[left]:
                # 左子树设为最大元素
                largest = left
            # 右子树存在且更大
            if right <= n and self.data[largest] < self.data[right]:
                # 右子树设为最大元素
                largest = right
            # 没有发生交换，堆化结束
            if largest == i:
                break
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            i = largest
        return