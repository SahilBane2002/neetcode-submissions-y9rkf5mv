class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort the strings
        if sorted(s) == sorted(t):
            return True
        return False