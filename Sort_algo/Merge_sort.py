

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left, right = arr[0:middle], arr[middle:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left,right):
    result = []
    while left and right:
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