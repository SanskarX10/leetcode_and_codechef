"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.
"""




class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
    
            
        if image[sr][sc] == newColor:
            return image
        self.fill(image, sr, sc, image[sr][sc], newColor)
        return image
            
    def fill(self, image, r, c, initial, meow):
        if r<0 or r >= len(image) or c<0 or c>= len(image[0]) or image[r][c] != initial:
            return
        image[r][c] = meow 
        self.fill(image,r+1,c, initial, meow)
        self.fill(image,r-1,c, initial, meow)
        self.fill(image,r,c+1, initial, meow)
        self.fill(image,r,c-1, initial, meow)
                
            
