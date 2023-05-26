class Solution:
    def frequencySort(self, s: str) -> str:
        ans = []
        for ch, oc in sorted(Counter(s).items(), key = lambda x: x[1], reverse = True):
            ans.extend([ch]*oc) 
        return ''.join(ans)
        