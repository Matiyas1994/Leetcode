class Solution:

    def __init__(self, w: List[int]):
        self.weight = [i for i in range(len(w))]
        self.probability = []
        summ = sum(w)
        for i in range(len(w)):
            self.probability.append(w[i]/summ)
        
        

    def pickIndex(self) -> int:
        return random.choices(self.weight,self.probability)[0]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
