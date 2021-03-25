import itertools


def count_sort(data):
    if len(data) <= 1:
        return
    counts_array = [0] * (max(data) + 1)
    for num in data:
        counts_array[num] += 1
    counts_array = list(itertools.accumulate(counts_array))

    temp = [0] * len(data)
    for num in reversed(data):
        index = counts_array[num] - 1
        temp[index] = num
        counts_array[num] -= 1

    return temp


if __name__ == '__main__':
    origin_data = [2, 3, 1, 2, 3, 4, 7]
    sorted_data = count_sort(origin_data)
    print(sorted_data)