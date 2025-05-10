def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", arr)
    selection_sort(arr)
    print("Sorted array:", arr)

def selection_sort(arr):
    for i in range(0, len(arr)):
        smallest_index = i
        for j in range(smallest_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        
main()