# Faça um programa em python que abra e reproduza um áudio em MP3.

from pygame import *
mixer.init()
mixer.music.load('musica.mp3')
mixer.music.play()

while mixer.music.get_busy():
    time.Clock().tick(10)
