class Solution:
    def splitNum(self, num: int) -> int:
        num=sorted(str(num))
        a=''
        b=''
        c=len(num)

        for i in range(c):
            if i%2==0:
               a+=num[i]
            else:
               b+=num[i]
        return int(a)+int(b)