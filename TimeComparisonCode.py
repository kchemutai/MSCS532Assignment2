import time
import random

from MergeSort import merge_sort  
from QuickSort import quick_sort 

def time_algorithm(algorithm, data):
    start = time.time()
    algorithm(data.copy()) 
    end = time.time()
    return end - start

# Test data
sorted_data = list(range(1000))
reverse_sorted_data = list(range(1000, 0, -1))
random_data = random.sample(range(1000), 1000)

times = {
    "Merge Sort": [
        time_algorithm(merge_sort, sorted_data),
        time_algorithm(merge_sort, reverse_sorted_data),
        time_algorithm(merge_sort, random_data)
    ],
    "Quick Sort": [
        time_algorithm(quick_sort, sorted_data),
        time_algorithm(quick_sort, reverse_sorted_data),
        time_algorithm(quick_sort, random_data)
    ]
}

print("Timing Results (in seconds):")
for sort_type, timings in times.items():
    print(f"{sort_type}:")
    print(f"  Sorted data: {timings[0]:.6f} s")
    print(f"  Reverse sorted data: {timings[1]:.6f} s")
    print(f"  Random data: {timings[2]:.6f} s")
