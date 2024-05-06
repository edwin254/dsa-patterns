# # quicksort uses divide-and-conquer, and so it's a recursive algorithm. 
# # The way that quicksort uses divide-and-conquer is a little different from how merge sort does. 
# In merge sort, the divide step does hardly anything, 
# and all the real work happens in the combine step. 
# Quicksort is the opposite: all the real work happens in the divide step.
# In fact, the combine step in quicksort does absolutely nothing.
def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    
    pivot = seq.pop()

    smaller_values = list(filter(lambda x: x <= pivot, seq))
    larger_values = list(filter(lambda x: x > pivot, seq))

    return quick_sort(smaller_values) + [pivot] + quick_sort(larger_values)
    


s = [5, 8, 2, 6, 9, 1, 0, 3,9,4,7]

print(quick_sort(s))
