class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        numstr= list(map(str,nums))

        numstr.sort(key= lambda x: x*10,reverse=True)

        if numstr[0]== "0":
            return "0"

        largest= ''.join(numstr)
        return largest
             

        