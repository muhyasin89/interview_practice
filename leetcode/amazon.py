a = [1, 2, 3]
n = len(a)
mod = 10**9 + 7

def sum_module(a, n):
    Max = max(a)

    cnt = [0 for i in range(Max + 1)]

    for i in a:
        cnt[i] += 1

    ans = 0

    for i in range(1, Max+1):
        for j in range(1, Max+1):
            ans = ans + cnt[i] * cnt[j] * (i % j)
            ans = ans % mod

    return ans

print(sum_module(a,n))
