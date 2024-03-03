import pygame
pygame.mixer.init()



class Monster:
    def __init__(self, monster_health, monster_name, monster_music, monster_pronouns):
        self.monster_health = monster_health
        self.monster_name = monster_name
        self.monster_music = monster_music
        self.monster_pronouns = monster_pronouns
    def monster_health_reduction(self,damage):
        self.monster_health -= damage

    def monster_attack_names (self, attack_name1, attack_name2, attack_name3,):
        self.attack_name1 = attack_name1
        self.attack_name2 = attack_name2
        self.attack_name3 = attack_name3
    def monster_attack_damage(self, player_damage1, player_damage2, player_damage3):
        self.attack_damage1 = player_damage1
        self.attack_damage2 = player_damage2
        self.attack_damage3 = player_damage3
    def music(self):
        pygame.mixer.stop()
        pygame.mixer.music.load(self.monster_music)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        pygame.time.delay(0)








