def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test cases
def test_merge_sort():
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert merge_sort([42]) == [42]
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert merge_sort([7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7]
    assert merge_sort([]) == []
    assert merge_sort([3, -1, 4, -1, 5, -9, 2, 6, 5, 3, -5]) == [-9, -5, -1, -1, 2, 3, 3, 4, 5, 5, 6]
    assert merge_sort([100000, 500, 10000, 2000, 500000]) == [500, 2000, 10000, 100000, 500000]
    print("All test cases passed");

# Run the tests
test_merge_sort()
