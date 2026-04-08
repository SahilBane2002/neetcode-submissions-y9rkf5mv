class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We will use Bucket sort

        # count = Counter(nums) # frequency map (num, freq)

        # bucket = [[] for _ in range(len(nums) + 1)] 

        # for num, freq in count.items():
        #     bucket[freq].append(num)

        # result = []

        # for freq in range(len(bucket)-1, 0, -1):
        #     for num in bucket[freq]:
        #         result.append(num)
        #         if len(result) == k:
        #             return result

        # return []
    
    # Heapq approach

        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
