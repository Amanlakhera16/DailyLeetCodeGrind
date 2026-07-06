class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        s=s.lower()
        for i in s:
            if ('0' <= i <= '9') or ('A' <= i <= 'Z') or ('a' <= i <= 'z'):
                ans+=i
        # print( ans) 
        flag=True
        left=0
        right=ans.__len__()-1
        # print(left," ",right)
        while left<right:
            # print("started")
            if ans[left]!=ans[right]:
                flag= False
                break
            left+=1
            right-=1
        # print(flag)
        return flag

        