

def shell_sort(data):
    length = len(data)
    if length <= 1:
        return
    # 增量因子
    gap = 1
    while gap < length / 3:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, length):
            value = data[i]
            j = i - gap
            while j >= 0 and data[j] > value:
                data[j+gap] = data[j]
                j -= gap
            data[j+gap] = value
        gap = gap // 3
    

if __name__ == '__main__':
    data = [2, 1, 3, 7, 6]
    shell_sort(data)
    print(data)