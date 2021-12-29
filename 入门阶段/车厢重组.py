sum=0
def bubbleSort(arr,n):
    global sum 
    # 遍历所有数组元素
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            if arr[j] > arr[j+1] :
                sum+=1
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return sum
if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    print(bubbleSort(arr,n))