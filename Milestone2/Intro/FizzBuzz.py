import turtle
""" The FizzBuzz :
There are 16 beads here, numbered 0 through 15. Notice the pattern:

If the number is divisible by 3, then the bead is red (a "Fizz").
If the number is divisible by 5, then the bead is green (a "Buzz")
If the number is divisible by 3 and 5, then there's a green bead in a red bead (a "FizzBuzz")"""




def fizz(tur):
    # A red square bead.
    tur.color("red")
    tur.left(90)
    for side in [10, 20, 20, 20, 10]:
        tur.forward(side)
        tur.right(90)

def buzz(tur):
    # A green hexagonal bead.
    # Fits inside the red bead.
    tur.color("green")
    tur.left(60)
    for side in range(6):
        tur.forward(10)
        tur.right(60)
    tur.right(60)

def plain(tur):
    # A gray octagonal bead.
    tur.color("gray")
    tur.left(90)
    for side in [4, 8, 8, 8, 8, 8, 8, 8, 4]:
        tur.forward(side)
        tur.right(45)
    tur.right(45)

# Set up the turtle to draw beads.
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.penup()
t.back(180)  # Back up to make room!
t.pendown()

for num in range(16):
    if num % 3 == 0:
        fizz(t)
        if num % 5 == 0:
            buzz(t)
    else:
        if num % 5 == 0:
            buzz(t)
        else:
            plain(t)

    # Advance to the next bead spot.
    t.color("gray")
    t.forward(22)
t.hideturtle()