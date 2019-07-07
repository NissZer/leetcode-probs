#link: https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_letter = dict()
        if s == "":
            return -1
        
        for letter in list(s): 
            if letter in count_letter:
                count_letter[letter] += 1
            else:
                count_letter[letter] = 1

        for i, letter in enumerate(list(s)):
            if letter in count_letter and count_letter[letter] == 1:
                return(i)
        return -1
