def bubble_sort(arr):
    swapping = True
    end = len(arr)
    while swapping:
        swapping = False
        for i in range(1, end):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swapping = True
    end -= 1
    return arr


def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    
    bubble_sort(arr)
    
    print("Sorted array:", arr)
    
main()