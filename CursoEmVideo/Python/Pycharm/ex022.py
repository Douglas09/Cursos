#executa um arquivo MP3 em python

#Exemplo 01
import webbrowser
webbrowser.open('audio.mp3')

#Exemplo 02
from playsound import playsound
playsound('audio.mp3')

#Exemplo 03
import pygame
pygame.init()
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
pygame.event.wait()
