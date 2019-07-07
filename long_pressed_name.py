#link: https://leetcode.com/problems/long-pressed-name/
class Solution:
    def groupify(self, word):
        result = []
        counter = 1
        for i in range(len(word)):
            if i == len(word) - 1 or word[i] != word[i + 1]:
                result.append((word[i], counter))
                counter = 1
                continue

            counter += 1

        return result

    def isLongPressedName(self, name: str, typed: str) -> bool:
        result_name = self.groupify(name)
        result_typed = self.groupify(typed)
        if len(result_name) != len(result_typed):
            return False

        for block_name, block_typed in zip(result_name, result_typed):
            block_name_letter, block_name_size = block_name
            block_typed_letter, block_typed_size = block_typed

            if block_name_letter != block_typed_letter or block_typed_size < block_name_size:
                return False
            
        return True
    
