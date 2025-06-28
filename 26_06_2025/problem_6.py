'''
1.sort student scores 
you are given array of integers representing studenbt score .
your task is to sort the array in asscending order using a basic sorting algorithmm(bubble sort/selection sort/insertion sort).
inputs
an integer m (1 <eual  n <eual 1000) - number of students
an array of n integers - the scores(0 < score < 100)

output:
sorted array of scores in ascending order 

input:5
scores:[55,90,70,60,80]
output:[55,60,70,80,90]

'''
def bubble_sort(scores):
    n = len(scores)
    for i in range(n):
        for j in range(0, n-i-1):
            if scores[j] > scores[j+1]:
                scores[j], scores[j+1]= scores[j+1],scores[j]
    return scores
scores = [55,90,70,60,80]
output =bubble_sort(scores)
print("Ountput:",output)













