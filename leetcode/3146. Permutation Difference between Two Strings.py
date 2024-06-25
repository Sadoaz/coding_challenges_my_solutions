class Solution:
    def findPermutationDifference(self, s,t):
        
        result = 0
        for x in range(len(s)):
            result+= abs(x - t.index(s[x]))
        return result





print(Solution().findPermutationDifference(s = "abcde", t = "edbac"))
        