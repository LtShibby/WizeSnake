"""
WizeSnakeGame.py

A simple implementation of the classic Snake game using Pygame.
The player controls a snake that grows in length as it consumes food.
The game features both manual and AI-controlled modes.

Modules:
- pygame: A library for creating video games in Python.
- time: Provides time-related functions.
- random: Implements pseudo-random number generators.

Classes:
- None

Functions:
- our_snake(snake_block, snake_list): Draws the snake on the display.
- message(msg, color): Displays a message on the screen.
- display_score(score): Renders the current score on the display.
- is_collision(x, y, snake_list): Checks for collisions with the snake's body.
- check_path_clear(start_x, start_y, x_change, y_change, snake_list, steps=100): Checks if the path is clear for a specified number of steps.
- ai_move(x1_change, y1_change, x1, y1, foodx, foody, snake_list, width, height): Controls the AI movement of the snake in a zigzag pattern.
- gameLoop(ai_mode=False): Main game loop that handles game logic and rendering.
"""

import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display dimensions
width = 600
height = 500  # Increased height for the score display
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Wize Snake Game')

# Set clock
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
ai_speed = 9999999  # Increased speed for AI mode

# Font styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
    """
    Draws the snake on the display.

    Parameters:
    - snake_block (int): The size of each segment of the snake.
    - snake_list (list): A list of coordinates representing the snake's body segments.
    """
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    """
    Displays a message on the screen.

    Parameters:
    - msg (str): The message to display.
    - color (tuple): The RGB color of the message.
    """
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])

def display_score(score):
    """
    Renders the current score on the display.

    Parameters:
    - score (int): The current score of the player.
    """
    score_text = score_font.render("Score: " + str(score), True, white)
    display.blit(score_text, [10, 10])  # Display score at the top left

def is_collision(x, y, snake_list):
    """
    Checks for collisions with the snake's body.

    Parameters:
    - x (float): The x-coordinate to check.
    - y (float): The y-coordinate to check.
    - snake_list (list): A list of coordinates representing the snake's body segments.

    Returns:
    - bool: True if there is a collision, False otherwise.
    """
    return [x, y] in snake_list

def check_path_clear(start_x, start_y, x_change, y_change, snake_list, steps=100):
    """
    Checks if the path is clear for a specified number of steps.

    Parameters:
    - start_x (float): The starting x-coordinate.
    - start_y (float): The starting y-coordinate.
    - x_change (int): The change in x-coordinate for each step.
    - y_change (int): The change in y-coordinate for each step.
    - snake_list (list): A list of coordinates representing the snake's body segments.
    - steps (int): The number of steps to check.

    Returns:
    - tuple: (bool, list) where the first element indicates if the path is clear,
              and the second element is the list of positions checked.
    """
    path = []
    for step in range(1, steps + 1):
        next_x = start_x + x_change * step
        next_y = start_y + y_change * step
        if is_collision(next_x, next_y, snake_list):
            return False, path  # Collision detected
        path.append((next_x, next_y))
    return True, path  # No collision

def ai_move(x1_change, y1_change, x1, y1, foodx, foody, snake_list, width, height):
    """
    Controls the AI movement of the snake in a zigzag pattern.

    Parameters:
    - x1_change (int): The current change in the x-coordinate (horizontal movement).
    - y1_change (int): The current change in the y-coordinate (vertical movement).
    - x1 (float): The current x-coordinate of the snake's head.
    - y1 (float): The current y-coordinate of the snake's head.
    - foodx (float): The x-coordinate of the food.
    - foody (float): The y-coordinate of the food.
    - snake_list (list): A list containing the coordinates of the snake's body segments.
    - width (int): The width of the game display.
    - height (int): The height of the game display.

    Returns:
    - tuple: Updated x1_change and y1_change values for the snake's movement.
    """
    # Define the zigzag movement pattern
    if x1 % (2 * snake_block) == 0:  # Check if the snake is at the left edge of the board
        if y1 < height - snake_block:  # If the snake is not at the bottom of the board
            y1_change = snake_block  # Move down
            x1_change = 0  # No horizontal movement
        else:  # If the snake is at the bottom of the board
            x1_change = -snake_block  # Move left
            y1_change = 0  # No vertical movement
    else:  # If the snake is not at the left edge
        if y1 > 0:  # If the snake is not at the top of the board
            y1_change = -snake_block  # Move up
            x1_change = 0  # No horizontal movement
        else:  # If the snake is at the top of the board
            x1_change = -snake_block  # Move left
            y1_change = 0  # No vertical movement

    # Calculate the next position based on the current changes
    next_x = x1 + x1_change
    next_y = y1 + y1_change

    # Check for collisions with the snake's body
    if is_collision(next_x, next_y, snake_list):
        # If a collision is detected, reverse the direction of movement
        x1_change = -x1_change
        y1_change = -y1_change

    return x1_change, y1_change  # Return the updated movement changes

def gameLoop(ai_mode=False):
    """
    Main game loop that handles game logic and rendering.

    Parameters:
    - ai_mode (bool): Flag to indicate if the game is in AI mode (default is False).
    """
    game_over = False
    game_close = False

    x1 = width / 2  # Initial x-coordinate of the snake's head
    y1 = height / 2  # Initial y-coordinate of the snake's head

    x1_change = 0  # Initial change in x-coordinate
    y1_change = 0  # Initial change in y-coordinate

    snake_list = []  # List to store the snake's body segments
    length_of_snake = 1  # Initial length of the snake
    score = 0  # Initialize score

    # Generate initial food position
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            display.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Quit the game
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # Restart the game
                        gameLoop(ai_mode)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Handle window close event
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:  # Toggle AI mode
                    ai_mode = not ai_mode
                if not ai_mode:  # Manual control
                    if event.key == pygame.K_LEFT and x1_change != snake_block:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT and x1_change != -snake_block:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP and y1_change != snake_block:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN and y1_change != -snake_block:
                        y1_change = snake_block
                        x1_change = 0

        # AI movement
        if ai_mode:
            x1_change, y1_change = ai_move(x1_change, y1_change, x1, y1, foodx, foody, snake_list, width, height)

        # Wrap around the screen
        x1 = (x1 + x1_change) % width
        y1 = (y1 + y1_change) % height

        # Log the current position
        print(f"Current Position: ({x1}, {y1})")

        display.fill(blue)  # Clear the display
        pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])  # Draw food
        snake_head = [x1, y1]  # Create a new head for the snake
        snake_list.append(snake_head)  # Add the new head to the snake's body
        if len(snake_list) > length_of_snake:  # If the snake exceeds its length
            del snake_list[0]  # Remove the tail segment

        # Check for self-collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)  # Draw the snake
        display_score(length_of_snake - 1)  # Display score
        pygame.display.update()  # Update the display

        # Check for food consumption
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1  # Increase the length of the snake
            score += 1  # Increment score

        # Increase speed in AI mode
        current_speed = ai_speed if ai_mode else snake_speed
        clock.tick(current_speed)  # Control the game speed

    pygame.quit()  # Quit Pygame
    quit()  # Exit the program

if __name__ == "__main__":
    gameLoop()  # Start the game