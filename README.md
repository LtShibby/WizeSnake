# Snake Game

A simple implementation of the classic Snake game using Pygame. The player controls a snake that grows in length as it consumes food. The game features both manual and AI-controlled modes.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Controls](#controls)
- [Game Logic](#game-logic)
- [License](#license)

## Features

- Classic Snake gameplay
- Manual control mode
- AI control mode with zigzag movement
- Score tracking
- Collision detection with the snake's body
- Screen wrapping

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/snake-game.git
   cd snake-game
   ```

2. Install the required packages:
   ```bash
   pip install pygame
   ```

## Usage

To run the game, execute the following command in your terminal:

```bash
python snakeGame.py
```

## Controls

- **Arrow Keys**: Control the direction of the snake.
- **I**: Toggle AI mode on and off.
- **C**: Play again after losing.
- **Q**: Quit the game.

## Game Logic

- The snake moves in a zigzag pattern when in AI mode, avoiding collisions with its own body.
- The player can control the snake manually using the arrow keys.
- The game keeps track of the score, which increases as the snake consumes food.
- If the snake collides with itself, the game ends, and the player can choose to play again or quit.