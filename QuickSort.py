def quick_sort(arr, low, high):
    if low < high:
        middle_index = partitions(arr, low, high)
        quick_sort(arr, low, middle_index - 1)
        quick_sort(arr, middle_index + 1 , high)

def partitions(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1    



def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    
    quick_sort(arr,0,len(arr)-1)
    
    print("Sorted array:", arr)
    
main()