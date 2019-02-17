# Adding menus

So in the [last](../p1) part of this tutorial, we got an awesome bouncing ball on the screen. But what if the user needs to stop playing this awesome game to get a snack? They need to be able to pause the game, and in order to do that, we need a menu to take over temporarily.

Let's get started by creating a method in our Pong class to add menus to the game. (The pause menu will most likely be one of menu menus you create, such as a high scores screen, options menu, etc).

```python
from PauseMenu import PauseMenu

class Pong(pygamer.Game):
    def __init__(self):
        ...
        
        self.add_menus()
        
    def add_menus(self):
        pause_menu = PauseMenu(self.window)
        self.menus.append(pause_menu)

```

This is great, we create a pause menu, and then add it to our games `menu`s array... but first we will need to implement what that `PausedMenu` looks like. To do this, we will subclass Pygamer's `Menu` class to present the user with a simple pause screen.

```python
import pygame
import pygamer


class PauseMenu(pygamer.Menu):
    def __init__(self, screen_to_take_over):
        super().__init__(screen_to_take_over)
        self.add_buttons()

    def add_buttons(self):
        continue_rect = pygame.rect.Rect(200, 400, 100, 50)
        continue_button = pygamer.Button(continue_rect, text="Continue")
        quit_rect = pygame.rect.Rect(500, 400, 100, 50)
        quit_button = pygamer.Button(quit_rect, text="Quit")
        self.objects += [continue_button, quit_button]
```

This will draw two rectangle buttons and draw them on the screen for you. However, we have no way to activate these buttons. Let's add the handler to do that.

```python
import sys

class PauseMenu(pygamer.Menu):
    ...
    
    def add_buttons(self):
        ...

        def button_handler(event):
            if event.key == pygame.K_SLASH:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_c:
                self.deactivate()

        self.handlers[pygame.KEYDOWN].append(button_handler)
```

Now that we have implemented the `PauseMenu` and added to our Pong game's menus array, we need a way to activate it so it can take over the game loop.

```python
class Pong(pygamer.Game):
    ...
    
    def add_menus(self):
        ...

        def menu_handler(event):
            if event.key == pygame.K_SLASH:
                pause_menu.activate()

        self.handlers[pygame.KEYDOWN].append(menu_handler)
```

This adds a keydown handler that checks if the key pressed was the `/`, and if so, activates the pause menu. You can imagine how you might just add other key options for other menus in a similar manner.

And there we have it! Now when a menu loads up, it will present the user with two buttons. If the user presses the `/` key, it will quit the game. If the user presses the `c` key, it will continue the game from where it left off before the menu loaded.

[Next](../p2), we will introduce adding handlers to other objects on the screen, such as a paddle to reflect our pong ball.