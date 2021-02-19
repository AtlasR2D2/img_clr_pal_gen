from turtle import Turtle


STARTING_POSITION_T = (0, +200)
STARTING_POSITION_M = (-100, +200)
STARTING_POSITION_C = (+50, +200)
GAP_PODIUM = 50
FINISH_LINE_Y = 280
NORTH_HEADING = 90
INITIAL_SHAPE_SIZE = 20
FONT = ("Courier", 12, "normal")
ALIGNMENT = "Center"
ALIGNMENT_C = "Left"

class TurtleClr(Turtle):
    def __init__(self, clr, position):
        super().__init__()
        self.shape("turtle")

        self.fillcolor((clr[0], clr[1], clr[2]))
        self.penup()
        self.setheading(NORTH_HEADING)
        self.position = self.determine_location(position_x=position)
        self.goto(self.position)

    def determine_location(self, position_x):
        """calculates the location based on position"""
        x_coor = STARTING_POSITION_T[0]
        y_coor = STARTING_POSITION_T[1] - (position_x-1) * GAP_PODIUM
        return x_coor, y_coor


class PodiumPosition(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.penup()
        self.hideturtle()
        self.color("black")
        self.location = self.determine_location(position_x=position)
        self.goto(self.location)
        self.show_position()

    def determine_location(self, position_x):
        """calculates the location based on position"""
        x_coor = STARTING_POSITION_M[0]
        y_coor = STARTING_POSITION_M[1] - (position_x-1) * GAP_PODIUM
        return x_coor, y_coor

    def pos_suffix(self):
        if self.position == 1:
            return "st"
        elif self.position == 2:
            return "nd"
        elif self.position == 3:
            return "rd"
        else:
            return "th"

    def show_position(self):
        self.clear()
        self.write(arg=f"{self.position}{self.pos_suffix()}", align=ALIGNMENT, font=FONT)

class ShowColor(Turtle):
    def __init__(self, clr, position):
        super().__init__()
        self.clr = clr
        self.penup()
        self.hideturtle()
        self.color("black")
        self.position = self.determine_location(position_x=position)
        self.goto(self.position)
        self.show_color()

    def determine_location(self, position_x):
        """calculates the location based on position"""
        x_coor = STARTING_POSITION_C[0]
        y_coor = STARTING_POSITION_C[1] - (position_x-1) * GAP_PODIUM
        return x_coor, y_coor

    def show_color(self):
        self.clear()
        self.write(arg=f"Color: {self.clr}", align=ALIGNMENT_C, font=FONT)