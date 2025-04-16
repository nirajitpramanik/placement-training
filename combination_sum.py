def combination_sum(candidates, target):
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]

    for num in candidates:
        for i in range(num, target + 1):
            for comb in dp[i - num]:
                dp[i].append(comb + [num])

    return dp[target]

n = int(input())
candidates = list(map(int, input().split()))
target = int(input())

combinations = combination_sum(candidates, target)

for combo in combinations:
    print(" ".join(map(str, combo)))
