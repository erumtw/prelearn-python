# ฟังก์ชันคำนวณหา factorial, permutation, combination

# factorial n! = n(n-1)(n-2) ex 3! = 3*2*1
# 0! = 1
def factorial(nums, k = 0):
    result = 1
    for i in range(nums, k, -1):
        result *= i
    return result


def permutation(n, k):
    # return factorial(n, n-k)
    return factorial(n) // factorial(n-k)

def combination(n, r):
    # return factorial(n) / (factorial(r) * (factorial(n-r)))
    return permutation(n, r) // factorial(r)

print(factorial(0))
print(permutation(10, 3))
print(combination(4, 1))