import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        """Codigo para controlar el movimiento de la bola"""

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball see the edge of the screen
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_x > SCREEN_HEIGHT - self.radius:
            self.change_x *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1


class MyGame(arcade.Window):

    def __init__(self, width, heigth, title):
        super().__init__(width, heigth, title)
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create A list for the balls
        self.ball_list = []

        # Add three balls to the list
        ball = Ball(50, 50, 3, 3, 15, arcade.color.AUBURN)
        self.ball_list.append(ball)

        ball = Ball(100, 150, 3, 3, 15, arcade.color.AUBURN)
        self.ball_list.append(ball)

        ball = Ball(150, 250, 3, 3, 15, arcade.color.AUBURN)
        self.ball_list.append(ball)

    def on_draw(self):
        arcade.start_render()
        for ball in self.ball_list:
            ball.draw()

    def update(self, delta_time):
        for ball in self.ball_list:
            ball.update()

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Examples Lab 7")
    arcade.run()


main()

