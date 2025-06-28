#Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.
arr = [10,20,65,45,7,100,46,105]
print(f"orginal array:{arr}")
count  = 0
for i in range(len(arr)):
    Flag = False
    for j in range (len(arr)-1):
        if(arr[j]>arr[j+1]):
            arr[i],arr[j+1] = arr[j+1],arr[j]
            print(arr)
            Flag=True
    if Flag == False:
        break
print(f"sorted{arr}")