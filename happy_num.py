#https://leetcode.com/problems/happy-number/
set_num = set()

while n not in set_num:
    set_num.add(n)
    n = sum([int(x) ** 2 for x in str(n)])
if n == 1:
    print(True)
