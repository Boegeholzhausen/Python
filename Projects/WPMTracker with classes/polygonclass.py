import turtle

class Polygon:
    def __init__(self, sides, name, size=150, color="blue", line_thickness=5):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles = (self.sides-2)*180
        self.angle = self.interior_angles/self.sides

    def draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180 - self.angle)



# square = Polygon(4, "Square")
# pentagon = Polygon(5, "Pentagon")
# hexagon = Polygon(6, "Hexagon", 100, "red")


# hexagon.draw()

class Square(Polygon):
    def __init__(self, size=150, color="blue", line_thickness=5):
        super().__init__(4, "Square", size, color, line_thickness)

    def draw(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()

square = Square(color="red")

square.draw()

turtle.done()