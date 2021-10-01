class Solution:
    def twoSum(self, l: List[int], target: int) -> List[int]:
        s=collections.Counter(l)
        for i in l:
            if target-i in s:
                if i==target-i and s[i]==1:
                    continue
                elif i==target-i and s[i]>1:
                    return [k for k, j in enumerate(l) if j == i]
                else:
                    return [l.index(i),l.index(target-i)]
                    break
