import heapq

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heap = heapq.heapify(data)
print((data))
print(heapq.heappop(data))

# Complexity Analysis of Heap Sort
# Time Complexity: O(N log N)
# Auxiliary Space: O(log n), due to the recursive call stack. However, auxiliary space can be O(1) for iterative implementation.

# Important points about Heap Sort:
# Heap sort is an in-place algorithm. 
# Its typical implementation is not stable but can be made stable (See this)
# Typically 2-3 times slower than well-implemented QuickSort.  The reason for slowness is a lack of locality of reference.
# Advantages of Heap Sort:
# Efficient Time Complexity: Heap Sort has a time complexity of O(n log n) in all cases. This makes it efficient for sorting large datasets. The log n factor comes from the height of the binary heap, and it ensures that the algorithm maintains good performance even with a large number of elements.
# Memory Usage – Memory usage can be minimal because apart from what is necessary to hold the initial list of items to be sorted, it needs no additional memory space to work
# Simplicity –  It is simpler to understand than other equally efficient sorting algorithms because it does not use advanced computer science concepts such as recursion.
# Disadvantages of Heap Sort:
# Costly: Heap sort is costly.
# Unstable: Heap sort is unstable. It might rearrange the relative order.
# Efficient: Heap Sort is not very efficient when working with highly complex data. 
# Frequently Asked Questions Related to Heap Sort
# Q1. What are the two phases of Heap Sort?

# The heap sort algorithm consists of two phases. In the first phase, the array is converted into a max heap. And in the second phase, the highest element is removed (i.e., the one at the tree root) and the remaining elements are used to create a new max heap.

# Q2. Why Heap Sort is not stable?

# The heap sort algorithm is not a stable algorithm. This algorithm is not stable because the operations that are performed in a heap can change the relative ordering of the equivalent keys.

# Q3. Is Heap Sort an example of the “Divide and Conquer” algorithm?

# Heap sort is NOT at all a Divide and Conquer algorithm. It uses a heap data structure to efficiently sort its element and not a “divide and conquer approach” to sort the elements.

# Q4. Which sorting algorithm is better – Heap sort or Merge Sort?

# The answer lies in the comparison of their time complexity and space requirements. The Merge sort is slightly faster than the Heap sort. But on the other hand merge sort takes extra memory. Depending on the requirement, one should choose which one to use.

# Q5. Why is Heap sort better than Selection sort?

# Heap sort is similar to selection sort, but with a better way to get the maximum element. It takes advantage of the heap data structure to get the maximum element in constant time 

# The sorting time of Heap Sort is O nlogn

#  both on average and worst-case. While qsort is about 20% faster on average, it suffers from an exploitable O (n2)
#  worst-case behavior and extra memory requirements that make it less suitable for kernel use.

# Another algorithm that Heap Sort is often compared to is Merge Sort, which has the same time complexity.

# Merge Sort has the advantage of being stable and intuitively parallelizable, while Heap Sort is neither.

# Another note is that Heap Sort is slower than Merge Sort in most cases, even though they have the same complexity since Heap Sort has larger constant factors.

# Heap Sort can, however, be implemented much more easily in place than Merge Sort can, so it's preferred when memory is a more important factor than speed.

# As we saw, Heap Sort isn't as popular as other efficient, general-purpose algorithms but its predictable behavior (other than being unstable) makes it a great algorithm to use where memory and security are more important than slightly faster run-time.

# It's really intuitive to implement and leverage the built-in functionality provided with Python, all we essentially have to do is put the items in a heap and take them out - similar to a coin counter.


"""
heapSort implementation:
"""
class Heap:

    def __init__(self, heap) -> None:
        self.heap = heap
        self.build_max_heap()

    def build_max_heap(self):
        n = len(self.heap)
        parent = n//2 -1

        for i in range(parent, -1, -1):
            self.heapify(n, i)

    def heapify(self, heap_size, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2 

        if left < heap_size and self.heap[left] > self.heap[largest]:
            largest = left

        if right < heap_size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            # swap largest child node with initial largest(index) 

            self.heap[largest], self.heap[index] =  self.heap[index],  self.heap[largest]
            
            self.heapify(heap_size, largest)

        def sort(self):
            n = len(self.heap)

            for i in range(n-1, 0, -1):
                # swap max heap first and last index

                self.heap[0], self.heap[i] =  self.heap[i],  self.heap[0]
                self.heapify(i, 0)
            return self.heap



heap = Heap(data)
def heap_sort(data):
    heap = Heap(data)
    heap.sort()
    return 