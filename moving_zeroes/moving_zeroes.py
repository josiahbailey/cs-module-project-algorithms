'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    track = len(arr)
    for x in range(0, len(arr)):
        print(arr)
        if arr[x] == 0:
            for z in range(x, len(arr)):
                if arr[z] != 0:
                    break
                elif z == len(arr) - 1:
                    return arr
            track -= 1
            if arr[track] == 0:
                for j in range(x, len(arr)):
                    if arr[j] != 0:
                        track = j
                        break
            arr[x], arr[track] = arr[track], arr[x]
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 2, 3, 0, 4, 0, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
