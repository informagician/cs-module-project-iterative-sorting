# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        if smallest_index != i:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here
    output = []

    for i in arr:
        output[i] = 0
    
    for j in range(1,len(arr)):
        output[arr[j]] = output[arr[j]] + 1

    for i in range(len(output)):
        output[i] = output[i] + output[i-1]
    
    for j in range(len(arr))
    return arr
