class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ra = Counter(ransomNote)
        ma = Counter(magazine)
        
        for key, freq in ra.items():
            if key not in ma or  ma[key] < freq:
                return False
        return True