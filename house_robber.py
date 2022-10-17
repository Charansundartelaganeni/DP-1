#TC: O(n)
#SC: O(n)


class Solution:
    def rob(self, nums) -> int:
        
        
        if len(nums)==1:   #initially if the length of the houses is one, then the profit is the first house
            return nums[0] 
       
        profit_before_that = nums[0]   #initial profit is going to be the first house
        
        current_profit = max(nums[0],nums[1])  #current profit will be the maximum of the first and second house
        
        for i in range(2, len(nums)):   #traverse from the second house 
            
            if (nums[i] + profit_before_that) > current_profit: #if the sum of current house value and profit before that is greater than the current profit, then it means we are choosing it
                
                temp = current_profit #if that's the case, save the current profit to temp as it may change
                current_profit = profit_before_that + nums[i]   #change the current profit as the sum of prev profit and current house
                profit_before_that = temp #now assign the prev profit as current
                
            else: 
                
                profit_before_that = current_profit #else no choose, that means the current profit is still the profit
   
        return current_profit #return the current profit