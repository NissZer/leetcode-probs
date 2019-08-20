#https://leetcode.com/problems/high-five/
count = {}
res = []
for item in arr:
    count.setdefault(item[0], []).append(item[1])

for key in count.keys():
    sorted_scores = sorted(count[key], reverse=True)
    res.append((key,sum(sorted_scores[:5])//5))


return res