
import pygame

#Creating window
background_colour = (245,245,245)
(width, height) = (300, 200)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bugz World')

screen.fill(background_colour)
pygame.display.flip()

bug = pygame.display.set_mode((500, 500))
#objext cordinates
x = 200
y = 200

#dimensions of object
width = 20
height = 20

vel = 10

run = True
while run:
    # creates time delay of 10ms 
    pygame.time.delay(10)
      
    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method.  
    for event in pygame.event.get():
          
        # if event object type is QUIT  
        # then quitting the pygame  
        # and program both.  
        if event.type == pygame.QUIT:
              
            # it will make exit the while loop 
            run = False
    # stores keys pressed 
    keys = pygame.key.get_pressed()
      
    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x>0:
          
        # decrement in x co-ordinate
        x -= vel
          
    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x<500-width:
          
        # increment in x co-ordinate
        x += vel
         
    # if left arrow key is pressed   
    if keys[pygame.K_UP] and y>0:
          
        # decrement in y co-ordinate
        y -= vel
          
    # if left arrow key is pressed   
    if keys[pygame.K_DOWN] and y<500-height:
        # increment in y co-ordinate
        y += vel
         
              
    # completely fill the surface object  
    # with black colour  
    bug.fill((0, 0, 0))
      
    # drawing object on screen which is rectangle here 
    pygame.draw.rect(bug, (255, 0, 0), (x, y, width, height))
      
    # it refreshes the window
    pygame.display.update() 
  
# closes the pygame window 
pygame.quit()
