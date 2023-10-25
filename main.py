import pygame
import sys

# ゲーム設定
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 9
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 60

# 色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# プレイヤーの初期位置
player_x, player_y = 0, 0

# Pygameの初期化
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def draw_grid():
    for x in range(0, WIDTH, GRID_WIDTH):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_HEIGHT):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

def main():
    global player_x, player_y

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_y = max(0, player_y - 1)
                elif event.key == pygame.K_DOWN:
                    player_y = min(GRID_SIZE - 1, player_y + 1)
                elif event.key == pygame.K_LEFT:
                    player_x = max(0, player_x - 1)
                elif event.key == pygame.K_RIGHT:
                    player_x = min(GRID_SIZE - 1, player_x + 1)

        screen.fill(BLACK)
        draw_grid()
        pygame.draw.rect(screen, WHITE, (player_x * GRID_WIDTH, player_y * GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT))
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
