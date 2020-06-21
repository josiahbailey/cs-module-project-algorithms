'''
Input: a List of integers where every int except one shows up twice
Returns: an integer

solution 1:
loop through all items in array
variable holds current number being checked
variable holds current index
all indexes after current index are checked to see if item exists again
if so break, if not return item

'''


def single_number(arr):
    curr = 0
    i = 0
    result = 0
    checked = []
    for item in arr:
        curr = item
        if curr in checked:
            next
        else:
            for k in range(i + 1, len(arr)):
                if arr[k] == curr:
                    checked.append(arr[k])
                    break
                if k == (len(arr) - 1):
                    result = arr[i]
            if result != 0:
                return result
            else:
                i += 1
                continue
        i += 1
    return False


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
