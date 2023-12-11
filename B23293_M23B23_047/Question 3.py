# Sorting algorithm 1: Selection Sort
unsorted_list = [14, 27, 8, -42, 11, 35, -9, 56, 23]

# Iterate through each element in the list
for i in range(len(unsorted_list)):
    # Assume the current index is the minimum
    k = i
    
    # Iterate through the remaining elements to find the minimum
    for j in range(i, len(unsorted_list)):
        # Compare the current element with the assumed minimum
        if unsorted_list[j] < unsorted_list[k]:
            # If a smaller element is found, update the minimum index
            k = j
    
    # Swap the current element with the minimum element found
    unsorted_list[i], unsorted_list[k] = unsorted_list[k], unsorted_list[i]

# Print the sorted list using Selection Sort
print("Sorted List (Selection Sort):", unsorted_list)


# Sorting algorithm 2: QuickSort
def quick_sort(arr):
    # Base case: If the list has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose the first element as the pivot
        pivot = arr[0]
        
        # Divide the list into two sublists: elements <= pivot and elements > pivot
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        
        # Recursively apply QuickSort to the sublists and combine the results
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Example usage of QuickSort
unsorted_list1 = [14, 27, 8, -42, 11, 35, -9, 56, 23]
sorted_list = quick_sort(unsorted_list1)

# Print the unsorted and sorted lists
print("Sorted List (QuickSort):", sorted_list)

#Complexity is O(nlogn)