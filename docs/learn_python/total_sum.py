"""
    The following code takes one int and outputs it's sum:
    n = 3
    1+2+3 = 6
"""
def total_sum(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
        
    return total_sum
    