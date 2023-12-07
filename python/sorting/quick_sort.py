
def quick_sort(seq):
    if len(seq) < 1:
        return seq
    
    pivot = seq.pop()

    smaller_values = list(filter(lambda x: x <= pivot, seq))
    larger_values = list(filter(lambda x: x > pivot, seq))

    return quick_sort(smaller_values) + [pivot] + quick_sort(larger_values)
    


s = [5, 8, 2, 6, 9, 1, 0, 3,9,4,7]

print(quick_sort(s))
