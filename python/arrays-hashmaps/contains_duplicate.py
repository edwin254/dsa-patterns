# # class Solution:
# def twoSum( nums: list[int], target: int) -> list[int]:
#     numMap = {}
#     n = len(nums)

#     # Build the hash table
#     for i in range(n):
#         numMap[nums[i]] = i

#     print(numMap)

#     # Find the complement
#     for i in range(n):
#         complement = target - nums[i]
#         if complement in numMap and numMap[complement] != i:
#             return [i, numMap[complement]]

#     return []  # No solution found


# if __name__ == "__main__":
#     nums = [3,3]
#     target = 6
#     print(twoSum(nums, target))


def evalRPN(tokens: list[str]) -> int:                #  Ex:  tokens = ["4","13","5","/","+"]
    stack = []
                                                            #      t     operation    stack
    for t in tokens:                                        #    –––––   –––––––––    ––––––––– 
        if t not in '/+-*':                                 #      4                    [4]
            stack.append(int(t))                            #     13                    [4,13]
                                                            #      5                    [4,13,5]
        else:                                               #      /     13 / 5 = 2     [4,2]
            num = stack.pop()                               #      +      4 + 2 = 6     [6]
            if   t == '+': stack[-1]+=  num
            elif t == '-': stack[-1]-=  num
            elif t == '*': stack[-1]*=  num
            else         : 
                
                stack[-1]= int(stack[-1]/num)   
        print(stack) 

    return stack[0]

tokens =["4","-2","/","2","-3","-","-"]

print(evalRPN(tokens)) 