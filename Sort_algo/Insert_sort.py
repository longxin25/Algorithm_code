

# 插入排序：从小到大
def insert_sort(data):
    length = len(data)
    if length <= 1:
        return
    # 起始已排序区间：data[0],未排序区间：data[1...n]
    for i in range(1, length):
        # 待插入元素
        value = data[i]
        # 已排序区间末尾
        j = i - 1
        # 从已排序区间末尾向前遍历，将比待插入元素大的数全部向后搬移
        while j >= 0 and data[j] > value:
            data[j+1] = data[j]
            j -= 1
        # 搬移结束，插入元素
        data[j+1] = value


if __name__ == '__main__':
    data = [2, 3, 1, 9, 8]
    insert_sort(data)
    print(data)