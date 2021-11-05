def binarySearch(arr:list,key:int)->int:
    left=0
    right=len(arr)
    if left>right:
        return -1
    while left<=right:
        midpoint=left+(right-left)//2
        if arr[midpoint]==key:
            return midpoint
        elif arr[midpoint]<key:
            left=midpoint+1
        elif arr[midpoint]>key:
            right=midpoint-1

            
dizi=[34,45,56,67,78,89,98,123,234,456,678]
sayi=123
print(binarySearch(dizi, sayi))