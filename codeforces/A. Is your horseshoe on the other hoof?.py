"""
Input
The first line contains four space-separated integers s1, s2, s3, s4 (1 ≤ s1, s2, s3, s4 ≤ 109) — the colors of horseshoes Valera has.

Consider all possible colors indexed with integers.

Output
Print a single integer — the minimum number of horseshoes Valera needs to buy.
"""



a = map(int, input().split())
def sol(a):
    u = set()
    u.update(a)
    return 4 - len(u)
print(sol(a))
