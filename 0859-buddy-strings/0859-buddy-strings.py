class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        occurance = [0]*26
        if s == goal:
            for character in s:
                idx = ord(character)-ord('a')
                if occurance[idx]:
                    return True
                occurance[idx] = 1
            return False

        differentPlaces = []
        for i in range(len(s)):
             if s[i] != goal[i]:
                    differentPlaces.append(i)


        if len(differentPlaces)!=2: return False
        first, second = differentPlaces[0], differentPlaces[1]
        return s[first]==goal[second] and s[second]==goal[first]
            