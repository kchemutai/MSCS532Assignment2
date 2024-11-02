def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Test cases
def test_quick_sort():
    assert quick_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert quick_sort([42]) == [42]    
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]    
    assert quick_sort([7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7]
    assert quick_sort([]) == []
    assert quick_sort([3, -1, 4, -1, 5, -9, 2, 6, 5, 3, -5]) == [-9, -5, -1, -1, 2, 3, 3, 4, 5, 5, 6]
    assert quick_sort([100000, 500, 10000, 2000, 500000]) == [500, 2000, 10000, 100000, 500000]
    print("All test cases passed")
# Run the tests
test_quick_sort()
