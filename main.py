from p5 import *
from ball import *
import random
from line import *


balls = [Ball(
        15, 
        Vector(random.randint(1, width), random.randint(1, height)), 
        Vector(random.randint(-5, 5), random.randint(-5, 5)), 
        Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        for i in range(3)]


def setup():
    size(500, 500)
    no_stroke()
    

def draw():
    background(200)
    for ball in balls:
        ball.update()
    for line in get_lines():
        line.draw_gradient_line(15)
    for ball in balls:
        ball.move()
    
    
def get_lines():
    lines = []
    for ball in balls:
        min_dist = height
        for second_ball in balls:
            temp_dist = dist(ball.pos, second_ball.pos)
            if temp_dist != 0 and temp_dist < min_dist:
                closest_ball = second_ball
                min_dist = temp_dist
        lines.append(Line(ball.pos, closest_ball.pos, ball.col, closest_ball.col))
    return lines


if __name__ == '__main__':
    print("hello")
    run()