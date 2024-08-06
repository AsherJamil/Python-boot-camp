import turtle
import math
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

# Register shapes
turtle.register_shape("invader", ((-10, -10), (10, -10), (10, 10), (-10, 10)))
turtle.register_shape("player", ((-10, -10), (10, -10), (10, 10), (-10, 10)))

# Create player
player = turtle.Turtle()
player.shape("player")
player.color("green")
player.penup()
player.speed(0)
player.setposition(0, -250)

# Create player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

# Create multiple enemies
number_of_enemies = 5
enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.shape("invader")
    enemy.color("red")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

# Create score display
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-330, 310)
score_string = "Score: %s" % score
score_pen.write(score_string, False, align="left",
                font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Set player speed
playerspeed = 15

# Define bullet state
bulletstate = "ready"

# Move player left and right


def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) +
                         math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# Keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main game loop
while True:
    screen.update()

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += 2
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemy.setx(-280)

        # Check for collision between bullet and enemy
        if is_collision(bullet, enemy):
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update the score
            score += 10
            score_string = "Score: %s" % score
            score_pen.clear()
            score_pen.write(score_string, False, align="left",
                            font=("Arial", 14, "normal"))

        # Check for collision between player and enemy
        if is_collision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += 20
        bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

turtle.done()
