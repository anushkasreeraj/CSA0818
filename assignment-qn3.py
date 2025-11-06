#lucky or not
# Recursive function to calculate the sum of digits of a number
def rsum(n):
    # Base case: If the number is 0, the sum is 0
    if n == 0:
        return 0
    else:
        return n % 10 + rsum(n // 10)

# Recursive function to calculate the product of digits of a number
def rprod(n):
    # Base case: If the number is 0, the product is 1 (since 0 would make the product 0, we handle it differently)
    if n == 0:
        return 1
    else:
        return n % 10 * rprod(n // 10)

# Function to check if the number is lucky
def isLucky(n):
    # Get the sum and product of digits
    sd = rsum(n)
    pd = rprod(n)
    
    # Compare if the sum and product are equal
    if sd== pd:
        return "Yes"
    else:
        return "No"

# Example usage:
num = int(input("Enter a number: "))
print(isLucky(num))
