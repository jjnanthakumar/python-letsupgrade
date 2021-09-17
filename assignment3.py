# 1. Write a program to implement insertion sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j-=1
        arr[j + 1] = key
        
    print(arr)
 
insertion_sort([12, 11, 13, 5, 6])
'''
2. def fun1(a,b=0, *args,**kwargs)
        ?? 
        
fun1(?)

Pass the argument to function fun1 and print those arguments

'''

def fun1(a,b=0, *args,**kwargs):
    print(a)
    print(args) # (30, 40)
    print(kwargs) # {'c': 100, 'd': 900}

fun1(10, 20,30,40, c=100, d=900)