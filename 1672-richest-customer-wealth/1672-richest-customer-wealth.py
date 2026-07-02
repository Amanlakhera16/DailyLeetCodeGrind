class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx_sm=0
        for i in range(len(accounts)):
            sm= sum(accounts[i])
            if sm>mx_sm:
                mx_sm=sm
        return mx_sm