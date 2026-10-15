#۱. الگوریتم جستجوی خطی 

def linear_search(arr, x):
    for i in range(len(arr)):        # c1
        if arr[i] == x:              # c2
            return i                 # c3 (برگرداندن اندیس عنصر پیدا شده)
    return -1                        # c4 (اگر عنصر در آرایه نبود)


# ۲. الگوریتم جستجوی دودویی 
def binary_search(arr, x):
    low = 0                          # c1
    high = len(arr) - 1              # c2
    
    while low <= high:               # c3
        mid = (low + high) // 2      # c4 (پیدا کردن وسط بازه)
        if arr[mid] == x:            # c5
            return mid               # c6 (عنصر پیدا شد)
        elif arr[mid] < x:           # c7
            low = mid + 1            # c8 (حذف نیمه چپ بازه)
        else:
            high = mid - 1           # c9 (حذف نیمه راست بازه)
            
    return -1                        # c10 (اگر عنصر در آرایه نبود)


# جایگذاری آرایه نمونه و اجرای هر دو روش
# تعریف یک آرایه مرتب ۸ تایی و گشتن به دنبال عدد 23
arr = [2, 5, 8, 12, 16, 23, 38, 56]
x = 23

print("andis ba jostojooye khati peyda shod:", linear_search(arr, x))     # خروجی: 5
print("andis ba jostojooye binary peyfa shod:", binary_search(arr, x))  # خروجی: 5