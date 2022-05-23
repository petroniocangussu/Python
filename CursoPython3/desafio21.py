#Programa que abre e reproduz um arquivo em mp3 - usar modulo
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('desafio21.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()