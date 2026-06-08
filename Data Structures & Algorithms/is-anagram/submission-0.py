class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def store(string) -> dict:
            dicto = {}
            for i in string:
                if i not in dicto:
                    dicto[i] = 1
                elif i in dicto:
                    dicto[i] += 1
            return dicto
        
        x = store(s)
        y = store(t)
        if x.items() != y.items():
            return False
        return True