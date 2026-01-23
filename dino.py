import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60
GRAVITY = 0.8
JUMP_STRENGTH = -19
GAME_SPEED = 9
OBSTACLE_FREQUENCY = 0.02  # Higher = more obstacles

# Colors
SKY_BLUE = (135, 206, 235)
GROUND_COLOR = (222, 184, 135)
RED = (255, 50, 50)
GREEN = (50, 200, 50)
BLUE = (50, 150, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 60
        self.vel_y = 0
        self.jumping = False
        self.color = BLUE
        self.score = 0
        
    def jump(self):
        if not self.jumping:
            self.vel_y = JUMP_STRENGTH
            self.jumping = True
    
    def update(self):
        # Apply gravity
        self.vel_y += GRAVITY
        self.y += self.vel_y
        
        # Check if player is on the ground
        ground_level = SCREEN_HEIGHT - 100
        if self.y >= ground_level - self.height:
            self.y = ground_level - self.height
            self.jumping = False
            self.vel_y = 0
    
    def draw(self, screen):
        # Draw player body
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0, 10)
        
        # Draw player eyes
        eye_radius = 5
        pygame.draw.circle(screen, WHITE, (self.x + 30, self.y + 15), eye_radius)
        pygame.draw.circle(screen, BLACK, (self.x + 30, self.y + 15), eye_radius // 2)
        
        # Draw player smile
        pygame.draw.arc(screen, RED, (self.x + 10, self.y + 25, 20, 15), 0, 3.14, 3)
        
        # Draw player legs (running animation)
        leg_y = self.y + self.height
        leg_offset = (pygame.time.get_ticks() // 100) % 20 - 10
        pygame.draw.line(screen, BLACK, (self.x + 10, leg_y), 
                        (self.x + 10, leg_y + 20 + leg_offset), 4)
        pygame.draw.line(screen, BLACK, (self.x + 30, leg_y), 
                        (self.x + 30, leg_y + 20 - leg_offset), 4)
    
    def get_rect(self):
        return pygame.Rect(self.x + 5, self.y + 5, self.width - 10, self.height - 10)

class Obstacle:
    def __init__(self, x):
        self.x = x
        self.width = random.randint(20, 40)
        self.height = random.randint(30, 70)
        self.y = SCREEN_HEIGHT - 100 - self.height
        self.color = random.choice([RED, GREEN, YELLOW])
        self.passed = False
    
    def update(self):
        self.x -= GAME_SPEED
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0, 5)
        
        # Add pattern to obstacle
        pattern_color = (self.color[0]//2, self.color[1]//2, self.color[2]//2)
        pygame.draw.rect(screen, pattern_color, 
                        (self.x + 5, self.y + 5, self.width - 10, self.height - 10), 2, 3)
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def is_off_screen(self):
        return self.x + self.width < 0

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = random.randint(50, 200)
        self.speed = random.uniform(0.5, 2.0)
        self.size = random.randint(40, 80)
    
    def update(self):
        self.x -= self.speed
    
    def draw(self, screen):
        # Draw fluffy cloud
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.size // 2)
        pygame.draw.circle(screen, WHITE, (int(self.x) + self.size // 3, int(self.y) - self.size // 6), self.size // 2)
        pygame.draw.circle(screen, WHITE, (int(self.x) + self.size // 2, int(self.y)), self.size // 2)
    
    def is_off_screen(self):
        return self.x + self.size < 0

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Adventures of Habibi")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.small_font = pygame.font.SysFont(None, 24)
        
        self.reset_game()
    
    def reset_game(self):
        self.player = Player(100, SCREEN_HEIGHT - 160)
        self.obstacles = []
        self.clouds = []
        self.game_over = False
        self.game_speed = GAME_SPEED
        self.score = 0
        self.high_score = self.load_high_score()
        
        # Create initial clouds
        for _ in range(5):
            cloud = Cloud()
            cloud.x = random.randint(0, SCREEN_WIDTH)
            self.clouds.append(cloud)
    
    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as file:
                return int(file.read())
        except:
            return 0
    
    def save_high_score(self):
        try:
            with open("highscore.txt", "w") as file:
                file.write(str(self.high_score))
        except:
            pass
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    if self.game_over:
                        self.reset_game()
                    else:
                        self.player.jump()
                
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.reset_game()
                else:
                    self.player.jump()
    
    def update(self):
        if not self.game_over:
            # Update player
            self.player.update()
            
            # Update score based on player's survival time
            self.score += 0.1
            self.player.score = int(self.score)
            
            # Update high score
            if self.player.score > self.high_score:
                self.high_score = self.player.score
            
            # Randomly generate obstacles
            if random.random() < OBSTACLE_FREQUENCY:
                self.obstacles.append(Obstacle(SCREEN_WIDTH))
            
            # Update obstacles
            for obstacle in self.obstacles[:]:
                obstacle.update()
                
                # Check for collision
                if self.player.get_rect().colliderect(obstacle.get_rect()):
                    self.game_over = True
                    self.save_high_score()
                
                # Check if obstacle is off screen
                if obstacle.is_off_screen():
                    self.obstacles.remove(obstacle)
            
            # Randomly generate clouds
            if random.random() < 0.01:
                self.clouds.append(Cloud())
            
            # Update clouds
            for cloud in self.clouds[:]:
                cloud.update()
                if cloud.is_off_screen():
                    self.clouds.remove(cloud)
    
    def draw(self):
        # Draw sky background
        self.screen.fill(SKY_BLUE)
        
        # Draw clouds
        for cloud in self.clouds:
            cloud.draw(self.screen)
        
        # Draw sun
        pygame.draw.circle(self.screen, YELLOW, (900, 80), 50)
        
        # Draw ground
        pygame.draw.rect(self.screen, GROUND_COLOR, (0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 100))
        
        # Draw ground pattern
        for i in range(20):
            x = (pygame.time.get_ticks() // 10 + i * 50) % (SCREEN_WIDTH + 50) - 50
            pygame.draw.line(self.screen, (200, 160, 120), 
                            (x, SCREEN_HEIGHT - 100), 
                            (x, SCREEN_HEIGHT), 3)
        
        # Draw player
        self.player.draw(self.screen)
        
        # Draw obstacles
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
        
        # Draw score
        score_text = self.font.render(f"Score: {self.player.score}", True, WHITE)
        self.screen.blit(score_text, (20, 20))
        
        # Draw high score
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, YELLOW)
        self.screen.blit(high_score_text, (20, 60))
        
        # Draw controls info
        controls_text = self.small_font.render("Press SPACE/UP or CLICK to jump", True, WHITE)
        self.screen.blit(controls_text, (20, SCREEN_HEIGHT - 40))
        
        # Draw game over screen
        if self.game_over:
            # Semi-transparent overlay
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            self.screen.blit(overlay, (0, 0))
            
            # Game over text
            game_over_font = pygame.font.SysFont(None, 72)
            game_over_text = game_over_font.render("GAME OVER", True, RED)
            self.screen.blit(game_over_text, 
                            (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 
                             SCREEN_HEIGHT // 2 - 100))
            
            # Final score
            final_score_text = self.font.render(f"Final Score: {self.player.score}", True, WHITE)
            self.screen.blit(final_score_text, 
                            (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, 
                             SCREEN_HEIGHT // 2 - 20))
            
            # Restart instruction
            restart_text = self.font.render("Press SPACE or CLICK to restart", True, GREEN)
            self.screen.blit(restart_text, 
                            (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 
                             SCREEN_HEIGHT // 2 + 40))
            
            # Habibi message
            habibi_text = self.font.render("Don't worry, habibi! Try again!", True, YELLOW)
            self.screen.blit(habibi_text, 
                            (SCREEN_WIDTH // 2 - habibi_text.get_width() // 2, 
                             SCREEN_HEIGHT // 2 + 100))
        
        # Draw title
        title_font = pygame.font.SysFont(None, 48)
        title_text = title_font.render("Adventures of habibi", True, BLUE)
        self.screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 10))
        
        # Update display
        pygame.display.flip()
    
    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

# Start the game
if __name__ == "__main__":
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Make sure you have pygame installed: pip install pygame")
        pygame.quit()