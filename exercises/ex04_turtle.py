"""Draws trees, birds, and a house at random location using the turtle library."""

__author__ = "730480180"

from turtle import Turtle, colormode, done
from random import randint


def draw_line(pen: Turtle, x1: int, y1: int, x2: int, y2: int) -> None:
    """Connects two points with a line. {x1} and {y1} parameters correspond with the first xy value pair; {x2} and {y2} arguments correspond with the second xy value pair."""
    # pen set up
    pen.penup()
    pen.setheading(0.0)
    # draw line
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)


def draw_triangle(pen: Turtle, x: int, y: int, height: int, width: int, shape_fill: bool) -> None:
    """Draws a triangle starting at {x} and {y} as the top point of the triangle with specified height and width."""
    # use drawLine; move triangle down height units and left/right 0.5 width units    

    # find two other points of the triangle
    bottom_left_x: int = x - (width // 2)
    bottom_right_x: int = x + (width // 2)
    bottom_left_right_y: int = y - height

    # draw triangle
    if shape_fill:
        pen.begin_fill()

    draw_line(pen, x, y, bottom_left_x, bottom_left_right_y)
    draw_line(pen, bottom_left_x, bottom_left_right_y, bottom_right_x, bottom_left_right_y)
    draw_line(pen, bottom_right_x, bottom_left_right_y, x, y)

    if shape_fill:
        pen.end_fill()


def draw_rectangle(pen: Turtle, x: int, y: int, height: int, width: int, shape_fill: bool) -> None:
    """Draws a rectangle started at the top-left corner at {x} and {y} with {height} height and {width} width."""
    # find other points on the rectangle
    top_bottom_right_x: int = x + width
    bottom_left_right_y: int = y - height
    # draw the rectangle
    if shape_fill:
        pen.begin_fill()

    draw_line(pen, x, y, top_bottom_right_x, y)
    draw_line(pen, top_bottom_right_x, y, top_bottom_right_x, bottom_left_right_y)
    draw_line(pen, top_bottom_right_x, bottom_left_right_y, x, bottom_left_right_y)
    draw_line(pen, x, bottom_left_right_y, x, y)

    if shape_fill:
        pen.end_fill()


def draw_square(pen: Turtle, x: int, y: int, length: int, shape_fill: bool) -> None:
    """Draws a square started at the top-left corner at {x} and {y} with [length] height and [length] width."""
    draw_rectangle(pen, x, y, length, length, shape_fill)


def draw_diamond(pen: Turtle, x: int, y: int, height: int, width: int, shape_fill: bool) -> None:
    """Draws a diamond centered at {x} and {y} with {height} height and {width} width."""
    left_x: int = x + (width // 2)
    right_x: int = x - (width // 2)
    top_y: int = y + (height // 2)
    bottom_y: int = y - (height // 2)

    trace_points: list[list[int]] = [[left_x, y], [x, top_y], [right_x, y], [x, bottom_y], [left_x, y]]

    if shape_fill:
        pen.begin_fill()

    i: int = 0
    while i < len(trace_points) - 1:
        draw_line(pen, trace_points[i][0], trace_points[i][1], trace_points[i + 1][0], trace_points[i + 1][1])
        i += 1

    if shape_fill:
        pen.end_fill()


def draw_arrow(pen: Turtle, x: int, y: int, length: int, point_direction: float, inner_angle: float) -> None:
    """Draws an arrow with a tip at {x} and {y} pointing at {point_direction} angle."""
    # this constant allows the arrow to be drawn at 45 degres
    DRAWING_DIRECTION: float = 180 + (inner_angle / 2)
    # pen set up
    pen.penup()
    pen.goto(x, y)

    pen.pendown()
    pen.setheading(point_direction)
    pen.left(DRAWING_DIRECTION)
    pen.forward(length)
    # pen set up
    pen.penup()
    pen.goto(x, y)

    pen.pendown()
    pen.setheading(point_direction)
    pen.right(DRAWING_DIRECTION)
    pen.forward(length)


def draw_tree(pen: Turtle, x: int, y: int) -> None:
    """Draws a tree with top at {x} and {y}."""
    leaf_height: int = 90
    leaf_width: int = 60
    trunk_height: int = 90
    trunk_width: int = 35
    leaf_width_multiple: int = 2
    # draws leaf
    pen.fillcolor("green")
    i: int = 0
    while i < 3:
        draw_triangle(pen, x, y, leaf_height, leaf_width, True)
        y -= leaf_height
        leaf_width *= leaf_width_multiple
        i += 1

    # draws trunk
    top_left_point_trunk_x: int = x - (trunk_width // 2)
    top_left_point_trunk_y: int = y
    pen.fillcolor("brown")
    draw_rectangle(pen, top_left_point_trunk_x, top_left_point_trunk_y, trunk_height, trunk_width, True)


def draw_bird(pen: Turtle, x: int, y: int) -> None:
    """Draws a bird with its head at {x} and {y}."""
    head_wings_displacement: int = 25
    tail: int = x - head_wings_displacement - 20
    draw_arrow(pen, x, y, 20, 0, 45)
    # drawing wings
    wing_length: int = 35
    wing_tilt: int = 15
    wing_angle: int = 180
    draw_arrow(pen, x - head_wings_displacement, y, wing_length, wing_tilt, wing_angle)
    # draw bird body
    draw_line(pen, x, y, tail, y)
    # draw bird tail
    draw_arrow(pen, tail, y, 15, 0, 30)


def draw_house(pen: Turtle, x: int, y: int, shape_fill: bool) -> None:
    """Draws a house with its highest point at {x} and {y}."""
    # draws roof 
    roof_height: int = 120
    roof_width: int = 270
    pen.fillcolor(211, 211, 211)
    draw_triangle(pen, x, y, roof_height, roof_width, True)

    # draws house body
    house_width: int = 180
    house_body_x: int = x - (house_width // 2)
    house_body_y: int = y - roof_height
    pen.fillcolor(203, 65, 84)
    draw_square(pen, house_body_x, house_body_y, house_width, True)

    # draws windows
    # general windows dimension
    win_width: int = 50
    win_height: int = 50
    # windows location relative to the house
    win1_x: int = x 
    win1_y: int = y - (roof_height // 3) * 2
    win2_x: int = x - (house_width // 4)
    win3_x: int = x + (house_width // 4)
    win2_3_y: int = y - ((house_width + roof_height) // 5) * 3
    win_location: list[list[int]] = [[win1_x, win1_y], [win2_x, win2_3_y], [win3_x, win2_3_y]]
    pen.fillcolor(255, 255, 102)

    i: int = 0
    while i < 3:
        # window cross location relative to windows
        win_cross_x1: int = win_location[i][0] - (win_width // 2)
        win_cross_x2: int = win_location[i][0] + (win_width // 2)
        win_cross_y1: int = win_location[i][1] + (win_height // 2)
        win_cross_y2: int = win_location[i][1] - (win_height // 2)

        draw_diamond(pen, win_location[i][0], win_location[i][1], win_height, win_width, True)
        draw_line(pen, win_cross_x1, win_location[i][1], win_cross_x2, win_location[i][1])
        draw_line(pen, win_location[i][0], win_cross_y1, win_location[i][0], win_cross_y2)

        i += 1

    # draw door
    door_width: int = 50
    door_height: int = 90
    door_x: int = x - (door_width // 2)
    door_y: int = house_body_y - (house_width // 2)
    pen.fillcolor(204, 153, 102)
    draw_rectangle(pen, door_x, door_y, door_height, door_width, True)
    
    # draw door knob
    door_knob_x: int = door_x + 8
    door_knob_y: int = door_y - (door_height // 3) * 2
    pen.penup()
    pen.goto(door_knob_x, door_knob_y)
    pen.pendown()
    pen.circle(5)


def main() -> None:
    colormode(255)
    wang_ba: Turtle = Turtle()
    wang_ba.shape("turtle")
    wang_ba.speed(0)

    # draws tree
    i: int = 0 
    while i < 5:
        draw_tree(wang_ba, randint(-700, -200), randint(-300, 400))
        draw_tree(wang_ba, randint(200, 700), randint(-300, 400))
        draw_tree(wang_ba, randint(-500, 500), randint(100, 500))

        i += 1

    # draws bird
    i = 0
    while i < 20:
        wang_ba.pencolor("red")
        draw_bird(wang_ba, randint(-600, 600), randint(50, 400))
        i += 1
    
    wang_ba.pencolor("black")
    # draws house
    draw_house(wang_ba, 0, 0, True)

    done()


if __name__ == "__main__":
    main()