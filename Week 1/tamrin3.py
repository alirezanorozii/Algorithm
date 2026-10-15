# مجموع اعداد زوج آرایه
def sum_even_numbers(arr):
    total_sum = 0                    # c1
    for i in range(len(arr)):        # c2
        if arr[i] % 2 == 0:          # c3
            total_sum += arr[i]      # c4
    return total_sum                 # c5

arr3 = [3, 10, 7, 4, 6]
print(sum_even_numbers(arr3))