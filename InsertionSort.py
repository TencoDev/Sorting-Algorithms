def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    
    insertion_sort(arr)
    
    print("Sorted array:", arr)
    
main()