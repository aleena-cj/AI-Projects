import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Catch Adventure")

# Colors
SKY = (135, 206, 235)
GRASS = (34, 177, 76)
WHITE = (255, 255, 255)
RED = (220, 20, 60)
YELLOW = (255, 215, 0)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
DARK_GREEN = (0, 100, 0)

title_font = pygame.font.SysFont("arial", 60, bold=True)
font = pygame.font.SysFont("arial", 32)
small_font = pygame.font.SysFont("arial", 25)

clock = pygame.time.Clock()

basket = pygame.Rect(400, 550, 120, 50)

score = 0
lives = 3
level = 1

items = []


def create_item():
    item_type = random.choice(["apple", "banana", "bomb"])

    return {
        "type": item_type,
        "x": random.randint(50, 850),
        "y": -50
    }


for _ in range(5):
    items.append(create_item())


def draw_cloud(x, y):
    pygame.draw.circle(screen, WHITE, (x, y), 25)
    pygame.draw.circle(screen, WHITE, (x + 25, y - 10), 30)
    pygame.draw.circle(screen, WHITE, (x + 55, y), 25)


def draw_apple(x, y):
    pygame.draw.circle(screen, RED, (x, y), 18)
    pygame.draw.rect(screen, DARK_GREEN, (x - 2, y - 25, 4, 10))


def draw_banana(x, y):
    pygame.draw.arc(screen, YELLOW,
                    (x - 20, y - 15, 40, 30),
                    0.5, 2.8, 8)


def draw_bomb(x, y):
    pygame.draw.circle(screen, BLACK, (x, y), 15)
    pygame.draw.line(screen, RED,
                     (x, y - 15),
                     (x, y - 25), 3)


def draw_background():
    screen.fill(SKY)

    draw_cloud(100, 80)
    draw_cloud(350, 120)
    draw_cloud(700, 90)

    pygame.draw.rect(screen,
                     GRASS,
                     (0, 600, WIDTH, 50))


def draw_basket():
    pygame.draw.rect(screen,
                     BROWN,
                     basket,
                     border_radius=10)

    pygame.draw.line(screen,
                     BLACK,
                     (basket.x,
                      basket.y + 10),
                     (basket.x + 120,
                      basket.y + 10), 2)


def show_start():
    while True:

        draw_background()

        title = title_font.render(
            "FRUIT CATCH ADVENTURE",
            True,
            BLACK)

        text = font.render(
            "Press ENTER to Start",
            True,
            BLACK)

        screen.blit(title, (110, 200))
        screen.blit(text, (300, 320))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    return


show_start()

running = True

while running:

    clock.tick(60)

    if score >= 20:
        level = 3
    elif score >= 10:
        level = 2
    else:
        level = 1

    speed = 4 + level

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        basket.x -= 8

    if keys[pygame.K_RIGHT]:
        basket.x += 8

    basket.x = max(0, min(WIDTH - basket.width,
                          basket.x))

    draw_background()

    for item in items:

        item["y"] += speed

        if item["type"] == "apple":
            draw_apple(item["x"],
                       item["y"])

        elif item["type"] == "banana":
            draw_banana(item["x"],
                        item["y"])

        else:
            draw_bomb(item["x"],
                      item["y"])

        item_rect = pygame.Rect(
            item["x"] - 20,
            item["y"] - 20,
            40,
            40)

        if basket.colliderect(item_rect):

            if item["type"] == "apple":
                score += 1

            elif item["type"] == "banana":
                score += 2

            else:
                lives -= 1

            item.update(create_item())

        if item["y"] > HEIGHT:
            item.update(create_item())

    draw_basket()

    pygame.draw.rect(
        screen,
        WHITE,
        (10, 10, 300, 90),
        border_radius=10)

    score_text = font.render(
        f"Score: {score}",
        True,
        BLACK)

    level_text = small_font.render(
        f"Level: {level}",
        True,
        BLACK)

    lives_text = small_font.render(
        f"Lives: {'❤️'*lives}",
        True,
        RED)

    screen.blit(score_text, (20, 15))
    screen.blit(level_text, (20, 55))
    screen.blit(lives_text, (140, 55))

    if lives <= 0:

        while True:

            draw_background()

            over = title_font.render(
                "GAME OVER",
                True,
                RED)

            final = font.render(
                f"Final Score: {score}",
                True,
                BLACK)

            restart = small_font.render(
                "Press R to Restart | ESC to Exit",
                True,
                BLACK)

            screen.blit(over, (250, 220))
            screen.blit(final, (340, 320))
            screen.blit(restart, (240, 400))

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_r:

                        score = 0
                        lives = 3
                        level = 1

                        items.clear()

                        for _ in range(5):
                            items.append(create_item())

                        basket.x = 400
                        break

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            else:
                continue
            break

    pygame.display.update()