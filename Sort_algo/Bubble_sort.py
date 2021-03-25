

# 冒泡排序：从小到大
def bubble_sort(data):
    length = len(data)
    if length <= 1:
        return
    for i in range(0, length):
        swaped = False
        for j in range(1, length - i):
            if data[j-1] > data[j]:
                data[j], data[j-1] = data[j-1], data[j]
                swaped = True
        if not swaped:
            break
    return data

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


if __name__ == '__main__':
    data = [3, 4, 1, 6, 2]
    sorted_data = bubble_sort(data)
    print(sorted_data)