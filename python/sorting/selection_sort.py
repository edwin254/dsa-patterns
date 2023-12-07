"""
FOR EACH ITEM:
 - LOOP SEQUENCE FINDING SMALLEST VALUE INDEX
 - STARTING FROM IT'S NEXT ITEM YO THE END OF SEQUENCE
 - COMPARE THE SMALLEST VALUE TO THE CURERENT SMALLEST VALUE

"""

def sort_squence(seq: list, start:int=0) -> list:
    min_index = start

    for i in range(len(seq)):
        # find min index
        for j in range(i+1, len(seq)):
            if seq[min_index] > seq[j]:
                min_index = j
            
        #swap min_item
        if seq[i]  > seq[min_index]:
            seq[i]  , seq[min_index] =seq[min_index]  , seq[i]

    return seq



s = [5, 8, 2, 6, 9, 1, 0, 7]

print(sort_squence(s))
