

def BuildMaxHeap(data):
    for i in range(len(data) // 2, -1, -1):
        Heapify(data, i)

# 堆化
def Heapify(data, i):
    # 左右子树下标
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    # 调整最大值
    if left < length and data[left] > data[largest]:
        largest = left
    if right < length and data[right] > data[largest]:
        largest = right
    # 将堆顶（最大值）和堆尾交换
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        Heapify(data, largest)

def heap_sort(data):
    global length
    length = len(data)
    # 构建最大堆
    BuildMaxHeap(data)
    for i in range(length-1, 0, -1):
        data[0], data[i] = data[i], data[0]
        # 尺寸减一
        length -= 1
        # 调整新的顶端元素至合适位置
        Heapify(data, 0)
    return data


if __name__ == '__main__':
    data = [4, 2, 1, 6, 8]
    result = heap_sort(data)
    print(result)