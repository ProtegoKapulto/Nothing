import Player
import time
import GameOver
import random
import Monster
import pygame
import Game
import os

pygame.init()
pygame.mixer.init()
mana_absorption_shield = False # Damit das Schild nicht aktiv ist
fire = 0 # Damit Feuer und Eis nicht aktiv sind
frozen = 0
fight = True # Damit Game Over richtig funktioniert

monika = Monster.Monster(50, "Monika", "Audio/copyrightisforlosers.mp3", "She")  # Secret Boss (Wurde eigentlich nur zum Testen im Spiel genutzt)
monika.monster_attack_names("Deletes a File", "Deletes all of your Files", "Just Monika")
monika.monster_attack_damage(random.choice([20, 20, 20, 50]), random.choice([20, 40, 40, 50]),
                             random.choice([20, 20, 50, 100]))

spit_tank = Monster.Monster(25, "Spit Tank", "Audio/virginOST.mp3", "He")  # Finaler Boss
spit_tank.monster_attack_names("Bad Grading", "Slap of Destruction", "Hoodi Strangler")
spit_tank.monster_attack_damage(random.choice([20, 20, 20, 30]), random.choice([20, 20, 30, 40]) ,random.choice([20, 20, 30, 50]))

goblin = Monster.Monster(15, "Goblin", "Audio/goblinfight.mp3", "It") # Alle diese Gegner werden hier definiert oben definiert
goblin.monster_attack_names("Bite", "Punch", "club swing")
goblin.monster_attack_damage(10, 15, 20)

orc = Monster.Monster(20, "Orc", "Audio/2dminecraft.mp3", "It")
orc.monster_attack_names("Stomp", "Stone Throw", "Magic Fireball Shot")
orc.monster_attack_damage(15, 20, 25)

ordinary_spider = Monster.Monster(25, "Ordinary Spider", "Audio/epicspiderdance.mp3", "It")
ordinary_spider.monster_attack_names("Web Entanglement", "Piercing Pincers", "Arachnid Assault")
ordinary_spider.monster_attack_damage(20, 25, 30)

code_waver = Monster.Monster(30, "Coder Waver", "Audio/lovethisone.mp3", "It")
code_waver.monster_attack_names("Laser String", "Binary Web Assault", f"Hi {os.getlogin()}", )
code_waver.monster_attack_damage(25, 30, 35)


def fight_start(monster): # Startet den Kampf
    if fight == True: # Damit nachdem das Monster besiegt wurde, der Kampf nicht weitergeht
        monster.music()
        print(animated_text(f"{monster.monster_name} is challenging you to a fight!!!"))
        player_turn()
    else:
        return


def player_turn(): # Wahl des Angriffs
    global damage
    global fight
    if fight == True:
        if monster.monster_health <= 0:
            return
        fight_answer = input(animated_text(f"""
        What do you want to do?
            Sword
            Magic
            Absorbing Mana Shield
            Run

            You have {player.player_health} HP and {player.mana} Mana

            """))
        if fight_answer.lower() == "sword" or fight_answer.lower() == "s":
            damage = player.sword()
            monster_health()
        elif fight_answer.lower() == "magic" or fight_answer.lower() == "m":
            magic()
        elif fight_answer.lower() == "absorbing mana shield" or fight_answer.lower() == "a" or fight_answer.lower() == "shield":
            shield()
        elif fight_answer.lower() == "run" or fight_answer.lower() == "r":
            run = random.choice([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
            if run == 1:
                pygame.mixer.Sound("Audio/run.mp3").play()
                print(animated_text("Wow you managed to run away you coward!!!"))
                fight = False
                return

            else:
                print(animated_text("You tried to run away but failed!!!"))
                pygame.mixer.Sound("Audio/fall.mp3").play()
                monster_attack()
        else:
            try_again()
    else:
        return


def try_again():  # Wenn man eine ungültige Eingabe in der Angriffsauswahl tätigt
    player_turn()


def monster_attack():  # Wird zum ausgeben der Art des Angriffs vom Monster genutzt und der Anzahl des Schadens am Spieler
    global frozen
    global damage

    attack = random.choice([1, 1, 1, 1, 2, 2, 2, 3])
    if frozen > 0:
        frozen_effect()
    else:
        if attack == 1:
            print(animated_text(f"{monster.monster_name} uses {monster.attack_name1}"))
            damage = monster.attack_damage1
            shield_check()
            if fight == True:
                player.damage(damage)
                print(animated_text(f"{monster.monster_name} gave you {monster.attack_damage1} damage"))
        elif attack == 2:
            print(animated_text(f"{monster.monster_name} uses {monster.attack_name2}"))
            damage = monster.attack_damage2
            shield_check()
            if fight == True:
                player.damage(damage)
                print(animated_text(f"{monster.monster_name} gave you {monster.attack_damage2} damage"))
        elif attack == 3:
            print(animated_text(f"{monster.monster_name} uses {monster.attack_name3}"))
            damage = monster.attack_damage3
            shield_check()
            if fight == True:
                player.damage(damage)
                print(animated_text(f"{monster.monster_name} gave you {monster.attack_damage3} damage"))
    if player.player_health <= 0:
        GameOver.game_over()
    else:
        player_turn()


def monster_health(): # Zum Ausgeben des Schadens an dem Monster
    global damage
    global fire
    global fight
    monster.monster_health_reduction(damage)
    if fire > 0:
        print(animated_text(f"You´ve dealt {monster.monster_name} {damage} damage and the fire made it loose 3 HP!!!"))
        monster.monster_health -= 3
        fire -= 1
    else:
        print(animated_text(f"You´ve dealt {monster.monster_name} {damage} damage!!!"))
    if monster.monster_health <= 0:
        print(animated_text(f"""{monster.monster_name} Health dropped to zero.
You Win!!!"""))
        fight = False
        return
    else:
        print(animated_text(f"{monster.monster_name} has {monster.monster_health} HP"))
        monster_attack()





def animated_text(text):  # Animation von ChatGPT erstellt
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)  # Zeit für nächsten Buchstaben hier konfigurierbar
    return ("")


def shield(): # Aktiviert den Schild effekt
    global mana_absorption_shield
    mana_absorption_shield = True
    monster_attack()


def shield_check(): # Überprüft ob das Schild aktiv ist
    global mana_absorption_shield
    global damage
    if mana_absorption_shield == True:
        player.shield()
        mana_absorption_shield = False
        print(animated_text(
            f"{monster.monster_name} tried to attack you, but due to your Absorbing Mana Shield, the damage was reduced and you refilled your Mana!!! "))
        damage -= 11
        if damage > 0:
            if fight == True:
                print(animated_text(f"{monster.monster_name} gave you {damage} damage"))
                player.damage(damage)
        elif damage == 0:
            print(animated_text(f"You blocked {monster.monster_name} attack!!!"))

        elif damage < 0:
            print(animated_text(
                f"Wow you blocked {monster.monster_name} attack and regained 1 HP!! How is this even possible???"))
            player.damage(damage)
        if player.player_health <= 0:
            GameOver.game_over()
        else:
            player_turn()


def fire_duration(): #  Legt fest wie lange das Monster brennt und gibt ihm etwas Schaden
    global damage
    global fire
    damage = random.choice([1, 2, 3])
    fire = random.choice([1, 1, 2, 2, 2, 2, 2, 3])
    print(animated_text(f"You made {monster.monster_name} go up in Flames!!!"))
    monster_health()


def ice_duration(): # friert das Monster ein für 2 Runden
    global frozen
    frozen = 2
    monster_attack()


def frozen_effect(): # Informiert den Spieler, dass das Monster eingefroren wurde
    global frozen
    global mana_absorption_shield
    if mana_absorption_shield == True:
        player.shield()
        mana_absorption_shield = False
    if frozen == 1:
        print(animated_text(
            f"{monster.monster_name} was frozen!!! {monster.monster_pronouns} won´t be able to attack this round!!! "))
        frozen -= 1
        player_turn()
    elif frozen == 2:
        print(animated_text(
            f"{monster.monster_name} was frozen!!! {monster.monster_pronouns} won´t be able to attack for {frozen} rounds!!! "))
        frozen -= 1
        player_turn()


def stats_reset(): # Stellt die Statuseffekte, die im Kampf gegeben wurden sind auf 0 und macht einen Kampf wieder möglich
    global fight
    global fire
    global frozen
    fight = True
    fire = 0
    frozen = 0


def magic():  # Wahl zwischen der Unterschiedlichen Magie
    global damage
    global player_mana
    magicAnswer = input(animated_text("""Which Magic do you want to use?
    Fire Magic (4 Mana)
    Ice Magic (4 Mana)
    Shadow Magic (6 Mana)
    Light Magic (7 Mana)
    Heal Magic (8 Mana)
    
    back
    """))
    if magicAnswer.lower() == "fire magic" or magicAnswer.lower() == "f":  # Brauche zwei unterschiedliche Fälle für einmal kein Mana und einmal falsche Eingabe
        if player.mana >= 4:
            player.fire_magic()
            fire_duration()
        else:
            print(animated_text("Not enough Mana for Fire Magic"))
            magic_return()

    elif magicAnswer.lower() == "ice magic" or magicAnswer.lower() == "i":
        if player.mana >= 4:
            player.ice_magic()
            ice_duration()
        else:
            print(animated_text("Not enough Mana for Ice Magic"))
            magic_return()

    elif magicAnswer.lower() == "shadow magic" or magicAnswer.lower() == "s":
        if player.mana >= 6:
            damage = player.shadow_magic()
            print(f"You envelop {monster.monster_name} in a shadow!!!")
            monster_health()
        else:
            print(animated_text("Not enough Mana for Shadow Magic"))
            magic_return()
    elif magicAnswer.lower() == "light magic" or magicAnswer.lower() == "l":
        if player.mana >= 7:
            damage = player.light_magic()
            monster_health()
        else:
            print(animated_text("Not enough Mana for Light Magic"))
            magic_return()
    elif magicAnswer.lower() == "heal magic" or magicAnswer.lower() == "h":
        if player.mana >= 8:
            player.heal_magic()
            print(f"You regenerated all of your hp")
            monster_attack()
        else:
            print(animated_text("Not enough Mana for Heal Magic"))
            magic_return()
    else:
        player_turn()


def magic_return(): # Bei nicht genug Mana wird man zurück auf die Auswahl der Magie Arten gebracht
    magic()

if __name__ == "__main__":
    game = Game.Game()  # Der Verlauf des Spiels wird hier angezeigt
    pygame.mixer.music.load("Audio/origetsisekaied.mp3")
    pygame.mixer.music.play(-1)
    pygame.time.delay(0)
    player = Player.Player(input(animated_text("What will the name of the legendary Hero be? ")))
    game.game_opening(player.name)
    game.first_scene(player.name)
    monster = goblin
    fight_start(monster)
    game.second_scene(player.name)
    way_answer = input(animated_text("Right or Left?: "))
    if way_answer.lower() == "right" or way_answer.lower() == "r":
        game.tunnel(player.name)
        monster = orc
        stats_reset()
        fight_start(monster)
    elif way_answer.lower() == "left" or way_answer.lower() == "l":
        game.ladder(player.name)
    else:
        game.secret_ending1(player.name)
        monster = monika
        stats_reset()
        fight_start(monster)
        game.secret_ending2(player.name)
    game.third_scene(player.name)
    monster = ordinary_spider
    stats_reset()
    fight_start(monster)
    game.forth_scene(player.name)
    monster = code_waver
    stats_reset()
    fight_start(monster)
    game.fifth_scene(player.name)
    monster = spit_tank
    stats_reset()
    fight_start(monster)
    game.last_scene(player.name)
    game.credits(player.name)


