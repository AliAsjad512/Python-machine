def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return [alice, bob]

a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = compareTriplets(a, b)
print(*result)