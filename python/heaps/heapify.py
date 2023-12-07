import heapq

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heap = heapq.heapify(data)
print((data))
print(heapq.heappop(data))