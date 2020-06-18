'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    length = len(arr)
    result = []
    for x in range(0, length):
        for z in range(0, length):
            if z != x:
                try:
                    result[x]
                except IndexError:
                    result.append(arr[z])
                else:
                    result[x] *= arr[z]

    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
