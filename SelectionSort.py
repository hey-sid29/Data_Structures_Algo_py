def SelectionSort(arr, n):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min]):
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp


if __name__ == '__main__':
    arr = [2, 7, 4, 1, 5, 3]
    SelectionSort(arr, len(arr))
    for i in range(len(arr)):
        print(arr[i], end= " ")