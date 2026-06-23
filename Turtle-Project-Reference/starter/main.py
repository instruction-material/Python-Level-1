import turtle


# ------------------------------------------------------------
# Function definitions
# ------------------------------------------------------------

# TODO: Return True only when x and y are inside the square boundary.
def is_inside_bounds(x, y):
    return True


# TODO: Clear the old score text and write the updated score.
def update_score():
    pass


# TODO: Draw a square border using border_turtle.
def draw_border():
    pass


# TODO: Calculate the next player position before moving.
def move_player(dx, dy):
    pass


def move_up():
    move_player(0, PLAYER_STEP)


def move_down():
    move_player(0, -PLAYER_STEP)


def move_left():
    move_player(-PLAYER_STEP, 0)


def move_right():
    move_player(PLAYER_STEP, 0)


# TODO: Move each enemy and reverse direction when the next position
# would leave the boundary.
def move_enemies():
    pass


# TODO: Compare the player and enemy positions. If they are close enough,
# update the global score and redraw the score text.
def check_enemy_collisions():
    global score
    pass


# ------------------------------------------------------------
# Variables and turtle attributes
# ------------------------------------------------------------

BOUNDARY = 160
PLAYER_STEP = 15
HIT_DISTANCE = 20
score = 0
enemies = []

screen = turtle.Screen()
screen.setup(420, 420)

player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()

score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(-180, 175)

border_turtle = turtle.Turtle()
border_turtle.hideturtle()
border_turtle.speed(0)


# ------------------------------------------------------------
# One-time setup logic
# ------------------------------------------------------------

draw_border()
update_score()

# TODO: Create triangle turtles, give each one dx and dy attributes,
# and add them to the enemies list.

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")


# ------------------------------------------------------------
# Continuous game logic
# ------------------------------------------------------------

# TODO: Add a loop that moves enemies, checks collisions, and updates
# the screen if tracer/update is enabled.
