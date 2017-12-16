from turtle import Turtle
from time import sleep

from point import Point


class Bar:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2
        self.draw()

    def draw(self):
        pen = Turtle()
        pen.pencolor("black")
        pen.hideturtle()
        pen.pensize(10)
        pen.penup()
        pen.setpos(self.point1.tuple())
        pen.pendown()
        pen.goto(self.point2.tuple())
        pen.penup()


class HorizontalBar(Bar):
    def __init__(self, x1: int, x2: int, y: int):
        x1, x2 = min(x1, x2), max(x1, x2)
        Bar.__init__(self, Point(x1, y), Point(x2, y))

    def collision(self, pos: Point):
        return (abs(pos.y - self.point1.y) < 1) or ((pos.x >= self.point1.x) and (pos.x <= self.point2.x))


class VerticalBar(Bar):
    def __init__(self, x: int, y1: int, y2: int):
        y1, y2 = min(y1, y2), max(y1, y2)
        Bar.__init__(self, Point(x, y1), Point(x, y2))

    def collision(self, pos: Point):
        return (abs(pos.x - self.point1.x) < 1) or ((pos.y >= self.point1.y) and (pos.y <= self.point2.y))


bar = HorizontalBar(x1=0, x2=100, y=0)
bar = VerticalBar(x=100, y1=0, y2=50)
bar = HorizontalBar(x1=0, x2=-100, y=-100)
sleep(5)
