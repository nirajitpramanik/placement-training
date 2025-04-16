m = int(input())
n = int(input())

courses, pre = [], []

for i in range(n):
    inp = [int(i) for i in input().split()]
    courses.append(inp[0])
    pre.append(inp[1])

if sorted(pre) == sorted(courses):
    print(0)
else:
    print(1)
