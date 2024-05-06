"""
FOR EACH ITEM:
 - LOOP SEQUENCE FINDING SMALLEST VALUE INDEX
 - STARTING FROM IT'S NEXT ITEM YO THE END OF SEQUENCE
 - COMPARE THE SMALLEST VALUE TO THE CURERENT SMALLEST VALUE

"""

def sort_squence(seq: list) -> list:

    def get_minIndex(start_index, seq):
        min_index = start_index

        for j in range(start_index+1 , len(seq)):

            if seq[min_index] > seq[j]:
                min_index = j

        return min_index


    for i in range(len(seq)):
        # find min index
        min_index = get_minIndex(i, seq)
            
        #swap min_item
        if seq[i]  > seq[min_index]:
            seq[i]  , seq[min_index] =seq[min_index]  , seq[i]

    return seq



s = [5, 8, 2, 6, 9, 1, 0, 7]

print(sort_squence(s))

# minimum total weight
# after decreasing the weight of the smallest item

def minimum_total(weights: list) -> int:

    total_weight = 0

    for i in range(len(weights)):
        total_weight += weights[i]

    return total_weight