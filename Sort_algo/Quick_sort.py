

def quick_sort(data, low, high):
    if low < high:
        p = partition(data, low, high)
        quick_sort(data, low, p-1)
        quick_sort(data, p+1, high)
    
def partition(data, low, high):
    pivot, j = data[low], low
    for i in range(low+1, high+1):
        if data[i] <= pivot:
            j += 1
            data[j], data[i] = data[i], data[j]
    data[low], data[j] = data[j], data[low]
    return j


if __name__ == '__main__':
    data = [1, 9, 2, 6, 4]
    quick_sort(data, 0, len(data) - 1)
    print(data)