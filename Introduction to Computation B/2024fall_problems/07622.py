# merge sort 求排列的逆序数
minimum = 0
def mergesort(arr):
    global minimum
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        Lptr = Rptr = ptr = 0
        while len(left) > Lptr and len(right) > Rptr:
            if left[Lptr] <= right[Rptr]:
                arr[ptr] = left[Lptr]
                Lptr += 1
            else:
                arr[ptr] = right[Rptr]
                Rptr += 1
                minimum += len(left)-Lptr
            ptr += 1
        while len(left) > Lptr:
            arr[ptr] = left[Lptr]
            ptr += 1
            Lptr += 1
        while len(right) >Rptr:
            arr[ptr] = right[Rptr]
            ptr += 1
            Rptr += 1

n = int(input())
arr = list(map(int, input().split()))
mergesort(arr)
print(minimum)

### 感觉好难，实在不能掌握