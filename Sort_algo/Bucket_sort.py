

def bucket_sort(data):
    length = len(data)
    if length <= 1:
        return
    # 桶的个数
    bucket_num = max(data) // 10 + 1
    # 创建n个桶
    bucket_list = [[] for i in range(0, bucket_num)]
    # 把每个元素装入对应的桶内
    for j in range(0, length):
        num = data[j] // 10
        bucket_list[num].append(data[j])
    result = []
    # 桶内排序，依次拼接
    for i in range(0, bucket_num):
        bucket_list[i].sort()
        result.extend(bucket_list[i])
    return result


if __name__ == '__main__':
    data = [22, 5, 11, 41, 45, 26, 23, 12, 7,34, 37]
    result_data = bucket_sort(data)
    print(result_data)