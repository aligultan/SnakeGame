import pygame
import random


class Snake():
    def __init__(self):
        # Initialize the attributes
        self.length = 3
        self.position = [(WIDTH // 2, HEIGHT // 2), (WIDTH // 2, HEIGHT // 2 + gridsize),
                         (WIDTH // 2, HEIGHT // 2 + 2 * gridsize)]  # Array of co-ordinates
        self.color = (0, 0, 255)
        self.direction = up
        self.score = 0

    def drawSnake(self, window):
        # Draw a rect for every coordinate in position
        for block in self.position:
            pygame.draw.rect(window, self.color, (block[0], block[1], gridsize, gridsize))

    def movement(self):
        head = self.position[0]
        x, y = self.direction
        # Move in that direction
        next = ((head[0] + x * gridsize) % WIDTH, (head[1] + y * gridsize) % HEIGHT)

        self.position.insert(0, next)
        self.position.pop()

    def check_game_end(self, window):
        if self.position[0] in self.position[1:]:
            # print("game end")
            global Highscore
            Highscore = self.score if self.score > Highscore else Highscore

            myfont = pygame.font.SysFont('Comic Sans MS', 25)
            text = myfont.render("Game Over", True, (0, 0, 0))
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))

            myfont2 = pygame.font.SysFont('Comic Sans MS', 10)
            text2 = myfont.render("Restarts Automatically", True, (0, 0, 0))
            text2_rect = text2.get_rect(center=(WIDTH // 2, HEIGHT // 2))

            window.blit(text, text_rect)
            window.blit(text2, text2_rect)
            pygame.display.update()
            pygame.time.delay(3000)
            self.__init__()

    def change_direction(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if not self.direction == down:
                        self.direction = up
                elif event.key == pygame.K_DOWN:
                    if not self.direction == up:
                        self.direction = down
                elif event.key == pygame.K_LEFT:
                    if not self.direction == right:
                        self.direction = left
                elif event.key == pygame.K_RIGHT:
                    if not self.direction == left:
                        self.direction = right


class Food():
    def __init__(self):
        self.position = (random.randint(0, WIDTH) // grids * grids, random.randint(0, WIDTH) // grids * grids)
        self.color = (0, 0, 0)

    def draw_food(self, window):
        pygame.draw.rect(window, self.color, (self.position[0], self.position[1], gridsize, gridsize))


WIDTH = 400
HEIGHT = 400

grids = 20
gridsize = WIDTH // grids

Highscore = 0

# Defining directions
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)


def setBackground(window):
    window.fill((175, 215, 70))
    # pygame.display.update()


def main():
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WIDTH, HEIGHT))  # pygame window
    pygame.display.set_caption("Snake Game")
    setBackground(window)

    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    while True:
        clock.tick(12)  # 12 frames per second
        snake.movement()
        snake.check_game_end(window)
        setBackground(window)
        snake.check_game_end(window)
        snake.drawSnake(window)
        food.draw_food(window)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if not snake.direction == down:
                        snake.direction = up

                elif event.key == pygame.K_DOWN:
                    if not snake.direction == up:
                        snake.direction = down

                elif event.key == pygame.K_LEFT:
                    if not snake.direction == right:
                        snake.direction = left

                elif event.key == pygame.K_RIGHT:
                    if not snake.direction == left:
                        snake.direction = right

                        # Food Eating code
        if food.position == snake.position[0]:
            # print("Food Eaten")
            snake.length += 1
            snake.score += 1
            snake.position.append((2 * snake.position[-1][0] - snake.position[-2][0], \
                                   2 * snake.position[-1][1] - snake.position[-2][1]))
            food.__init__()

        text = myfont.render('Score: {}'.format(snake.score), True, (0, 0, 0))
        text2 = myfont.render('HighScore: {}'.format(Highscore), True, (0, 0, 0))
        window.blit(text, (0, 0))
        window.blit(text2, (0, 20))
        pygame.display.update()

    return


main()