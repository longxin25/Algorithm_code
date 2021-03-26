

# 冒泡排序：从小到大
def bubble_sort(data):
    length = len(data)
    if length <= 1:
        return
    for i in range(0, length):
        # 该趟冒泡是否发生了数据交换
        swaped = False
        # 开始冒泡，同时范围向前缩减
        for j in range(1, length - i):
            # 前面的数大
            if data[j-1] > data[j]:
                # 交换
                data[j], data[j-1] = data[j-1], data[j]
                swaped = True
        # 当此次冒泡未发生数据交换，则证明数据已有序，退出循环
        if not swaped:
            break


if __name__ == '__main__':
    data = [3, 4, 1, 6, 2]
    bubble_sort(data)
    print(data)