def linear_search(arr, target):
    # Your code here
    for x in range(0, len(arr)):
        if arr[x] == target:
            return x


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    lower = 0
    higher = len(arr)

    while lower < higher:
        middle = (lower + higher) // 2
        if arr[middle] == target:
            return middle
        elif target > arr[middle]:
            lower = middle
        else:
            higher = middle + 1



    return -1  # not found
