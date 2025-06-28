#Binary search
def binarySearch(arr, target,length):
  low = 0
  high = length - 1
  while (len(arr)>1):
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid
    if arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return None
arrays= [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_ = 5
length = 10
result = binarySearch(arrays, target_ , length)
if result != None:
  print("Found at index", result)
else:
  print("Not found")




def BinarySearch(Arr, Target,pivot=0):
    if(len(Arr)==0):
        print("Array does not exist")
    else:
        Mid=len(Arr)//2
    if Target==Arr[Mid]:
        print(f"Element Found at {Mid+pivot} index")
    else:
        if (Target<Arr[Mid]):
            return BinarySearch(Arr[:Mid], Target,pivot)
        elif(Target>Arr[Mid]):
            return BinarySearch(Arr[Mid+1:], Target,pivot+Mid+1)
        else:
            print("Element does not exist")
Output=BinarySearch([1,2,3,4,5],4)

