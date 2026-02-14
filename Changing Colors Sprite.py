import pygame

def main():
    print("Starting color changing sprite application...")
    pygame.init()
    screen_width, screen_height = 500,500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('color changing sprite')
    print("Window created. Application running...")

    colors = {
        'red':pygame.Color('red'),
        'green' : pygame.Color('green'),
        'blue': pygame.Color('Blue'),
        'yellow': pygame.Color('yellow'),
        'white': pygame.Color('white')
   }
    current_color = colors['white']

    x,y = 30,30
    sprite_width, sprite_height = 60,60

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    current_color = colors['red']
                elif event.key == pygame.K_g:
                    current_color = colors['green']
                elif event.key == pygame.K_b:
                    current_color = colors['blue']
                elif event.key == pygame.K_y:
                    current_color = colors['yellow']
                elif event.key == pygame.K_w:
                    current_color = colors['white']
        
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color, (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    print("Application closed.")

if __name__ == "__main__":
    main()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True