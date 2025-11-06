#frequency of eachh element in a list and the find the number with the highest frequency and its frequency
def freq(n):
    d = {}
    # Count frequencies of each element
    for i in n:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    # Find the element with the maximum frequency
    maxe = max(d, key=d.get)
    maxf= d[maxe]
    return maxe, maxf

# Example usage
nums = [1, 3, 2, 3, 4, 3, 5, 1, 3]
element, freq = freq(nums)
print(f"The number with the highest frequency is {element}, and its frequency is {freq}.")
