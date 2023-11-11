def binary_search(sequence, item):
    result = None
    low = 0
    high = len(sequence) - 1

    while low <= high:
        mid = (low + high) // 2
        if sequence[mid] == item:
            result = mid
            high = mid - 1
        elif sequence[mid] > item:
            high = mid -1
        else:
            low = mid + 1
    return result 
