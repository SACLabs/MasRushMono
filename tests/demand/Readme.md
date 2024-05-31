# This is the description of demand

## Theme

A python implementation snake game. 

The snake's goal is to eat the food continuously and fill the map with its bodies as soon as possible.

For better understanding, you could check the snake game's definition on: https://en.wikipedia.org/wiki/Snake_(1998_video_game)

## Components

The source code should cover the following components, each component is implenmented by a class and written in a seperate .py file:

- A Snake class that represents the snake in the game. It should have attributes and methods to track the snake's position, direction, length, and movement.
- A Map class that represents the game board or grid. It should have methods to create food for the snake, check if the game board is full, and track the state of each grid cell (empty, snake body, snake head, or food).
- A Direc class that defines the possible directions the snake can move (up, down, left, right).
- A PointType class that defines the different types of grid cells (empty, snake body, snake head, etc.).
- A Pos class or module that represents the position or coordinates of a grid cell.
- The game logic should handle snake movement, eating food, growing the snake's length, detecting collisions with walls or the snake's body, and updating the game board accordingly.

## Requirement
The implementation should follow the structure and behavior implied by the test cases in test_snake.py. 

Please provide the Python source code that satisfies the test cases and implements the snake game as described.

##  Reference

https://github.com/chuyangliu/snake.git