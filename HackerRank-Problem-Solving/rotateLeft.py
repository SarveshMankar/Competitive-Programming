def rotateLeft(d, arr):
    # Write your code here
    for i in range(d):
        arr.append(arr[0])
        arr.pop(0)
    
    return arr