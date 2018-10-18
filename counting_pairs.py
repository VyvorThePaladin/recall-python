# Counts total number of pairs in a
# space separated integer input

from collections import Counter

socks = Counter(input().split())

print(sum(map(lambda x: x//2, socks.values())))