

def count_sort(data):
    if len(data) <= 1:
        return
    # 桶的数量 = 最大值 + 1
    bucket_num = max(data) + 1
    # 建桶
    buckets = [0] * bucket_num
    # 开始计数
    for num in data:
        buckets[num] += 1
    # 排序：从桶里依次取数据，保证顺序从小到大
    sorted_index = 0
    for i in range(0, bucket_num):
        while buckets[i] > 0:
            data[sorted_index] = i
            sorted_index += 1
            buckets[i] -= 1
    return data


if __name__ == '__main__':
    origin_data = [2, 3, 1, 4, 7]
    sorted_data = count_sort(origin_data)
    print(sorted_data)