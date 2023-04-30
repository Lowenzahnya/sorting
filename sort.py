import random


def findsmalest(arr):
    smallest_index = 0
    smallest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def sorting(arr):
    new_arr = []
    for i in range(len(arr)):
        small = findsmalest(arr)
        new_arr.append(arr.pop(small))
    return new_arr


arr = [random.randint(0, 100) for i in range(15)]
print(arr)
print(f'{sorting(arr)}\n')
