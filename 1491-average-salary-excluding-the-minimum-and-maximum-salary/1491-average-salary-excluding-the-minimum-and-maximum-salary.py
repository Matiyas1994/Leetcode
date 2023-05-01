class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n = len(salary)
        return sum(salary[1:-1])/(n-2)
        