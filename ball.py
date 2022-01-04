from p5 import *

class Ball:
    
    def __init__(self, dim, pos, speed, color):
        self.dim = dim
        self.pos = pos
        self.speed = speed
        self.col = color


    def update(self):
        self.pos += self.speed
        
        if self.pos.x > width - self.dim / 2:
            self.speed.x = -self.speed.x
        elif self.pos.x < self.dim / 2:
            self.speed.x = -self.speed.x

        if self.pos.y > height - self.dim / 2:
            self.speed.y = -self.speed.y
        elif self.pos.y < self.dim / 2:
            self.speed.y = -self.speed.y

    
    def move(self):
        no_stroke()
        with push_matrix():
                fill(self.col)
                ellipse_mode(CENTER)
                ellipse(self.pos, self.dim, self.dim)
