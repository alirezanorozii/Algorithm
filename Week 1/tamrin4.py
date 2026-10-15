
# تعریف توابع (تمرین‌های ۱، ۲ و ۳)

# تمرین ۱: پیدا کردن کوچک‌ترین عنصر
def find_min(arr):
    min_val = arr[0]                 # c1
    for i in range(1, len(arr)):     # c2
        if arr[i] < min_val:         # c3
            min_val = arr[i]         # c4
    return min_val                   # c5


# تمرین ۲: شمارش تعداد تکرار x
def count_occurrences(arr, x):
    count = 0                        # c1
    for i in range(len(arr)):        # c2
        if arr[i] == x:              # c3
            count += 1               # c4
    return count                     # c5


# تمرین ۳: مجموع اعداد زوج آرایه
def sum_even_numbers(arr):
    total_sum = 0                    # c1
    for i in range(len(arr)):        # c2
        if arr[i] % 2 == 0:          # c3
            total_sum += arr[i]      # c4
    return total_sum                 # c5


# تمرین ۴: اجرای ۴ تست (عادی و مرزی) برای هر الگوریتم

#   تست برای تمرین ۱ 
print(find_min([14, 8, 23, 5, 19]))   # تست ۱: حالت عادی
print(find_min([42]))                 # تست ۲ (مرزی): آرایه تک‌عنصری
print(find_min([9, 9, 9, 9]))         # تست ۳ (مرزی): همه عناصر تکراری
print(find_min([-5, -1, -10, 0]))     # تست ۴ (مرزی): شامل اعداد منفی

print("-" * 20)

#   تست برای تمرین ۲ 
print(count_occurrences([7, 2, 7, 9, 7, 4], 7))   # تست ۱: حالت عادی
print(count_occurrences([], 5))                   # تست ۲ (مرزی): آرایه خالی
print(count_occurrences([1, 2, 3], 9))            # تست ۳ (مرزی): عدد x در آرایه نیست
print(count_occurrences([7, 7, 7], 7))            # تست ۴ (مرزی): همه عناصر برابر x هستند

print("-" * 20)

#   تست برای تمرین ۳ 
print(sum_even_numbers([3, 10, 7, 4, 6]))         # تست ۱: حالت عادی
print(sum_even_numbers([]))                       # تست ۲ (مرزی): آرایه خالی
print(sum_even_numbers([1, 3, 5, 7]))             # تست ۳ (مرزی): همه اعداد فرد هستند
print(sum_even_numbers([-4, -2, 0, 6]))           # تست ۴ (مرزی): اعداد زوج منفی و صفر