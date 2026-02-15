import pygame

pygame.init()
screen_width,screen_height = 640,480
display = pygame.display.set_mode((640,480))
pygame.display.set_caption("My First Game Screen")
GREEN = (0,255,0)

font = pygame.font.Font(None, 48)
text = "Hello, Pygame!"
text_color = (255, 255, 255) 
bg_color = (0, 0, 0)     
display.fill(bg_color)

rect_width = 200
rect_height = 100

rect = pygame.Rect(0, 0, rect_width, rect_height)
rect.center = (screen_width // 2, screen_height // 2)

text_surface = font.render(text, True, text_color)

text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    display.fill(bg_color)
    display.blit(text_surface, text_rect)
    pygame.draw.rect(display, GREEN, rect)
    pygame.display.flip()