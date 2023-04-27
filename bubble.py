import time
start=time.time()
def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp

alist=[55,24,13,12,8]
print("before sorting:",alist)
bubble_sort(alist)
print("after sorting:",alist)
end=time.time()
print(f"Runtime of the program is{end-start}")

