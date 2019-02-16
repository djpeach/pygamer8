# Getting Started with Pygamer

Pygamer is an opinionated way to build with Pygame that makes developers' lives easier and building games more fun!

Pygamer makes developing python games with [Pygame](https://www.pygame.org/wiki/GettingStarted) quick, modular, maintainable, and scalable. You can load a game window in a matter of seconds, build a simple game in a matter of minutes, and then spend as much time as you want to scale your game as far as you like. And it will be easily maintainable, debuggable, and variable. This is due to the central ideas behind the Pygamer system for Pygame.

## Centrals ideas behind Pygamer

* All Games have objects, players, and menus
* All objects react to events in specific ways (handlers)
* All games and objects need to update and draw on each frame
* Players need to have their own objects that are coupled to their player instance
* Menus should not affect gameplay until active, at which point they should immediately take over the game loop
* The current running Game or Menu should receive and delegate all events to the proper handlers

## Start a game with Pygamer

Check out our [examples](examples) for an introduction on how to create games.
