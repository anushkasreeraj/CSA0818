#
def intersect(num1, num2):
    # Dictionary to count the occurrences of each element in num1
    count1 = {}
    for num in num1:
        count1[num] = count1.get(num, 0) + 1
    
    # List to store the intersection result
    intersection = []
    
    # Iterate through num2 and check if each element exists in count1
    for num in num2:
        if num in count1 and count1[num] > 0:
            intersection.append(num)
            count1[num] -= 1  # Decrease the count since we've added this element
    
    return intersection

# Example 1
num1 = eval(input())
num2 = eval(input())
print(intersect(num1, num2))  # Output: [2, 2]

