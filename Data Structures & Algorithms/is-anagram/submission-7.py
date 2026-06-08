class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        counter = {}
        for i in s:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        
        for j in t:
            if j in counter:
                counter[j] -= 1
            else:
                return False
        
        if all(x == 0 for x in counter.values()):
            return True
        return False