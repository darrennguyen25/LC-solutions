'''
Premium question

Description:
A row of n houses where each house can be painted 1 of 3 colors: red, blue, or green.
The cost of painting each house with a certain color is different. You have to paint
all the houses such that no 2 adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an 'n x 3' cost
matrix 'costs'

Ex: costs[0][0] is the cost of painting house 0 with red
    costs[1][2] is the cost of painting house 1 with green
    ...

Return the minimum cost to paint all houses

Solution:
Picking which color to paint each house depends on the color choices made for the previous house
Use DP to keep track of the minimum cost up to each house while adhering to the color restriction
Initialize dp array to store the 3 costs of the paints for each house
Iterate over the houses with a for loop to get the 3 costs
Calculate the minimum cost for painting the current house with previous house costs
    To paint current red house, look for the min cost between painting the prev house blue or green
    Then add that min to the cost of painting the current house red
    Do the same thing with the current blue, but this time take the min of the red and green costs
    Do the same thing with the current green, but this time take the min of the red and blue costs

    Doing this ensures that for any house, we choose the color that wasn't chosen for the prev house
    and had the min cost among the remaining colors

After calculating, store those new values into the dp array and keep iterating.
Once we're done iterating take the min of final dp array and return that value


Time Complexity: O(n)
Space Complexity: O(1) extra space for initializing dp list
'''

def min_cost(costs):
    #Store the prices to paint the previous house
    dp = [0, 0, 0]

    #Iterate over the houses
    for i in range(len(costs)):
        #get the min cost of painting each house, not repeating the color of the adj house
        dp0 = costs[i][0] + min(dp[1], dp[2])
        dp1 = costs[i][1] + min(dp[0], dp[2])
        dp2 = costs[i][2] + min(dp[0], dp[1])
        
        #Update the current min costs for each color
        dp = [dp0, dp1, dp2]

    #Return the min cost among the 3 paints at the end
    return min(dp)

#test
costs = [[17, 2, 17],  [16, 16, 5], [14, 3, 19]]
print(min_cost(costs))