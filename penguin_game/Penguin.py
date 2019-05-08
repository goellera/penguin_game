import pygame, sys
import time
import random

pygame.init()

# Variables
FPS = 30
WINDOW_SIZE = (1000, 700)
fps_clock = pygame.time.Clock()
penguin_x = 500
penguin_y = 350
img = pygame.image.load('assets/antarctica2.png')
img_x = 0
img_y = 0
stage = 1
my_font = pygame.font.Font('freesansbold.ttf',25)
peng_turn = "down"
orca_active = 0

# Colors
BLACK        = (0, 0, 0)
WHITE        = (255,255,255)
RED          = (0x800000)
GREEN        = (0x008000)
BLUE         = (0x000080)
LIGHT_YELLOW = (0xFFFF80)
ORANGE       = (0xFFA500)
DARK_BLUE    = (0x1E69FF)
ICE_BLUE     = (0xADD8E6)

# Set Up Window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('A Game')

# Penguin Drawing
penguin_size = 1
penguin_box = 0
penguinM_box = pygame.draw.rect(screen,BLACK,(-100,-100,1,1),1)
def draw_penguin(x,y):
	global penguin
	global penguin_box
	global penguinM_box
	if stage != 3:
		penguin_box = pygame.Rect(penguin_x - int(penguin_size * 50),penguin_y - int(penguin_size * 100),int(penguin_size * 100),int(penguin_size * 246))
		if peng_turn == "up":
			penguin = pygame.image.load('assets/3D_PenguinBack.png')
		elif peng_turn == "down":
			penguin = pygame.image.load('assets/3D_PenguinFront.png')
		elif peng_turn == "right":
			penguin = pygame.image.load('assets/3D_PenguinSideR.png')
		elif peng_turn == "left":
			penguin = pygame.image.load('assets/3D_PenguinSideL.png')
	
	if stage == 3:
		if peng_turn == "right":
			penguin = pygame.image.load('assets/3D_PenguinSideR.png')
			penguin = pygame.transform.rotate(penguin,270)
			penguin_box = pygame.Rect(penguin_x - int(penguin_size * 118),penguin_y - int(penguin_size * 25),int(penguin_size * 246),int(penguin_size * 100))
			penguinM_box = pygame.Rect(penguin_x - int(penguin_size * 53),penguin_y - int(penguin_size * 25),int(penguin_size * 100),int(penguin_size * 100))
		elif peng_turn == "left":
			penguin = pygame.image.load('assets/3D_PenguinSideL.png')
			penguin = pygame.transform.rotate(penguin,90)
			penguin_box = pygame.Rect(penguin_x - int(penguin_size * 127),penguin_y - int(penguin_size * 23),int(penguin_size * 246),int(penguin_size * 100))
			penguinM_box = pygame.Rect(penguin_x - int(penguin_size * 127),penguin_y - int(penguin_size * 23),int(penguin_size * 100),int(penguin_size * 100))
			
	penguin = pygame.transform.scale(penguin,(int(penguin_size * 267),int(penguin_size * 267)))
	screen.blit(penguin,(penguin_x - penguin_size * 133,penguin_y - penguin_size * 105))

# Fish Counter
def currency_B():
	screen.blit(pygame.image.load('assets/fishC.png'),(10,10))
	
# Game Loop
fish_y = random.randint(190,600)
fish_x = random.randint(1,2)
fish2_y = random.randint(190,600)
fish2_x = random.randint(1,2)
fish3_y = random.randint(190,600)
fish3_x = random.randint(1,2)
fish4_y = random.randint(190,600)
fish4_x = random.randint(1,2)
fish5_y = random.randint(190,600)
fish5_x = random.randint(1,2)
orca_x = -900
orca_y = random.randint(100,400)
currency_counter = int(0)
while True:
	# Adding Shapes
	#screen.fill(WHITE)
	screen.blit(img,(img_x,img_y))
	draw_penguin(penguin_x,penguin_y)
	# Currency
	text = my_font.render(str(currency_counter),True,BLACK)
	text_rect = text.get_rect()
	text_rect.center = (125,75)
	# Event Handlers
	
	# Controls
	keystate = pygame.key.get_pressed()
	if keystate[pygame.K_UP] or keystate[pygame.K_w]:
		if stage == 3:
			penguin_y -= 6
		else:
			penguin_y = penguin_y - 3
		peng_turn = "up"
	if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
		if stage == 3:
			penguin_y += 6
		else:
			penguin_y = penguin_y + 3
		peng_turn = "down"
	if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
		if stage == 3:
			penguin_x += 6
		else:
			penguin_x = penguin_x + 6
		peng_turn = "right"
	if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
		if stage == 3:
			penguin_x -= 6
		else:
			penguin_x = penguin_x - 6
		peng_turn = "left"

	# Sets borders and changes the scene if the penguin ventures in a certain direction
	# Stage 1
	if stage == 1:
		if penguin_x + int(penguin_size * 47) >= 1000:
			stage = 2
			img = pygame.image.load('assets/antarcticaS2.png')
			penguin_x = 200
		if penguin_x - int(penguin_size * 47) <= 0:
			penguin_x = penguin_x + 6
		if penguin_y - int(penguin_size * 98) <= 175:
			penguin_y = penguin_y + 3
		if penguin_y + int(penguin_size * 143) >= 700:
			penguin_y = penguin_y - 3
		penguin_size = penguin_y/350
		# Stage 2
	if stage == 2:
		if penguin_x + int(penguin_size * 47) >= 1000:
			penguin_x = penguin_x - 6
		if penguin_x - int(penguin_size * 47) <= 0:
			stage = 1
			img = pygame.image.load('assets/antarctica2.png')
			penguin_x = 900
			penguin_y = 350
		if penguin_y - int(penguin_size * 98) <= 275:
			penguin_y = penguin_y + 3
		if penguin_y + int(penguin_size * 143) >= 700:
			stage = 3
			img = pygame.image.load('assets/antarcticaO2.png')
			penguin_y = 100
			penguin_x = 600
		penguin_size = penguin_y/350 - .2
		# Stage 3
	if stage == 3:
		if penguin_x + int(penguin_size * 47) >= 945:
			penguin_x = penguin_x - 6
		if penguin_x - int(penguin_size * 47) <= 55:
			penguin_x = penguin_x + 6
		if penguin_y - int(penguin_size * 98) <= -50:
			stage = 2
			penguin = pygame.image.load('assets/3D_PenguinFront.png')
			img = pygame.image.load('assets/antarcticaS2.png')
			penguin_y = 500
		if penguin_y + int(penguin_size * 143) >= 750:
			penguin_y = penguin_y - 6
		penguin_size = 0.75
		
		# Spawns Orca
		orca_box = pygame.Rect(orca_x + 260,orca_y + 90,620,225)
		orca_box2 = pygame.Rect(orca_x + 60,orca_y + 150,200,155)
		screen.blit(pygame.image.load('assets/orca.png'),(orca_x,orca_y))
		
		# Remove Currency when Hit
		if penguin_box.colliderect(orca_box) or penguin_box.colliderect(orca_box2):
			currency_counter = currency_counter - 1
			if currency_counter <= 0:
				currency_counter = 0
		
		# Spawns Fish
		screen.blit(pygame.image.load('assets/fishS.png'),(fish_x,fish_y))
		screen.blit(pygame.image.load('assets/fishS.png'),(fish2_x,fish2_y))
		screen.blit(pygame.image.load('assets/fishS.png'),(fish3_x,fish3_y))
		screen.blit(pygame.image.load('assets/fishS.png'),(fish4_x,fish4_y))
		screen.blit(pygame.image.load('assets/fishS.png'),(fish5_x,fish5_y))
		
		# Add Currency and Resets Fish
		if penguinM_box.colliderect(fish_box):
			currency_counter = currency_counter + 1
			fish_y = random.randint(190,600)
			fish_x = -70
		if penguinM_box.colliderect(fish_box2):
			currency_counter = currency_counter + 1
			fish2_y = random.randint(190,600)
			fish2_x = -70
		if penguinM_box.colliderect(fish_box3):
			currency_counter = currency_counter + 1
			fish3_y = random.randint(190,600)
			fish3_x = -70
		if penguinM_box.colliderect(fish_box4):
			currency_counter = currency_counter + 1
			fish4_y = random.randint(190,600)
			fish4_x = -70
		if penguinM_box.colliderect(fish_box5):
			currency_counter = currency_counter + 1
			fish5_y = random.randint(190,600)
			fish5_x = -70
	# Allows fish to keep moving if stage != 3 to look cleaner
	fish_chance = random.randint(0,100)
	fish2_chance = random.randint(0,100)
	fish3_chance = random.randint(0,100)
	fish4_chance = random.randint(0,100)
	fish5_chance = random.randint(0,100)
	if fish_x >= 1000 and fish_chance == 75:
		fish_x = -70
		fish_y = random.randint(190,600)
	if fish2_x >= 1000 and fish2_chance == 75:
		fish2_x = -70
		fish2_y = random.randint(190,600)
	if fish3_x >= 1000 and fish3_chance == 75:
		fish3_x = -70
		fish3_y = random.randint(190,600)
	if fish4_x >= 1000 and fish4_chance == 75:
		fish4_x = -70
		fish4_y = random.randint(190,600)
	if fish5_x >= 1000 and fish5_chance == 75:
		fish5_x = -70
		fish5_y = random.randint(190,600)
	fish_box = pygame.Rect(fish_x,fish_y,61,35)
	fish_box2 = pygame.Rect(fish2_x,fish2_y,61,35)
	fish_box3 = pygame.Rect(fish3_x,fish3_y,61,35)
	fish_box4 = pygame.Rect(fish4_x,fish4_y,61,35)
	fish_box5 = pygame.Rect(fish5_x,fish5_y,61,35)
	fish_x = fish_x + 12
	fish2_x += 16
	fish3_x += 8
	fish4_x += 10
	fish5_x += 20
	
	# Allows Orca to spawn and move if stage != 3 to look cleaner
	if orca_active == 0:
		orca_chance = random.randint(0,450)
		orca_x = -900
		orca_y = random.randint(100,400)
		if orca_chance == 300:
			orca_active = 1
		
	if orca_active == 1:
		orca_x = orca_x + 8
		
	if orca_x >= 1000:
		orca_active = 0
		
	# Adds Currency Graphic and Text				
	currency_B()
	screen.blit(text,text_rect)
	
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			
	# Refresh the Screen
	pygame.display.update()
	fps_clock.tick(FPS)
'''
Ideas:
*Cave in area 3 leads to dungeon type area where it can be explored and is similar to sidescroller
*Area 1 will have house that can be build by buying sections with fish
*Left to area 1 will be a medieval penguin town
'''
