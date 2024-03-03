import pygame
import random
import time
pygame.mixer.init()
class Player:
    def __init__(self, name):
        self.name = name
        self.player_health = 100
        self.mana = 10
    def damage(self,damage):
        self.player_health -= damage
    def shield(self):
        self.mana = 10
        sound_effect_shield = pygame.mixer.Sound("Audio/shield.mp3")
        sound_effect_shield.play()

    def sword(self):
        damage = random.choice([1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6])
        sound_effect_sword = pygame.mixer.Sound("Audio/Sword.mp3")
        sound_effect_sword.play()
        return damage


    def ice_magic(self):
        self.mana -= 4
        sound_effect_ice = pygame.mixer.Sound("Audio/Ice.mp3")
        sound_effect_ice.play()
    def fire_magic(self):
        self.mana -= 4
        sound_effect_fire = pygame.mixer.Sound("Audio/fireball.mp3")
        sound_effect_fire.play()
    def shadow_magic(self):
        self.mana -= 6
        damage = random.choice([4, 5, 6])
        sound_effect_shadow = pygame.mixer.Sound("Audio/shadow.mp3")
        sound_effect_shadow.play()
        return damage
    def light_magic(self):
        self.mana -= 7
        damage = random.choice([5, 6])
        sound_effect_light = pygame.mixer.Sound("Audio/light.mp3")
        sound_effect_light.play()
        return damage


    def heal_magic(self):
        self.mana -= 8
        self.player_health = 100
        sound_effect_heal = pygame.mixer.Sound("Audio/heal.mp3")
        sound_effect_heal.play()




def animated_text(text):  # Animation von ChatGPT erstellt
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01) # Zeit für nächsten Buchstaben hier konfigurierbar
    return ("")
