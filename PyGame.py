
from tkinter import messagebox , Tk
import pygame,sys,random


window_width,window_height = 500,500
window = pygame.display.set_mode((window_width,window_height))

clock = pygame.time.Clock()

def main() : 
    run = True
    while run :
        # Quit 
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
                
                # Draw 
                
                window.fill((0, 0, 0))
                
                # Update 
                
                pygame.display.flip()
                clock.tick(8)
                
main()