from collections import Counter

def find_max_frequency_element(arr):
    freq = Counter(arr)
    max_element = max(freq, key=freq.get)
    return max_element, freq[max_element]

arr = [1, 2, 3, 2, 4, 2, 5, 3, 3, 3]
element, frequency = find_max_frequency_element(arr)
print("Element:", element)
print("Frequency:", frequency)