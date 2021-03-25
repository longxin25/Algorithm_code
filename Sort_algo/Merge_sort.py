

# 分解
def merge_sorted(data_list, low, high):
    if low < high:
        # 折半分成两个子数组
        mid = low + (high - low) // 2
        merge_sorted(data_list, low, mid)
        merge_sorted(data_list, mid+1, high)
        merge(data_list, low, mid, high)
        

# 合并
def merge(data_list, low, mid, high):
    i, j = low, mid+1
    temp = []
    while i <= mid and j <= high:
        # 依次添加较小的子数组
        if data_list[i] < data_list[j]:
            temp.append(data_list[i])
            i += 1
        else:
            temp.append(data_list[j])
            j += 1
    start = i if i <= mid else mid
    end = mid if i <= mid else high
    temp.extend(data_list[start:end+1])
    data_list[low:high+1] = temp


if __name__ == '__main__':
    origin_data = [2, 3, 1, 7, 5]
    merge_sorted(origin_data, 0, len(origin_data) - 1)
    print(origin_data)