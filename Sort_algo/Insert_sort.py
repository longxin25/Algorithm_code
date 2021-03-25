

# 插入排序：从小到大
def insert_sort(data):
    length = len(data)
    if length <= 1:
        return
    # 起始已排序区间：data[0],未排序区间：data[1...n]
    for i in range(1, length):
        value = data[i]
        j = i - 1
        while j >= 0 and data[j] > value:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = value
    return data


if __name__ == '__main__':
    data = [2, 3, 1, 9, 8]
    sorted_data = insert_sort(data)
    print(sorted_data)