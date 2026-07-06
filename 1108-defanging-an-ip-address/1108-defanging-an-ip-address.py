class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=""
        for i in address:
            # print(i)
            if i =='.':
                ans+='[.]'
            else:
                ans+=i
        return ans