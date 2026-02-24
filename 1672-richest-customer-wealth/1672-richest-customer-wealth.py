class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        Sum=0
        for i in accounts:
            if Sum<sum(i):
                Sum=sum(i)
        return Sum
        