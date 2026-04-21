import pygame
import math
import datetime

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Clock")

font = pygame.font.SysFont(None, 40)

center = (300, 300)
radius = 200

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 0), center, radius, 3)
    pygame.draw.circle(screen, (0, 0, 0), center, 5)

    for i in range(12):
        angle = i * 30 - 90

        x1 = center[0] + radius * math.cos(math.radians(angle))
        y1 = center[1] + radius * math.sin(math.radians(angle))

        x2 = center[0] + (radius - 20) * math.cos(math.radians(angle))
        y2 = center[1] + (radius - 20) * math.sin(math.radians(angle))

        pygame.draw.line(screen, (0, 0, 0), (x1, y1), (x2, y2), 3)

        if i % 3 == 0:
            number = str(i if i != 0 else 12)

            text = font.render(number, True, (0, 0, 0))

            x = center[0] + (radius - 40) * math.cos(math.radians(angle))
            y = center[1] + (radius - 40) * math.sin(math.radians(angle))

            text_rect = text.get_rect(center=(x, y))
            screen.blit(text, text_rect)

    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute


    second_angle = seconds * 6 - 90
    minute_angle = minutes * 6 - 90

    sec_length = 150
    sec_x = center[0] + sec_length * math.cos(math.radians(second_angle))
    sec_y = center[1] + sec_length * math.sin(math.radians(second_angle))

    pygame.draw.line(screen, (0, 0, 255), center, (sec_x, sec_y), 2)

    min_length = 100
    min_x = center[0] + min_length * math.cos(math.radians(minute_angle))
    min_y = center[1] + min_length * math.sin(math.radians(minute_angle))

    pygame.draw.line(screen, (255, 0, 0), center, (min_x, min_y), 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()