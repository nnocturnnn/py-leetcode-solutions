class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[bit ^ 1 for bit in pix][::-1] for pix in image]