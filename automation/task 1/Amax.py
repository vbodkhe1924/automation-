arr = []
n = len(arr)
def Max(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

Maximun = Max(arr, n)
print("Largest in given array ", Maximun)

