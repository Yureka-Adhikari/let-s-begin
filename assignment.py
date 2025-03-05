import pygame

pygame.init()

green = (85, 142, 77)
clock = pygame.time.Clock()

display_surface= pygame.display.set_mode((500,700))
pygame.display.set_caption("assignmentttt")

image1 = pygame.image.load('assig.jpg')
image2 = pygame.image.load('assignment2.jpg')
image3 = pygame.image.load('assignment3.jpg')
SIZE1= (100,160)
SIZE2= (100,140)
SIZE3= (110,180)

image1 = pygame.transform.scale(image1, SIZE1)
image2 = pygame.transform.scale(image2, SIZE2)
image3 = pygame.transform.scale(image3, SIZE3)
POSITION1 = (200,100)
POSITION2 = (200,500)
POSITION3 = (190,300)

while True:
    display_surface.fill(green)
    display_surface.blit(image1, POSITION1)
    display_surface.blit(image2, POSITION2)
    display_surface.blit(image3, POSITION3)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.display.flip()
    clock.tick(30)
        
        