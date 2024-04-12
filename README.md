# Pong Game

This Python program utilizes the Turtle module to create a simple Pong game where two players control paddles to bounce a ball back and forth across the screen.

## Features

- **Two Player Gameplay**: Players can control paddles using keyboard inputs to bounce the ball and prevent it from reaching their side.
- **Score Tracking**: The game keeps track of each player's score and displays it on the screen.
- **Collision Detection**: The program detects collisions between the ball, paddles, and walls to determine the direction of the ball's movement.
- **Game Over**: The game ends when one player misses the ball, and their opponent scores a point.

## How It Works

The program uses the Turtle module to create the game objects and handle game logic. Here's how it works:

1. **Setup**: The program initializes the game window, sets up the screen, creates paddles, a ball, and a scoreboard.
2. **Keyboard Controls**: Players can control the paddles using specific keys assigned to each paddle's movement functions.
3. **Main Loop**: The program enters a main loop where it continuously updates the game state and checks for collisions.
4. **Collision Detection**: The program detects collisions between the ball and the paddles or the walls to determine the ball's movement direction.
5. **Score Tracking**: The game keeps track of each player's score and updates the scoreboard accordingly.
6. **Game Over**: The game ends when one player misses the ball, and their opponent scores a point. The game window closes when clicked.

## Usage

1. Run the program using a Python interpreter.
2. Use the following keys to control the paddles:
   - Player 1 (Right Paddle): Up Arrow (Up), Down Arrow (Down)
   - Player 2 (Left Paddle): "w" (Up), "s" (Down)
3. Play the game by bouncing the ball back and forth between the paddles.
4. The game ends when one player misses the ball, and their opponent scores a point.

## Customization

You can customize the program in the following ways:

- **Screen Size**: Adjust the width and height of the game screen by modifying the `screen.setup()` call.
- **Paddle Speed**: Change the speed at which the paddles move by adjusting the `Paddle` class methods.
- **Ball Speed**: Modify the speed at which the ball moves by adjusting the `Ball` class `move_speed` attribute.

## Prerequisites

Before running the program, ensure you have Python installed on your system. The Turtle module is included in the standard Python library, so no additional installation is required.

