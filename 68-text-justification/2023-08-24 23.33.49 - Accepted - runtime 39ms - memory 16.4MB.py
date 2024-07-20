class Solution:
    def format_line(self, words, maxWidth, is_last=False):
        if is_last or len(words) == 1:
            return ' '.join(words).ljust(maxWidth)
        
        total_length = sum(len(word) for word in words)
        total_spaces = maxWidth - total_length
        space_gaps = len(words) - 1
        base_spaces = total_spaces // space_gaps
        extra_spaces = total_spaces % space_gaps
        
        formatted_line = words[0]
        for i in range(1, len(words)):
            spaces = base_spaces + (1 if i <= extra_spaces else 0)
            formatted_line += ' ' * spaces + words[i]
        
        return formatted_line
        
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line_words = []
        line_length = 0
        
        for word in words:
            if line_length + len(line_words) + len(word) > maxWidth:
                result.append(self.format_line(line_words, maxWidth))
                line_words = []
                line_length = 0
            line_words.append(word)
            line_length += len(word)
        
        result.append(self.format_line(line_words, maxWidth, is_last=True))
        
        return result