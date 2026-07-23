class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = defaultdict(int)
        for num in nums:
            numCount[num] += 1

        groupByCount = defaultdict(list)
        for key, v in numCount.items():
            groupByCount[v].append(key)
        result = []

        for key, v in reversed(sorted(groupByCount.items())):
            print(key, v)
            for j in v:
                result.append(j)
                if len(result) == k:
                    return result
        # print(list(groupByCount.values())[k-1:])
