

def BuildMaxHeap(data):
    for i in range(len(data) // 2, -1, -1):
        Heapify(data, i)

def Heapify(data, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < length and data[left] > data[largest]:
        largest = left
    if right < length and data[right] > data[largest]:
        largest = right
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        Heapify(data, largest)

def heap_sort(data):
    global length
    length = len(data)
    BuildMaxHeap(data)
    for i in range(length-1, 0, -1):
        data[0], data[i] = data[i], data[0]
        length -= 1
        Heapify(data, 0)
    return data


if __name__ == '__main__':
    data = [4, 2, 1, 6, 8]
    result = heap_sort(data)
    print(result)