import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('goodfeeling.Ogg')
pygame.mixer.music.play()
parar = input('aperte algo para a musica parar ')
pygame.event.wait()