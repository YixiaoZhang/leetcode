from collections import Counter


s="a"
t="a"

tCounter = Counter(t)
sCounter = Counter(s[0:0+len(t)+1])
tCounter = tCounter-sCounter

print(tCounter)