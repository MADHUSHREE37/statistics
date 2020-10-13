import statistics
items = int(input())
numbers = list(map(int,input().split()))

print(statistics.mean(numbers))
#mean = sum(numbers)/items
print(statistics.median(numbers))
#index = items // 2
#median = 0
#if items % 2:
#    median =  sorted(numbers)[index]
#median =  sum(sorted(numbers)[index - 1:index + 1]) / 2
print(max(sorted(numbers), key=numbers.count))
