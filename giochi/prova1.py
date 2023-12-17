import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Il mio primo programma")
screen.fill("white")
#screen.fill((255, 255, 255))
pygame.display.flip()
input("Premi INVIO per terminare il programma")
pygame.quit()