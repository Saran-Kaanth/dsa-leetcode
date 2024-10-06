from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_list=[]
        for num in nums:
            if num!=val:
                new_list.append(num)
            # if num==val:
            #     new_list.insert(-1,"_")
            # else:
            #     new_list.insert(0,num)
        
        return new_list

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
        
        
                


if __name__=="__main__":
    solution=Solution()
    val=solution.removeElement([0,1,2,2,3,0,4,2],2)
    print(val)
        