# packing problem 
toys_list  = input("Enter a list of toys : ")
list = []
while True:
    print("1. list of toy names ")
    print("2. Remove dublicates")
    print("3. View the final sorted toys list")
    print("-------------")
    for num in toys_list:
        if num not in list:
            list.remove(toys_list)
    print("given_list:", toys_list)
    print("List after removing duplicates:", list)


    #incomplete