class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        sorted_vovels = sorted([char for char in s if char in vowels], reverse=True)
        result = []
        for char in s:
            if char.lower() in 'aeiou':
                result.append(sorted_vovels.pop())
            else:
                result.append(char)
        return ''.join(result)
        
        