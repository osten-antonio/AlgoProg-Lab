import pygame

pygame.init()
screen=pygame.display.set_mode((1200,720))
clock=pygame.time.Clock()

running=True
dt=0

player_pos=pygame.Vector2(screen.get_width() / 2, screen.get_height() /2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill('purple')
        pygame.draw.circle(screen,'red',player_pos,40)

        keys=pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 200 * dt
            if player_pos.y < 40:
                player_pos.y = 40
        if keys[pygame.K_a]:
            player_pos.x -= 200 * dt
            if player_pos.x < 40:
                player_pos.x = 40
        if keys[pygame.K_s]:
            player_pos.y += 200 * dt
            if player_pos.y > 680:
                player_pos.y = 680
        if keys[pygame.K_d]:
            player_pos.x += 200 * dt
            if player_pos.x > 1160:
                player_pos.x = 1160



        pygame.display.flip()
        dt=clock.tick(60)/1000
pygame.quit()