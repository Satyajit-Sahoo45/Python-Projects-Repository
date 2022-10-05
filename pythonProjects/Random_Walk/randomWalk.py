import turtle as t
import random

tim = t.Turtle()

# colours = ["dark green", "dark slate gray","gray", "light steel blue","medium blue", "dodger blue", "dark orchid",
# "dark orange", "maroon", "black", "yellow"]

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)

    return color


directions = [0, 90, 180, 270]
tim.pensize(5)
# tim.speed("slowest")

for _ in range(1000):
    # tim.color(random.choice(colours))
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(directions))

