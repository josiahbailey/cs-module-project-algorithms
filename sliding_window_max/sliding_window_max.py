'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here
    result = []
    x = 0
    length = len(nums)
    for i in range(0, length - (k - 1)):
        biggest = nums[i]
        for j in range(i, k + i):
            if nums[j] > biggest:
                biggest = nums[j]
        result.append(biggest)
        biggest = 0
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7, -1, -2, -3]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
