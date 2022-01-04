from p5 import *

class Line:
    
    def __init__(self, point1, point2, color1, color2):
        self.point1 = point1
        self.point2 = point2
        self.color1 = color1
        self.color2 = color2


    def draw_gradient_line(self, segm):
        for i in range(segm):
            stroke(self.color1.lerp(self.color2, i/segm))
            stroke_weight(5)
            line(
            ((segm - i) * self.point1.x + i * self.point2.x) / segm,
            ((segm - i) * self.point1.y + i * self.point2.y) / segm, 
            ((segm - i - 1) * self.point1.x + (i + 1) * self.point2.x) / segm, 
            ((segm - i - 1) * self.point1.y + (i + 1) * self.point2.y) / segm
            )



        