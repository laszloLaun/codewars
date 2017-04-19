def sel_reverse(arr, l):
    result = []
    if l >= len(arr):
        result = sorted(arr, reverse=True)
    elif l == 0:
        result = sorted(arr)
    else:
        for i in range(0, len(arr), l):
            result += sorted(arr[i:i + l], reverse=True)
    return result
sel_reverse([1, 2, 3, 4, 5, 6], 3)
