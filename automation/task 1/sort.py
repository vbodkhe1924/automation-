def Sort(array):
  for i in range(len(array)):
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

arr1 = [10,5,6,7,67]

Sort(arr1)

print('Sorted Array in Ascending Order:')
print(arr1)