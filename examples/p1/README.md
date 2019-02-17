# Initializing a game and adding objects

The pre-built structure and opinions of Pygamer make loading a game screen a simple two-line process.

```python
import pygamer

pygamer.Game().run()
```

This imports Pygamer, creates an instance of the base `Game` class, and calls its `run()` method. This is the method responsible for running the Pygame loop and calling all other necessary methods to delegate functionality dynamically.

This is super easy, but a blank screen isn't very exciting. Let's make our game a little more specific to our needs. We will build a simple Pong game for this example. As you can imagine, the Pong game should know much more about how the game works than the `Game` class does. So let's subclass `Game`, and start getting specific to our particular game. 

Start by creating a `Pong.py` file and adding the following code:

```python
import pygamer

class Pong(pygamer.Game):
  def __init__(self, ball_speed, paddle_speed, ball_radius, window_size=(800, 600)):
    super().__init__(window_size=window_size, bg_color=(255, 255, 255))
    self.w, self.h = window_size
```

Now create a `main.py` and add the following code. (this is the file you will be running your game from)

```python
from Pong import Pong

if __name__ == "__main__":
    Pong((5, 5), 7, 20).run()
```

Now you can run your game with `python main.py`, or, because we used `if __name__ == "__main__":`, use a debugger with an IDE like pycharm.

So here we have subclassed Game, but our game is still not very exciting. Lets start building some of the objects and logic needed for Pong to function. First let's use the parameters in our constructor to make the ball for our game. 

However, before we can add a ball to Pong, we need to create the class for the Ball. Luckily, Pygamer also comes with an `Object` class that wraps much of the functionality we will need. Let's subclass that to create our Ball class.

Create a `Ball.py` class file and add the following code:

```python
import pygamer

class Ball(pygamer.Object):
  def __init__(self, speed, color, radius, center_position):
    rect = pygame.rect.Rect(center_position[0] - radius, center_position[1] - radius, radius * 2, radius * 2)
    super().__init__(rect, speed)
    self.color = color
    self.radius = radius
    self.diameter = radius * 2
    self.initital_position = center_position
```

Ok let's walk through what is going on in this `Object` subclass. Each object expects a [`pygame.rect.Rect()`](https://www.pygame.org/docs/ref/rect.html) to display and control it. We use our constructor parameters to build this rect. We also pass in the speed to the `Object` to override the default of `speed=(0, 0)` (no movement). We then set member variables we will need later for the Ball class.

Now let's use this Ball in our Pong game.

> NOTE: We are only showing the relevant updated code from before. `...` indicates previously written code.

```python
from Ball import Ball

class Pong(pygamer.Game):
  def __init__(self, ball_speed, paddle_speed, ball_radius, window_size=(800, 600)):
    ...

    self.ball = Ball(ball_speed, (150, 25, 200), ball_radius, (self.w // 2, self.h // 2))
```

Now our Pong game has a ball, but if we run the game again, we will still see the blank screen. There are two more steps we need to do to see the ball show on the screen. First, we need to add the ball to the `Game`'s `objects` array. 

```python
class Pong(pygamer.Game):
    def __init__(self, ball_speed, paddle_speed, ball_radius, window_size=(800, 600)):
        ...
        self.objects.append(self.ball)
```

Second, we need to implement the `draw()` method for the Ball (`Object` sub-class).

> Each `Object`'s `draw()` method is declared, but not implemented, since this functionality is very specific to what the object is. It will need to be implemented on a per-subclass basis for each `Object`. We will do that in the Ball class now.

```python
import pygame

class Ball(pygamer.Object):
  ...

  def draw(self, surface_to_draw_on):
    pygame.draw.circle(surface_to_draw_on, self.color, (self.rect.x + self.radius, self.rect.y + self.radius), self.radius)
```

Now the Ball knows how to draw itself. (Draw it on the surface with it's color, radius, and positioned at whatever its current `rect` position is) Now all we need to do is add it to the `Game`'s `objects` array, and the `Game` will handle the rest of the loop and delegating needs. Running the app, we should now see the ball on the screen and moving at a speed of `(5, 5)` (+5 in the x and y directions, respectively).

The next thing we might need to do is prevent the ball from going off of the screen. This is a perfect use for the `Game`'s `update` method.

```python
import pygame

class Pong(pygamer.Game):
  ...

  def update(self):
    x, y = self.ball.speed
    if self.ball.left < self.window.left:
        self.ball.rect = pygame.rect.Rect(0, self.ball.top, self.ball.width, self.ball.height)
        self.ball.speed = (-x, y)
    elif self.ball.right > self.window.right:
        self.ball.rect = pygame.rect.Rect(self.window.right - self.ball.width, self.ball.top, self.ball.width, self.ball.height)
        self.ball.speed = (-x, y)
    elif self.ball.top < self.window.top:
        self.ball.rect = pygame.rect.Rect(self.ball.left, 0, self.ball.width, self.ball.height)
        self.ball.speed = (x, -y)
    elif self.ball.bottom > self.window.bottom:
        self.ball.rect = pygame.rect.Rect(self.ball.left, self.window.bottom - self.ball.height, self.ball.width, self.ball.height)
        self.ball.speed = (x, -y)
    super().update()
```

Here, we just check the bounds of the ball to the bounds of the window. If there is a crossover, we reset the ball's `rect` to the appropriate axis, and reverse the appropriate speed direction.

This has been a basic intro to how easy it is to build a game with Pygamer, we continue this project in our part two, by adding a menu to our game, allowing the user to pause the game. Check it out [here](../p2)