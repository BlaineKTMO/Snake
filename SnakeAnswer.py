import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake class
class Snake:
    def __init__(self):
        self.positions = [(100, 100), (80, 100), (60, 100)]
        self.direction = (20, 0)
        self.grow = False

    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        
        if self.grow:
            self.positions = [new_head] + self.positions
            self.grow = False
        else:
            self.positions = [new_head] + self.positions[:-1]

    def change_direction(self, direction):
        self.direction = direction

    def check_collision(self):
        head = self.positions[0]
        return head in self.positions[1:] or not (0 <= head[0] < WIDTH and 0 <= head[1] < HEIGHT)

    def grow_snake(self):
        self.grow = True

    def draw(self, surface):
        for pos in self.positions:
            pygame.draw.rect(surface, GREEN, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))

# Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

    def respawn(self):
        self.position = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)

# Main game loop
def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 20):
                    snake.change_direction((0, -20))
                elif event.key == pygame.K_DOWN and snake.direction != (0, -20):
                    snake.change_direction((0, 20))
                elif event.key == pygame.K_LEFT and snake.direction != (20, 0):
                    snake.change_direction((-20, 0))
                elif event.key == pygame.K_RIGHT and snake.direction != (-20, 0):
                    snake.change_direction((20, 0))

        snake.move()

        if snake.positions[0] == food.position:
            snake.grow_snake()
            food.respawn()

        if snake.check_collision():
            running = False

        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()