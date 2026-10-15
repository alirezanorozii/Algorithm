#شمارش تعداد تکرار
def count_occurrences(arr, x):
    count = 0                        # c1
    for i in range(len(arr)):        # c2
        if arr[i] == x:              # c3
            count += 1               # c4
    return count                     # c5

arr2 = [7, 2, 7, 9, 7, 4]
print(count_occurrences(arr2, 7))