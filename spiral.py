import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Spirals with Turtle Graphics")

# Create a list of turtles for multiple spirals
spirals = []

# List of colors to use in the spirals
colors = ["red", "yellow", "blue", "green", "orange", "purple", "pink", "cyan", "white"]

# Function to create a turtle with a random color and position
def create_turtle():
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    t.color(random.choice(colors))
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.pendown()
    spirals.append(t)

# Function to draw a spiral
def draw_spiral(turtle, size, angle, increment, num_turns):
    for _ in range(num_turns):
        turtle.color(random.choice(colors))
        turtle.forward(size)
        turtle.right(angle)
        size += increment

# Create multiple turtles
for _ in range(5):
    create_turtle()

# Draw spirals with user-specified parameters
def draw_spirals(size, angle, increment, num_turns):
    for spiral in spirals:
        draw_spiral(spiral, size, angle, increment, num_turns)

# Change the background color
def change_bgcolor():
    screen.bgcolor(random.choice(colors))

# Main function to run the drawing
def main():
    size = int(screen.numinput("Spiral Size", "Enter the initial size of the spiral:", 5, minval=1, maxval=20))
    angle = int(screen.numinput("Spiral Angle", "Enter the angle for the spiral:", 45, minval=1, maxval=360))
    increment = int(screen.numinput("Size Increment", "Enter the size increment for each step:", 3, minval=1, maxval=10))
    num_turns = int(screen.numinput("Number of Turns", "Enter the number of turns:", 100, minval=10, maxval=1000))
    
    draw_spirals(size, angle, increment, num_turns)

# Bind the space key to change the background color
screen.listen()
screen.onkey(change_bgcolor, "space")

# Run the main function
main()

# Hide all turtles and display the window
for spiral in spirals:
    spiral.hideturtle()

turtle.done()
