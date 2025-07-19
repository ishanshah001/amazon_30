class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict ={}
        count = [[] for i in range(len(nums))]
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=0
        
        for num in dict.keys():
            count[dict[num]].append(num)
        
        i = len(nums) -1
        op= []
        print(count)
        while k!=0:
            if count[i]:    
                j=0           
                while k>0 and j!=len(count[i]):
                    op.append(count[i][j])
                    j+=1
                    k-=1
            i-=1
        return op