def simpleArraySum(ar):
    return sum(ar)

n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
result = simpleArraySum(ar)
print(result)