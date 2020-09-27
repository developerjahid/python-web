import turtle

jahid_turtle = turtle.Turtle()

def square():
    print(jahid_turtle.forward(100))
    print(jahid_turtle.right(90))
    print(jahid_turtle.forward(100))
    print(jahid_turtle.right(90))
    print(jahid_turtle.forward(100))
    print(jahid_turtle.right(90))
    print(jahid_turtle.forward(100))

# square()
# print(jahid_turtle.forward(200))
# square()

# jahid = "happy"

# while jahid == "happy" :
#     square()

for count in range(4):
    square()


