def diagonalDifference(arr):
    primary = 0
    secondary = 0
    n = len(arr)
    
    for i in range(n):
        primary += arr[i][i]
        secondary += arr[i][n-1-i]
    
    return abs(primary - secondary)

n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)