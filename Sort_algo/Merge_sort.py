

def merge_sort(data):
    if len(data) <= 1:
        return data
    middle = len(data) // 2
    # 分割成左右两部分
    left, right = data[0:middle], data[middle:]
    # 递归进行分割，最后合并
    return merge(merge_sort(left), merge_sort(right))

# 拼接函数
def merge(left,right):
    # 存储结果
    result = []
    while left and right:
        # 向结果中添加较小元素
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


if __name__ == '__main__':
    origin_data = [2, 3, 1, 7, 5]
    result_data = merge_sort(origin_data)
    print(result_data)