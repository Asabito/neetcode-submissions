class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        td = defaultdict(int)
        for n in nums:
            td[n] += 1
        td = dict(sorted(td.items(), key=lambda item: item[1]))
        return list(td.keys())[-k:]