def MaximumSubarraySum(Array):
#     n=len(Array)
#     Max=Array[0]
#     for i in range(0 ,n):
#         j=i+1
#         s=Array[i]
#         while(j < n):
#             if ( s >= Max ):
#                 Max=s
#         s = s + Array[j]
#         j=j+1

#     return Max

# array = [-2, -1, -3, 4, -1, 2, 1, -5, 4]
# print(MaximumSubarraySum(array))