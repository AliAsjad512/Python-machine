def birthdayCakeCandles(candles):
    max_height = max(candles)
    return candles.count(max_height)

n = int(input().strip())
candles = list(map(int, input().rstrip().split()))
result = birthdayCakeCandles(candles)
print(result)