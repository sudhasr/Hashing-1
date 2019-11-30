"""The approach is to iterate through the array of strings and sort each string, add
 new strings as key and empty list as value to hashmap. When we find a matched string,
 append the strings to the list values"""
#Accepted on leetcode
#Time complexity - O(n) as we traverse entire list
#Space omplexity - O(n) since we are using hashmap


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_dict = dict()
        for i in strs:
            temp = "".join(sorted(i))
            if temp not in anagram_dict:
                anagram_dict[temp] = []
            anagram_dict[temp].append(i)                     
        return anagram_dict.values()