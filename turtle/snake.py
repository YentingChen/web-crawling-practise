from turtle import Turtle

class Snake:

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
    
    def create_snake(self):
        starting_positions = [(0,0), (-20,0), (-40,0)]
        for position in starting_positions:
            newTurtle = Turtle()
            newTurtle.shape('square')
            newTurtle.penup()
            newTurtle.goto(position)
            self.segments.append(newTurtle)
    
    def move(self):
        for index in range(len(self.segments) - 1, -1, -1):
            if index == 0: 
                if self.segments[index].xcor() > 280: 
                    self.segments[index].goto(-300, self.segments[index].ycor())
                if self.segments[index].xcor() < -300:
                    self.segments[index].goto(280, self.segments[index].ycor())
                if self.segments[index].ycor() > 280:
                    self.segments[index].goto(self.segments[index].xcor(), -300)
                if self.segments[index].ycor() < -300:
                    self.segments[index].goto(self.segments[index].xcor(),280)

                else:
                    self.segments[index].forward(20)
            else:
                new_x = self.segments[index - 1].xcor()
                new_y = self.segments[index - 1].ycor()
                self.segments[index].goto(new_x, new_y)
    
    def grow(self):
        newTurtle = Turtle()
        newTurtle.shape('square')
        newTurtle.penup()
        last = self.segments[-1]
        if self.segments[0].heading() != 0:
             newTurtle.goto((last.xcor() - 20, last.ycor()))
        if self.segments[0].heading() != 90:
             newTurtle.goto((last.xcor(), last.ycor() - 20))
        if self.segments[0].heading() != 180:
             newTurtle.goto((last.xcor() + 20, last.ycor()))
        if self.segments[0].heading() != 270:
             newTurtle.goto((last.xcor(), last.ycor() + 20))
       
        self.segments.append(newTurtle)


    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
             self.segments[0].setheading(0)
        