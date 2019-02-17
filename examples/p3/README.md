# More players, more fun

[Previously](../p2), we learned how to add a menu to our game super simply. This time, we will learn how add players to our game, each with their own paddle to reflect the ball.

First, we will use the existing `pygamer.Player` class to create our own `PongPlayer`. Create a file called `PongPlayer.py` and add the following code:
```python
import pygamer

class PongPlayer(pygamer.Player):
    def __init__(self, paddle):
        self.objects = [paddle]
```

Here, we just accept a paddle in our player constructor and put it into the player's `object`s array.

Also, in order to give each of our players a paddle to move on the screen, let's create a `Paddle.py` file and implement it like so:

```python
import pygamer

class Paddle(pygamer.Object):
    def __init__(self, rect):
        super().__init__(rect, speed=(0, 7))
        self.rect = rect
        self.color = (80, 134, 240)
        
    def draw(self, surface_to_draw_on):
        pygame.draw.rect(surface_to_draw_on, self.color, self.rect)
```

Here, we just accept a rect into the paddle constructor, and use it to draw the paddle on the screen.

Next, we will use our new player and paddle classes to add players to our Pong game:

```python
from Paddle import Paddle
from Player import Player

class Pong(pygamer.Game):
    ...
    
    self.add_players()
    
    def add_players(self):
        paddle_w = 50
        paddle_height = 150
        paddle_1 = Paddle(pygame.rect.Rect(100, self.window.centery - (paddle_height // 2), paddle_w, paddle_height))
        paddle_2 = Paddle(pygame.rect.Rect(self.widow.right - 100 - paddle_w, self.window.centery - (paddle_height // 2), paddle_w, paddle_height))
        player_1 = Player(paddle1)
        player_2 = Player(paddle2)

```