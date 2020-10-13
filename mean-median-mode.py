import statistics
items = int(input())
numbers = list(map(int,input().split()))

print(statistics.mean(numbers))
print(statistics.median(numbers))
print(max(sorted(numbers), key=numbers.count))
