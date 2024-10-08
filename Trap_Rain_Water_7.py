def trap(height):
    n = len(height)
    if n < 3:
        return 0

    left_max = [0] * n
    right_max = [0] * n
    water_trapped = 0

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])

    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    for i in range(n):
        water_trapped += min(left_max[i], right_max[i]) - height[i]

    return water_trapped

height = list(map(int, input().split()))
print(trap(height))
