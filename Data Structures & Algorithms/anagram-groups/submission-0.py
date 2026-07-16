class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary_pool = {}
        a_list = []
        for i, v in enumerate(strs):
            sorted_str = "".join(sorted(v))
            if sorted_str not in dictionary_pool:
                dictionary_pool[sorted_str] = [v]
            else:
                dictionary_pool[sorted_str].append(v)
        for j, k in dictionary_pool.items():
            a_list.append(k)
        return a_list