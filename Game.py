import time
import pygame
import Chatbot

pygame.mixer.init()


def animated_text(text):  # Animation von ChatGPT erstellt
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0)  # Zeit für nächsten Buchstaben hier konfigurierbar (Falls man das Spiel testet, sollte man time.sleep auf 0 setzen)
    return ""


class Game:

    def game_opening(self, name):
        print(animated_text(
            f"""
In a world that was not quite like ours, there lived an ordinary person named {name}. 
{name} was not only an enthusiastic computer user but also a passionate game developer. He spent most of his time in front of the screen, immersed in the complex art of programming. 
One day, {name} was working on his latest project, a game so challenging and detailed that it pushed the limits of his hardware. 
The performance was so high that the temperature of the PC steadily increased. {name} did not notice the warning signs, so concentrated with his work. 
Suddenly, a bright flash of light filled the room, followed by a massive explosion that originated from his computer.
{name} felt a sharp pain, then darkness. When {name} opened his eyes, everything was different. The gray office chair and the blinking computer screen were gone. 
Instead, he found himself in a world that looked like a living version of the game he had been working on. He had been reborn in a fantasy world."""))
        input("""

press Enter to begin your adventure: """)

    def first_scene(self, name):
        pygame.mixer.stop()
        pygame.mixer.music.load("Audio/bestrpg.mp3")
        pygame.mixer.music.play(-1)
        pygame.time.delay(0)
        print(animated_text(f"""
* {name} tries to take a look at his surroundings, but all he can see is an endless abyss of darkness. * 
    {name}: Am I dead? No, it can’t be. I can still sense something. But what is this scent? It’s musty and… it vaguely smells like decay? 
            Even if I am alive, why can’t I see anything? It’s so dark, it’s as if I have my eyes… *opens his eyes* Ah, that explains it. But where am I?
* The moment {name} begins to take in his surroundings, he instantly regrets ever opening his eyes * 
    {name}: How can this be? Everything here mirrors the game I created. 
            The stone walls, the ominous ceiling, everything… It’s identical to my game!!! But how could this happen? 
* suddenly, {name} hears a deafening scream, not one of pain, but of fury. Behind him, a circle adorned with peculiar symbols materializes, and out of it emerges a small green goblin. * 
* It charges towards him, and in an instant, {name} knows exactly what to do… *"""))

    def second_scene(self, name):
        pygame.mixer.stop()
        pygame.mixer.music.load("Audio/bestrpg.mp3")
        pygame.mixer.music.play(-1)
        pygame.time.delay(0)
        print(animated_text(f"""
* The Goblin turns to dust with one last scream of pain. *
    {name}: That was a close one but luckily i somehow knew how to fight??? That was really weird. 
            The only time I came close to defeating someone in a fight was that one time I thought an intruder had broken in to my house but it turned out to be a reflection of mine.
            I think there might still be some shards of glass somewhere inside my hand...
            Anyway it seems like I might have gotten some fighting skills when I was reincarnated in this world and also something that might be magic.
            Its probably not a good time to worry about this, I have to find a way out of this dungeon before another Goblin appears.
            It seems like there are two main ways I could go, the tunnel on the right or I climb a ladder on the left.
            Hmmm which way should I go?"""))

    def tunnel(self, name):
        print(animated_text(f"""
* {name} enters the tunnel. He can hardly see anything except for a dim light at the end this dark hallway. *
   * After quite some time {name} finally reaches the light. *
* {name} looks around. Suddenly he is no longer in the dark tunnel but in a Dripstone Cave *
    {name}: Wow this place is so beautiful. This stones... I somehow feel that they have an enormous magical aura.
            I can´t explain it but I have this urge to touch them.
* The moment {name} gets near one of the stones they start to emit a bright flash *
* The floor begins to shake and a giant Orc emerges from the ground *
* It takes one of the stones and puts it into *
* It gives off a deafening scream and runs towards {name} *
* Once again {name} knows exactly what to do * """))

    def ladder(self, name):
        print(animated_text(f"""
* {name} climbs the ladder *
* Suddenly he is inside a big arena. In front of him is an old looking person in an armor on which some grass has started to grow on*
* He looks at him. He does not seem to be awake.*
* He has a feeling that if he tells him "back" or "exit" he will leave this person behind *
* He comes a bit closer and suddenly the persons eyes are wide open and he opens his mouth... *
"""

                            ))
        Chatbot.chatbot()

    def ladder_second_scene(self, name):
        print(animated_text(f"""
* {name} decides that he talked enough to this deranged man and walks away from him *
* The man screams something at {name} but he is way to focused on what lies ahead and genuinely could not care less*"""))

    def secret_ending1(self, name):
        print(animated_text(f"""
* {name} decides that going nowhere and just staying where he woke up is the best course of action *
* He lays down and takes a nap however it is interrupted by someone speaking *
* {name} looks up and sees a girl sitting besides him and quietly laughing at him*
* {name} is extremely startled buy this. He wants to say something however it is probably the first time he tried to talk to a woman which was not his mother *
* Unable to get a word out Monika seems to get a bit annoyed by him and decides that it would be better for the both of them in this awkward situation if {name} just dies *
    {name}: No wait dont do this, Nooooooooooooo!!!
* However {name} knows exactly what to do (which can not be said about his flirting skills) *"""))

    def secret_ending2(self, name):
        print(animated_text(f"""
* After Monika turned to dust {name} celebrates for a while however he quickly realizes that it is probably nothing to be happy about *
* He realizes that his inability to talk to woman has costed someones live, so he decides to just lay down and wait for someone to kill him *
* This however never happens because no Monster wants to interact with someone like him*
* So {name} continues to lay on the ground till the end of times *"""))
        print(animated_text(f"""
                  You got the Virgin Ending!!!"""))
        exit()

    def third_scene(self, name):
        pygame.mixer.stop()
        pygame.mixer.music.load("Audio/cave.mp3")
        pygame.mixer.music.play()
        pygame.time.delay(0)
        print(animated_text(f"""
* {name} continuous to walk through the dungeon*
* Finally the location seems to change and now he is inside of an almost stereotypical cave. *
* On the walls {name} notices some spiderwebs and he already gets an idea what he will fight next *  
    {name}: Well looks like I might need to fight a spider... So original...
* Suddenly a sound of something crawling is hear. But it is not the sound of a spider, the sounds like something out of metal *
    {name}: Wow, it looks like I might see something more original than a spider.
* Out of the cave comes an ordinary Spider running towards him. *
    {name}: Are you kidding me?!
* {name} knows exactly what to do. *
                
            """))

    def forth_scene(self, name):
        pygame.mixer.stop()
        pygame.mixer.music.load("Audio/thecore.mp3")
        pygame.mixer.music.play()
        pygame.time.delay(0)
        print(animated_text(f"""
* The Spider screams in pain *
    {name}: Well that is one more problem taken care of.
* The Spider begins to scream even harder but instead of turning to dust it begins to grow *
    {name}: What is going on?! You should be dead by now.
* The Spider is now four times of its original size *
* It runs towards the {name} *
* And {name} knows exactly what to... *
* A flashing red light comes from the other end of the cave and hits the Spider *
* The Spider turns to dust immediately *
    {name}: What the hell just happened?!
* The Player walks towards the origin of the red light and once again his surroundings change. *
* Now he is within a different cave. *
* This cave looks similar to the previous one but something is different *
* In the depths of the cave, intricate webs woven intertwine with pulsating lines of code, creating a mesmerizing fusion of ancient enchantment and futuristic technology. *
    {name}: Wow this place, it feels different. I no longer have a sense of magic all around me.
            I feels more like I am back home at my PC programming my Game. I missed this feeling so much.
* From the top of the cave a Spider comes crawling down. Or something that resembles a Spider. *
* It is fully made out of metall and has several coolers on its back *
* You can also see some circuits sticking out of it *
* It notices {name} but does not seem to care about him *
* It continues to crawl towards a wall of the cave and after it reaches it, it stops moving *
* Suddenly out of its back comes something out that resembles a Turret and in the blink of an eye it opens fire on {name} *
* {name} manages to dodge the same red light which killed the Ordinary Spider and once again he feels that he knows exactly what to do. * 
                
                
        """))

    def fifth_scene(self, name):
        pygame.mixer.stop()
        pygame.mixer.music.load("Audio/thecore.mp3")
        pygame.mixer.music.play()
        pygame.time.delay(0)
        print(animated_text(f"""
* The Spider falls to the ground and turns to dust *
* A feeling of relief washes over {name} *
    {name}: This felt different... It was way stronger than the Monsters before it 
            and its attacks also seemed to be different.
            Maybe it means that I am getting closer to the exit?
            Well lets see what awaits me at the end of this cave.
* {name} comes to the end of the cave and he sees a wooden door. *
* {name} tries to open the door but the moment he touches the door knob the floor under him disappears and he falls down *
* After a long time of falling he feels that he finally landed, however everything is still covered in darkness * 
    {name}: Am I finally dead? No wait we already had this already. 
* {name} opens his eyes *
* He looks around. It looks like he might be in a room belonging to a castle *
* He lays on a red carpet and in front of him is a giant golden throne only a giant could possible normally sit on *
* Behind the Throne is an even larger metal Gate *
    {name}: It seems like this Gate over there might be the exit to this Dungeon!!!
            I should quickly get to it before some other monster appears
* However after {name} took one step forward something manifested on the Throne *
* A big pile of machine parts lays on the thrown and the parts one by one begin to hoover and fly towards an other part *
* Slowly those parts begin to resemble something similar a to big cannon than slowly it gets some wheels and finally those wheels get some tracks *
    {name}: Is this a tank?!
* The tank seems to be unhappy that it has no visualization *
* Both look at each other and have a feeling that this battle might decide the future of this world *
* {name} has hopefully the last time the feeling that he knows exactly what to do *
"""))

    def last_scene(self, name):
        pygame.mixer.stop()
        pygame.mixer.music.load("Audio/anending.mp3")
        pygame.mixer.music.play(-1)
        pygame.time.delay(0)
        print(animated_text(f"""
* After a hard fought battle Spit Tank finally turns to dust *
* The Gate slams open and it is filled with a blinding light *
    {name}: Well it looks like this is it.
            Finally I can exit the Dungeon I am so exited to see what lies ahead.
* {name} walks to the gate and turns around, looking at the throne room *
* He gives off a sigh, turns around and goes through the door *
* The door closes behind him and the dungeon gets filled with an endless darkness *
"""))

    def credits(self, name):
        pygame.mixer.stop()
        pygame.mixer.music.load("Audio/world.execute(me).mp3")
        pygame.mixer.music.play()
        pygame.time.delay(0)
        print(animated_text(f"""
        Directed by:    Garry Sidelkivsky
        Written by:     Garry Sidelkivsky
        Creative Writing:   Garry Sidelkivsky
                            Abinaash Sivasundar
                            Hong-Duc Huynh
                            Julien Schumacher
                            John Pascal Schumacher
                            Emil Epstein
        Music by:       Garry Sidelkivsky
                        Abinaash Sivasundar
                        Julien Schumacher
        Sound Effects by:   Garry Sidelkivsky
                            Abinaash Sivasundar
                            Julien Schumacher
        Code Designed by:   Garry Sidelkivsky
        
        Better Code Designed by:    Garry Sidelkivsky
                                    Mr. Spittank
        Beta Tester:             Garry Sidelkivsky
                                 Hong-Duc Huynh
                                 Abinaash Sivasundar
                                 Julien Schumacher
        Special Thanks to:     YOU 
                    Thanks for playing my Game!!!
        
         """))
        print(animated_text(f"{name} will return...      (If I have some free time)"))
        input("Press Enter to leave this world")
        exit()
