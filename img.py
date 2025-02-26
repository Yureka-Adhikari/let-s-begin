import pygame

pygame.init()

green = (156, 223, 169)
clock = pygame.time.Clock()

display_surface= pygame.display.set_mode((500,700))
pygame.display.set_caption("porscheee")

image = pygame.image.load('img.jpg')
SIZE= (340,600)

image = pygame.transform.scale(image, SIZE)
POSITION = (80,50)

while True:
    display_surface.fill(green)
    display_surface.blit(image, POSITION)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.display.flip()
    clock.tick(30)
        
        