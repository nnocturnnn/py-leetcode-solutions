class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.lower().split()
        for i in range(len(title)):
            if len(title[i]) > 2:
                title[i] = title[i].capitalize()
        return " ".join(title)
        