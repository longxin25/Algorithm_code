

# 选择排序：从小到大
def select_sort(data):
    length = len(data)
    if length <= 1:
        return
    for i in range(0, length):
        # 求i到length(未排序区间)的最小值
        min_index = i
        min_value = data[i]
        for j in range(i, length):
            if data[j] < min_value:
                min_index = j
                min_value = data[j]
        # 通过交换把最小值放到首位
        data[i], data[min_index] = data[min_index], data[i]
    return data


if __name__ == '__main__':
    data = [2, 5, 4, 6, 9]
    select_sort(data)
    print(data)

                