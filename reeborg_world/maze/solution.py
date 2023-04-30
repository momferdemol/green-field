import library  

while front_is_clear():
    move()

turn_left()

while not at_goal():
    
    if right_is_clear():
        library.turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    turn_left()
    turn_left()
    turn_left()
