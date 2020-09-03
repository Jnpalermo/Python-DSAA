def bubbleSort(arr):
    n = len(arr)

    # Traverse through elements in array
    for i in range(n-1):
        #range(n) also work but outer loop will repeat

            # Last i elements are in place
            for j in range(0, n-i-1):

                # traverse the array from 0 to n-i-1
                # swap if the element found is greater
                # than the next
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [24, 15, 99, 82, 6]

print("Unsorted array is:")
for i in range(len(arr)):
    print(arr[i])


bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print("%d" %arr[i])



