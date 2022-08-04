#binary search

#say you have an array [1,2,3,4,5,6,7,8,9]
arr = [1,2,3,4,5,6,7,8,9]

#search for 1
#iteration 1 = n/2; arr[n/2] == 1 ? No? Greater? Pick right hand side of array

#iteration k = n/2^k
#Big O is for worst case scenario
#Worst case is when n = 1, size of array gets to 1
#1 = n/2^k
#n = 2^k
#find K => log base2 n = log base2 2^k
#=> log n = k

#bigO of binary is O(log n)

def binarySearch(arr, item):
    n = len(arr)

    start = 0
    end = n
    #[1,2,3,4,5,6,7,8], search for 8
    while start <= end:
        midpoint = start + (end - start) // 2 
        #1 midpoint = 0 + 8 // 2 = 4
        #2 midpoint = (3 + 8) // 2 = 5
        if item == arr[midpoint]:
            return midpoint
            #1 arr[4] == 8? no

        if arr[midpoint] > item:
            end = midpoint - 1
            #1 arr[4] > 8 ? no
        else:
            start = midpoint + 1
            #1 start = 3

print(binarySearch([1,2,3,4],4))
