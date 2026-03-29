class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        for string in strs:
            canonical = ''.join(sorted(string))
            if canonical in anagram_groups:
                anagram_groups[canonical].append(string)
            else:
                anagram_groups[canonical] = [string]
        return list(anagram_groups.values())
