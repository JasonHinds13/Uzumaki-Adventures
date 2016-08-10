import pygame, sys, random, time
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock() #clock
FPS = 60 #Frames Per Second

#This class is for the main character which you control

class Hero(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('Data/NarutoSprites/narutoS.png').convert_alpha()

        self.rect = self.image.get_rect()

    def stats(self):

        self.health = vital

        self.chakra = power

        #Draw a health bar onto the screen

        pygame.draw.rect(screen, color, [20, 20,  self.health, 10])

        #Draw a bar to represent chakra

        pygame.draw.rect(screen, BLUE,[20, 40,  self.chakra, 10])

    def render(self):

        screen.blit(self.image, self.rect)

#This class defines the Jutsu/Moves the player can use

class Jutsu(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('Data/Effects/fireball.png').convert_alpha()

        self.rect = self.image.get_rect()

        self.bx = 0
        self.by = 0

#This class defines the enemies found in the game

class Enemy(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('Data/NarutoSprites/gaaraS.png').convert_alpha()

        self.rect = self.image.get_rect()

        self.health = Evital
        self.hcolor = Ecolor

        self.move = random.choice(NPCmov)

        self.xspeed = 0
        self.yspeed = 0

    def update(self):

        #This will draw a health bar above each enemy's head

        pygame.draw.rect(screen, self.hcolor, [(self.rect.x + 2), (self.rect.y - 2),  self.health, 6])

    def render(self):

        screen.blit(self.image, self.rect)

pygame.display.set_icon(pygame.image.load('Data/NarutoSprites/narutoS.png'))
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Uzumaki Adventures")

#font = pygame.font.Font("Data/Fonts/CALIBRI.ttf",25)
#font2 = pygame.font.Font("Data/Fonts/CALIBRI.ttf",21)

#Linux Font Issue
font = pygame.font.SysFont("CALIBRI.ttf",25)
font2 = pygame.font.SysFont("CALIBRI.ttf",21)

#This is an array to store the movements of the NPCs
NPCmov = ['MoveUp','MoveDown','MoveLeft','MoveRight', 'Stand']

#This is an array to store the different attacks of the player
attack = ['fireball', 'kunai', 'shuriken']
#Initialize as fireball
attack = 'fireball'

kunai = 30 #Amount of Kunai character has
shuriken = 30 #Amount of shuriken character has

xs = 0 #Player's x speed
ys = 0 #Player's y speed

score = 0

player = Hero()
bullet = Jutsu()

player.rect.x = 270 #100 #Player starting x position
player.rect.y = 300 #150 #Player starting y position

vital = 150 #Players Max Health
power = 150 #Players Max Chakra

Evital = 30 #Enemy's Max Health

RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

color = GREEN #Player's Health Bar Color
Ecolor = GREEN #Enemy's Health Bar Color

Edamage = 2 #Damage taken by enemies

#Player movements
up = False
down = True
right = False
left = False

loading = True #This is for the loading screen
welcome = False #This is for the welcome screen
running = False #This is for the actual game

second = 0 #This will be used to manage time

enemies = pygame.sprite.Group() #Sprite group for enemies
bullets = pygame.sprite.Group() #Sprite group for jutsu/bullets
AllSprites = pygame.sprite.Group() #Sprite group for all sprites available

bad = Enemy()

seconds = 0

#To define the current background when the game starts
background = pygame.image.load('Data/TerrainData/grass2.png').convert_alpha()
backrect = background.get_rect()

#These are variables for the starting screen
bkg = pygame.image.load('Data/Effects/NarutoBkg.png').convert_alpha()
bkgrect = bkg.get_rect()

#This is for the loading screen
bkg2 = pygame.image.load('Data/Effects/NaruBkg.jpg').convert_alpha()
bk2rect = bkg2.get_rect()

#summoning pad
summonpad = pygame.image.load('Data/TerrainData/summon2.png').convert_alpha()

#This is for music
sound = pygame.mixer.Sound('Data/Sounds/Opening.ogg')
kunai_sound = pygame.mixer.Sound('Data/Sounds/kunai.ogg')
fireball_sound = pygame.mixer.Sound('Data/Sounds/Fireball.ogg')
shuriken_sound = pygame.mixer.Sound('Data/Sounds/shuriken.ogg')

#Variables for the selection circle at the starting screen
circlex = 140
circley = 20
cy = 20

#NPC Movement Variables
bad.move = random.choice(NPCmov)

#For different moves selection
wepselect = pygame.image.load('Data/Effects/weapons.png').convert_alpha()

fullscreen = False
instructions = False

#Loading Screen
while loading == True:

    screen.blit(bkg2, bk2rect)
    screen.blit(font.render(str('Loading Game...'), True,(0,0,0)), (50,350))
    pygame.display.flip()

    sound.play()
    sound.fadeout(11000)
    time.sleep(7)

    loading = False
    welcome = True

#Starting Screen
while welcome == True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit(1)

        if event.type == pygame.KEYDOWN:

            if event.key == K_ESCAPE:
                sys.exit(1)

            if event.key == K_DOWN:

                if circley == 20:
                    cy = 50
                if circley == 50:
                    cy = 80
                if circley == 80:
                    cy = 110
                if circley == 110:
                    cy = 20

            if event.key == K_UP:

                if circley == 20:
                    cy = 110
                if circley == 50:
                    cy = 20
                if circley == 80:
                    cy = 50
                if circley == 110:
                    cy = 80

            if event.key == K_RETURN:

                if circley == 20:
                    welcome = False
                    running = True

                if circley == 50 and instructions == False:
                    instructions = True

                elif circley == 50 and instructions == True:
                    instructions = False

                if circley == 80 and fullscreen == False:
                    screen = pygame.display.set_mode((600, 400),pygame.FULLSCREEN)
                    fullscreen = True

                elif circley == 80 and fullscreen == True:
                    screen = pygame.display.set_mode((600, 400))
                    fullscreen = False

                if circley == 110:
                    sys.exit(1)

            if event.key == ord('e'):
                screen = pygame.display.set_mode((600, 400))
                fullscreen = False


    circley = cy

    screen.blit(bkg, bkgrect)
    screen.blit(font.render(str('Start Game'), True,(WHITE)), (10,10))
    screen.blit(font.render(str('Controls'), True,(WHITE)), (10,40))
    screen.blit(font.render(str('FullScreen'), True,(WHITE)), (10,70))
    screen.blit(font.render(str('Exit Game'), True,(WHITE)), (10,100))
    pygame.draw.circle(screen, RED, (circlex, circley), 10, 5)

    if fullscreen == True:
        screen.blit(font.render(str("Press 'Q/E' To Toggle FullScreen On/Off Respectively"), True,(255,255,255)), (10,370))

    if instructions == True:
        screen.blit(font2.render(str('Use Arrows To Move'), True,(BLACK)), (10,140))
        screen.blit(font2.render(str('Press G To Summon Enemies'), True,(BLACK)), (10,161))
        screen.blit(font2.render(str('Press F or Spacebar To Attack'), True,(BLACK)), (10,182))
        screen.blit(font2.render(str('Press Numbers 1-3 To Change Attacks'), True,(BLACK)), (10,203))
        screen.blit(font2.render(str('Press Q/E To Change Fullscreen'), True,(BLACK)), (10,224))

    pygame.display.flip()

#Actual Game
while running == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(1)

        if event.type == pygame.KEYDOWN:

            if event.key == ord('e'):
                screen = pygame.display.set_mode((600, 400))

            if event.key == ord('q'):
                screen = pygame.display.set_mode((600, 400),pygame.FULLSCREEN)

            if event.key == K_ESCAPE:
                sys.exit(1)

            if event.key == ord('f') or event.key == K_SPACE:

                if attack == 'fireball' and power > 0:

                    bullet = Jutsu()

                    bullet.rect.x = player.rect.x
                    bullet.rect.y = player.rect.y

                    fireball_sound.play()

                    if up == True:
                        bullet.image = pygame.image.load('Data/Effects/fireballup.png').convert_alpha()
                        bullet.by = -5
                        bullet.bx = 0
                    if down == True:
                        bullet.image = pygame.image.load('Data/Effects/fireballdown.png').convert_alpha()
                        bullet.by = 5
                        bullet.bx = 0
                    if left == True:
                        bullet.image = pygame.image.load('Data/Effects/fireballleft.png').convert_alpha()
                        bullet.bx = -5
                        bullet.by = 0
                    if right == True:
                        bullet.image = pygame.image.load('Data/Effects/fireball.png').convert_alpha()
                        bullet.bx = 5
                        bullet.by = 0

                    power -= 5

                if attack == 'kunai' and kunai > 0:
                    bullet = Jutsu()

                    bullet.rect.x = player.rect.x
                    bullet.rect.y = player.rect.y

                    kunai = kunai - 1

                    kunai_sound.play()

                    if up == True:
                        bullet.image = pygame.image.load('Data/Effects/KunaiUp.png').convert_alpha()
                        bullet.by = -5
                        bullet.bx = 0
                    if down == True:
                        bullet.image = pygame.image.load('Data/Effects/KunaiDown.png').convert_alpha()
                        bullet.by = 5
                        bullet.bx = 0
                    if left == True:
                        bullet.image = pygame.image.load('Data/Effects/KunaiLeft.png').convert_alpha()
                        bullet.bx = -5
                        bullet.by = 0
                    if right == True:
                        bullet.image = pygame.image.load('Data/Effects/KunaiRight.png').convert_alpha()
                        bullet.bx = 5
                        bullet.by = 0

                if attack == 'shuriken' and shuriken > 0:
                    bullet = Jutsu()

                    bullet.rect.x = player.rect.x
                    bullet.rect.y = player.rect.y

                    shuriken = shuriken - 1

                    shuriken_sound.play()

                    if up == True:
                        bullet.image = pygame.image.load('Data/Effects/shuriken.png').convert_alpha()
                        bullet.by = -5
                        bullet.bx = 0
                    if down == True:
                        bullet.image = pygame.image.load('Data/Effects/shuriken.png').convert_alpha()
                        bullet.by = 5
                        bullet.bx = 0
                    if left == True:
                        bullet.image = pygame.image.load('Data/Effects/shuriken.png').convert_alpha()
                        bullet.bx = -5
                        bullet.by = 0
                    if right == True:
                        bullet.image = pygame.image.load('Data/Effects/shuriken.png').convert_alpha()
                        bullet.bx = 5
                        bullet.by = 0

                bullets.add(bullet)
                AllSprites.add(bullet)

            if event.key == ord('1'):
                attack = 'fireball'
            if event.key == ord('2'):
                attack = 'kunai'
            if event.key == ord('3'):
                attack = 'shuriken'

            if event.key == ord('g'):
                bad = Enemy()

                bad.rect.x = 270 #random.randrange(0, 500)
                bad.rect.y = 70 #random.randrange(100, 300)

                enemies.add(bad)
                AllSprites.add(bad)

            if event.key == K_DOWN:
                down = True
                up = False
                right = False
                left = False
                player.image = pygame.image.load('Data/NarutoSprites/narutoM.png').convert_alpha()
                ys = 3

            if event.key == K_UP:
                up = True
                down = False
                right = False
                left = False
                player.image = pygame.image.load('Data/NarutoSprites/narutobackM.png').convert_alpha()
                ys = -3

            if event.key == K_LEFT:
                left = True
                right = False
                up = False
                down = False
                player.image = pygame.image.load('Data/NarutoSprites/narutoleftM.png').convert_alpha()
                xs = -3

            if event.key == K_RIGHT:
                right = True
                left = False
                down = False
                up = False
                player.image = pygame.image.load('Data/NarutoSprites/narutorightM.png').convert_alpha()
                xs = 3

        if event.type == pygame.KEYUP:

            if event.key == K_DOWN:
                player.image = pygame.image.load('Data/NarutoSprites/narutoS.png').convert_alpha()
                ys = 0

            if event.key == K_UP:
                player.image = pygame.image.load('Data/NarutoSprites/narutobackS.png').convert_alpha()
                ys = 0

            if event.key == K_LEFT:
                player.image = pygame.image.load('Data/NarutoSprites/narutoleftS.png').convert_alpha()
                xs = 0

            if event.key == K_RIGHT:
                player.image = pygame.image.load('Data/NarutoSprites/narutorightS.png').convert_alpha()
                xs = 0

    AllSprites.update()

    for bullet in bullets:

        hit = pygame.sprite.spritecollide(bullet, enemies, False)

        #Controls The Bullet's Movements

        bullet.rect.x += bullet.bx
        bullet.rect.y += bullet.by

        for bad in hit:
            score += 1
            bad.health -= 10
            bullets.remove(bullet)

        if bad.health <= 10:
            bad.hcolor = RED

        if bad.health <= 0:
            enemies.remove(bad)

        if bullet.rect.x > 600:
            bullets.remove(bullet)
        if bullet.rect.y > 400:
            bullets.remove(bullet)
        if bullet.rect.x < 0:
            bullets.remove(bullet)
        if bullet.rect.y < 0:
            bullets.remove(bullet)

    for bad in enemies:

        #Control's The NPC's Movements

        bad.rect.x += bad.xspeed
        bad.rect.y += bad.yspeed

        if pygame.sprite.spritecollide(player, enemies, False):
            vital -= 10

        if bad.move == 'MoveUp':
            if bad.rect.y > random.randint(10, 200):
                bad.image = pygame.image.load('Data/NarutoSprites/gaarabackM.png').convert_alpha()
                bad.xspeed = 0
                bad.yspeed = random.randrange(-3, -2)
            else:
                bad.move = random.choice(NPCmov)

        if bad.move == 'MoveDown':
            if bad.rect.y < random.randint(200, 390):
                bad.image = pygame.image.load('Data/NarutoSprites/gaaraM.png').convert_alpha()
                bad.xspeed = 0
                bad.yspeed = random.randrange(2, 3)
            else:
                bad.move = random.choice(NPCmov)

        if bad.move == 'MoveLeft':
            if bad.rect.x > random.randint(10, 300):
                bad.image = pygame.image.load('Data/NarutoSprites/gaaraleftM.png').convert_alpha()
                bad.xspeed = random.randrange(-3, -2)
                bad.yspeed = 0
            else:
                bad.move = random.choice(NPCmov)

        if bad.move == 'MoveRight':
            if bad.rect.x < random.randint(300, 590):
                bad.image = pygame.image.load('Data/NarutoSprites/gaararightM.png').convert_alpha()
                bad.xspeed = random.randrange(2, 3)
                bad.yspeed = 0
            else:
                bad.move = random.choice(NPCmov)

        if bad.move == 'Stand':
            bad.image = pygame.image.load('Data/NarutoSprites/gaaraS.png').convert_alpha()
            bad.xspeed = 0
            bad.yspeed = 0
            bad.move = random.choice(NPCmov)

    #Controls The Player's Movements

    player.rect.x += xs
    player.rect.y += ys

    #This Manages Time

    second += 1

    if second >= 100:
        if vital < 150:
            vital += 7
        if power < 150:
            power += 5
        second = 0

    #This manages both player and enemy health

    if vital < 50:
        color = RED

    if vital > 50:
        color = GREEN

    if vital < 0:
        vital = 0

    if vital > 150:
        vital = 150

    if power < 0:
        power = 0

    if power > 150:
        power = 150

    screen.blit(background, backrect)

    screen.blit(summonpad, (250, 50))

    enemies.draw(screen)
    bullets.draw(screen)

    enemies.update()

    player.render()
    player.stats()

    screen.blit(wepselect, (452, 0))

    screen.blit(font.render(str(kunai), True,(255,255,255)), (515,29))
    screen.blit(font.render(str(shuriken), True,(255,255,255)), (565,29))

    screen.blit(font.render(str("Score: %d" %score), True,(255,255,255)), (20,60))

    if attack == 'fireball':
        pygame.draw.rect(screen,RED, (452, 0, 56, 30), 3)
    if attack == 'kunai':
        pygame.draw.rect(screen,RED, (508, 0, 50, 30), 3)
    if attack == 'shuriken':
        pygame.draw.rect(screen,RED, (558, 0, 42, 30), 3)

    screen.blit(font.render(str("Target Practice - Press To 'G' Summon Enemies"), True,(255,255,255)), (10,370))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
quit()
