#TC: O(n) 
#SC: O(n)


class Solution:
    def deleteAndEarn(self, nums) -> int:
        table = [0] + [0] * max(nums) #initialize the table with a zero and zeroes upto maximum value in nums
        
        for n in nums:
            table[n] += n #add the values of nums inside the table

        for index in range(3, len(table)): #we can start from third index, as the before two is filled
            table[index] += max(table[index-3], table[index - 2]) #now at every point, the particular index will be the maximum between index - 3 and index - 2 (choose or no choose)

        return max(table[-1], table[-2]) #now print the max between the last before index or the index before that, which is going to give us the exact answer