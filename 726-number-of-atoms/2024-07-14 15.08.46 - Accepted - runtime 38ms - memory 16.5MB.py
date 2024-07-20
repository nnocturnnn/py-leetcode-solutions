class Solution:
    def countOfAtoms(self, formula: str) -> str:
        counts = defaultdict(int)
        stack = []
        multiplier, num = 1, ''
        element = ''

        for i in range(len(formula) - 1, -1, -1):
            c = formula[i]
            if c.isdigit():
                num = c + num 
            elif c.isalpha():
                element = c + element
                if c.isupper():
                    counts[element] += multiplier * (int(num) if num else 1)
                    element, num = '', ''
            elif c == ')':
                stack.append(int(num) if num else 1)
                multiplier *= int(num) if num else 1
                num = ''
            elif c == '(':
                multiplier //= stack.pop()

        return ''.join(f"{key}{(counts[key] if counts[key] > 1 else '')}" for key in sorted(counts))