#linear srearch algorithm-checks each element one by one 
Arr = [5, 6, 2, 3, 4, 7, 8, 9, 10]
def linear_search(key, arr, length):
    for i in range(length):
        if arr[i] == key:
            return i
    return None
res = linear_search(10, Arr, len(Arr))
if res is None:
    print("Element not found")
else:
    print(f"Element found at index {res}")


print("------------------------------------------------------")
#checks with iterations
def linear_search(key, arr, length):
  count=0
  for i in range(length):
      count+=1
      print(f"{count} iteration")
      if arr[i] == key:
        print(f"element found at index {i}")
        break
  else:
        print("element not found")
res=linear_search(9,[5,6,9, 2, 3, 4, 7, 8, 9,10],9)