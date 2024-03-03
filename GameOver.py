import pygame



pygame.mixer.init()

def game_over():
    pygame.mixer.stop()
    print("Your HP dropped to Zero... You failed us all!!! ")
    pygame.mixer.music.load("Audio/GameOver.mp3")
    pygame.mixer.music.play()
    pygame.time.delay(5000)
    exit()





