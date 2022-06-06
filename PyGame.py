

from tkinter import messagebox , Tk
import pygame,sys,random


width,height = 400,400
game_screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()

x, y = 200,200
delta_x , delta_y = 0, 0

def snack() : 
    global x , y
    x = x + delta_x
    y = y + delta_y
    pygame.draw.rect(game_screen,(255,255,255),[x,y,10,10])
    pygame.display.update()


def main() :
    
    # Snacks
    
   
    
     
    run = True
    while run :
        # Quit 
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
                snack()
                # Snack Movements 
             
                
                # Game Over 
              
                
                # Draw 
                window.fill((0, 0, 0))
                
                # Update 
                pygame.display.flip()
                clock.tick(8)
                
main()