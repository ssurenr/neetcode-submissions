class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_counter = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            strs_counter[sorted_word].append(word)
        return list(strs_counter.values())
            
        