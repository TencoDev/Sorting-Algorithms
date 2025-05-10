def merge(arr1, arr2):
    final_arr = []
    i, j = 0, 0
    while i < len(arr1)  and j < len(arr2):
        if arr1[i] <= arr2[j]:
            final_arr.append(arr1[i])
            i += 1
        else:
            final_arr.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        final_arr.append(arr1[i])
        i += 1
        
    while j < len(arr1):
        final_arr.append(arr2[j])
        j += 1
        
    return final_arr

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    first_half = arr[:len(arr)//2]
    second_half = arr[len(arr)//2:]
    sorted_first_half = merge_sort(first_half)
    sorted_second_half = merge_sort(second_half)
    return merge(sorted_first_half, sorted_second_half)

def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    
    arr = merge_sort(arr)
    
    print("Sorted array:", arr)
    
main()
    