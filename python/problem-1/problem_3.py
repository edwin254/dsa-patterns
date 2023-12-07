import time
 
def maxSum(arr, k):
    # length of the array
    n = len(arr)
 
    # n must be greater than k
    if n < k:
        print("Invalid")
        return -1
 
    # Compute sum of first window of size k
    window_sum = sum(arr[:k])
 
    # first sum available
    max_sum = window_sum
 
    # Compute the sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # the current window.
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
    # for i in range(n-k+1):
    #     current_window = arr[i:i+k]
    #     print(current_window, i)
    #     current_sum = sum(current_window)
    #     max_sum = max(max_sum, current_sum)

 
    return max_sum
 
 
# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
start_time = time.time()
print(maxSum(arr, k))
end_time = time.time()
print(end_time - start_time)