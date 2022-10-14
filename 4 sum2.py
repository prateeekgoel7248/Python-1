class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
#         count = 0
#         num_dict = {}
#         for i in C:
#             for j in D:
#                 s = i + j
#                 if s in num_dict:
#                     num_dict[s] += 1
#                 else:
#                     num_dict[s] = 1

#         for i in range(len(A)):
#             for j in range(len(B)):
#                 target = 0 - (A[i]+B[j])
#                 if target in num_dict:
#                     count += num_dict[target]
#         return count
# Solution - O(n^2) - Hashmaps
        # Solve 2sum for nums1 and nums2, solve 2sum for nums3 and nums4. Then for each -(a+b)=c+d, ans+=(# ways to get a+b)*(# ways to get c+d)
        freq1=collections.Counter(nums1)
        freq2=collections.Counter(nums2)
        freq3=collections.Counter(nums3)
        freq4=collections.Counter(nums4)
        
        # key=a+b, value=number of ways to get a+b from nums1, nums2
        dic12=collections.defaultdict(int)
        for a,countA in freq1.items():
            for b,countB in freq2.items():
                dic12[a+b] += countA*countB
        
        # key=c+d, value=number of ways to get c+d from nums3, nums4
        dic34=collections.defaultdict(int) 
        for c,countC in freq3.items():
            for d,countD in freq4.items():
                dic34[c+d] += countC*countD
        
        # Combine 2sum for nums1,nums2 and 2sum for nums3,nums4 to get ans
        ans=0
        for ab in dic12.keys():
            if -ab in dic34:
                # num times a+b+c+d=(a+b)+(c+d)=0 <==> -(a+b)=c+d
                ans+=dic12[ab]*dic34[-ab]
        return ans