#پیداکردن کوچکترین عنصر
def find_min(arr):
    min_val = arr[0]                 # c1
    for i in range(1, len(arr)):     # c2
        if arr[i] < min_val:         # c3
            min_val = arr[i]         # c4
    return min_val                   # c5

arr1 = [14, 8, 23, 5, 19]
print(find_min(arr1))