import turtle 
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()

num_sides = 4
side_length1 = 70
angle  = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length1)
    
    polygon.right(angle)

turtle.done()