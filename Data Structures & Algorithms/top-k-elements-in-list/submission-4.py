class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        freq = [[] for i in range(len(nums)+1)]
        for key, v in count.items():
            freq[v].append(key)

        res = []
        for v in range(len(freq)-1, 0, -1):
            for j in freq[v]:
                res.append(j)
                if len(res) == k:
                    return res
        # print(list(groupByCount.values())[k-1:])
