

def quick_sort(data, low, high):
    if low < high:
        # 分区
        p = partition(data, low, high)
        # 对左右区间分别进行快速排序
        quick_sort(data, low, p-1)
        quick_sort(data, p+1, high)
    
# 分区方法类似选择排序
def partition(data, low, high):
    # 分区点， 分区下标
    pivot, j = data[low], low
    for i in range(low+1, high+1):
        # 小于分区点的元素移至前面
        if data[i] <= pivot:
            # 有序区间扩大
            j += 1
            # 交换，将小于分区点的元素换到有序区间尾部
            data[j], data[i] = data[i], data[j]
    # 最后把分区点移到有序区间的末端，使得分区点前面的元素全部小于分区点
    data[low], data[j] = data[j], data[low]
    return j


if __name__ == '__main__':
    data = [8, 9, 2, 6, 4]
    quick_sort(data, 0, len(data) - 1)
    print(data)