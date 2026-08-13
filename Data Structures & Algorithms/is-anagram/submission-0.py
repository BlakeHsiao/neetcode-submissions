class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Converts string to list
        s = list(s)
        t = list(t)

        #List to alphabetical
        s = sorted(s)
        t = sorted(t)

        return s == t