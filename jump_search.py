import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # ✅ Fix: use min(step, n) - 1 to prevent IndexError
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while prev < n and arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if prev < n and arr[prev] == target:
        return prev
    return -1

print(jump_search([1, 3, 5, 7, 9, 11, 13], 9))
