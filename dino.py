import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300
GROUND_HEIGHT = 250
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chrome Dino Game")
clock = pygame.time.Clock()

# Load images (replace with your own paths or use rectangles)
def load_image(name, scale=1):
    img = pygame.Surface((50, 50), pygame.SRCALPHA)
    pygame.draw.rect(img, BLACK, (0, 0, 50, 50))  # Placeholder for dino
    pygame.draw.rect(img, (100, 100, 100), (10, 10, 30, 30))  # Dino "eyes"
    return pygame.transform.scale(img, (50 * scale, 50 * scale))

# Game variables
class Dino:
    def __init__(self):
        self.x = 50
        self.y = GROUND_HEIGHT - 50
        self.jump_velocity = 0
        self.is_jumping = False
        self.image = load_image("dino", 0.8)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def jump(self):
        if not self.is_jumping:
            self.jump_velocity = -15
            self.is_jumping = True

    def update(self):
        # Gravity
        self.jump_velocity += 0.8
        self.y += self.jump_velocity

        # Ground collision
        if self.y >= GROUND_HEIGHT - 50:
            self.y = GROUND_HEIGHT - 50
            self.is_jumping = False
            self.jump_velocity = 0

        self.rect.y = self.y

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Cactus:
    def __init__(self):
        self.width = random.randint(20, 40)
        self.height = random.randint(30, 50)
        self.x = SCREEN_WIDTH
        self.y = GROUND_HEIGHT - self.height
        self.speed = 7
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 100, 0))  # Green cactus
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def is_off_screen(self):
        return self.x < -self.width

# Game objects
dino = Dino()
cacti = []
spawn_timer = 0
score = 0
game_over = False
font = pygame.font.SysFont(None, 36)

def reset_game():
    global dino, cacti, score, game_over
    dino = Dino()
    cacti = []
    score = 0
    game_over = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if game_over:
                    reset_game()
                else:
                    dino.jump()

    if not game_over:
        # Update
        dino.update()

        # Spawn cacti
        spawn_timer += 1
        if spawn_timer >= random.randint(50, 150):
            cacti.append(Cactus())
            spawn_timer = 0

        # Update cacti
        for cactus in cacti[:]:
            cactus.update()
            if cactus.is_off_screen():
                cacti.remove(cactus)
                score += 1

            # Pixel-perfect collision
            if dino.rect.colliderect(cactus.rect):
                game_over = True

    # Draw
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (0, GROUND_HEIGHT + 5), (SCREEN_WIDTH, GROUND_HEIGHT + 5), 2)

    dino.draw()
    for cactus in cacti:
        cactus.draw()

    # Score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    if game_over:
        game_over_text = font.render("Game Over! Press SPACE to restart", True, BLACK)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2))

    pygame.display.flip()
    clock.tick(FPS)