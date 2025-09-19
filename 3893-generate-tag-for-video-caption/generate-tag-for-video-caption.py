class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        if not words:
            return "#"
        camel = words[0].lower() + "".join(w.capitalize() for w in words[1:])
        camel = re.sub(r'[^a-zA-Z]', '', camel)
        return ("#" + camel)[:100]