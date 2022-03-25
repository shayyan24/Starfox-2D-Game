# Shayyan Husein
# January 10, 2022
# Unit 3 Summative Task - Pygame
import easygui
import pygame
import time
pygame.init()

print("\nMake sure you extend the GUI window to make \nsure the entire program screen width and height is visible")

# Defining Screen Size and Caption
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Starfox 2D - Journey to the Landmaster | Shayyan Husein")

# ---- Creating Sprites -----

# Creating Sprite for main character named Fox
fox = pygame.sprite.Sprite()
fox.image = pygame.image.load("images/fox_w.png").convert_alpha()
fox.rect = fox.image.get_rect()
fox.rect.topleft = (-100,-100,)
# screen.blit(fox.image, fox.rect)

# Creating Sprite for main villian named Wolf
wolf = pygame.sprite.Sprite()
wolf.image = pygame.image.load("images/wolf.png")
wolf.rect = wolf.image.get_rect()
wolf.rect.topleft = (-100,-100,)
wolf_hp = 10
# screen.blit(wolf.image, wolf.rect)


# Creating a stationary image of fox for introduction page or dialog scenes
fox_stationary = pygame.sprite.Sprite()
fox_stationary.image = pygame.image.load("images/fox_oc.png")
fox_stationary.rect = fox_stationary.image.get_rect()
fox_stationary.rect.topleft = (480, 260)

# Creating a stationary image of airship for introduction page or dialog scenes
airship_stationary = pygame.sprite.Sprite()
airship_stationary.image = pygame.image.load("images/arwing.png")
airship_stationary.rect = airship_stationary.image.get_rect()
airship_stationary.rect.topleft = (630, 120)

# Creating Sprite for Fox's Airship
airship = pygame.sprite.Sprite()
airship.image = pygame.image.load("images/arwing.png")
airship.rect = airship.image.get_rect()
airship.rect.topleft = (-100, -180)
# screen.blit(airship.image, airship.rect)

# Creating Sprite for Enemy
enemy = pygame.sprite.Sprite()
enemy.image = pygame.image.load("images/enemy_land.png")
enemy.rect = enemy.image.get_rect()
enemy.rect.topleft = (-350, -180)
# screen.blit(enemy.image, enemy.rect)

# Creating Sprite for Obstacle
obstacle = pygame.sprite.Sprite()
obstacle.image = pygame.image.load("images/obstacle.png")
obstacle.rect = obstacle.image.get_rect()
obstacle.rect.topleft = (-350, -180)
# screen.blit(obstacle.image, obstacle.rect)

# Creating Heart Sprite for Lives Counter
heart = pygame.sprite.Sprite()
heart.image = pygame.image.load("images/heart.png")

# Creating Sprite for the boundary (left) wall
wall = pygame.sprite.Sprite()
wall.image = pygame.image.load("images/wall.png")
wall.rect = wall.image.get_rect()
wall.rect.topleft = (-10, 0)
# screen.blit(wall.image, wall.rect)

# Defining top wall boundary for final level
top_wall = pygame.sprite.Sprite()
top_wall.image = pygame.image.load("images/health_point.png")
top_wall.rect = top_wall.image.get_rect()
top_wall.rect.topleft = (45, 0)

# Defining bottom wall boundary for final level
bottom_wall = pygame.sprite.Sprite()
bottom_wall.image = pygame.image.load("images/health_point.png")
bottom_wall.rect = bottom_wall.image.get_rect()
bottom_wall.rect.topleft = (45, 400)

# Creating Sprite for the map advancing wall (right side)
advance_wall = pygame.sprite.Sprite()
advance_wall.image = pygame.image.load("images/wall.png")
advance_wall.rect = wall.image.get_rect()
advance_wall.rect.topleft = (800, 0)
# screen.blit(wall.image, wall.rect)

# Creating Sprite for Coin 1
coin1 = pygame.sprite.Sprite()
coin1.image = pygame.image.load("images/coin.png")
coin1.rect = coin1.image.get_rect()
coin1.rect.topleft = (-675, 10)
# screen.blit(coin1.image, coin1.rect)
coin1_taken = False

# Creating Sprite for Coin 2
coin2 = pygame.sprite.Sprite()
coin2.image = pygame.image.load("images/coin.png")
coin2.rect = coin2.image.get_rect()
coin2.rect.topleft = (-675, 10)
# screen.blit(coin2.image, coin2.rect)
coin2_taken = False

# Creating Sprite for Coin 3
coin3 = pygame.sprite.Sprite()
coin3.image = pygame.image.load("images/coin.png")
coin3.rect = coin3.image.get_rect()
coin3.rect.topleft = (-675, 10)
# screen.blit(coin3.image, coin3.rect)
coin3_taken = False

# Creating Sprite for Mega Coin
mega_coin = pygame.sprite.Sprite()
mega_coin.image = pygame.image.load("images/mega_coin.png")
mega_coin.rect = mega_coin.image.get_rect()
mega_coin.rect.topleft = (-2000,-200)
# screen.blit(mega_coin.image, mega_coin.rect)
mega_coin_taken = False

# Creating Sprite for laser
laser = pygame.sprite.Sprite()
laser.image = pygame.image.load("images/laser.png")
laser.rect = laser.image.get_rect()
laser.rect.topleft = (-150, -150)
# screen.blit(laser.image, laser.rect)

# Creating Sprite for rope
rope = pygame.sprite.Sprite()
rope.image = pygame.image.load("images/rope.png")
rope.rect = rope.image.get_rect()
rope.rect.topleft = (670, 115)
# screen.blit(rope.image, rope.rect)

# Creating Sprite for platform
platform = pygame.sprite.Sprite()
platform.image = pygame.image.load("images/platform.png")
platform.rect = platform.image.get_rect()
platform.rect.topleft = (510, 110)
# screen.blit(platform.image, platform.rect)

# Creating Sprite for door (locked secret door)
door = pygame.sprite.Sprite()
door.image = pygame.image.load("images/door.png")
door.rect = door.image.get_rect()
door.rect.topleft = (2000, 200)
# screen.blit(door.image, door.rect)

# Creating Sprite for castle
castle = pygame.sprite.Sprite()
castle.image = pygame.image.load("images/castle.png")
castle.rect = castle.image.get_rect()
castle.rect.topleft = (700, 95)
# screen.blit(castle.image, castle.rect)

# Creating Sprite for target
target = pygame.sprite.Sprite()
target.image = pygame.image.load("images/target.png")
target.rect = target.image.get_rect()
target.rect.topleft = (2000,800)
# screen.blit(target.image, target.rect)

# Creating Sprite for key
key = pygame.sprite.Sprite()
key.image = pygame.image.load("images/key.png")
key.rect = key.image.get_rect()
key.rect.topleft = (2000,800)
# screen.blit(key.image, key.rect)

# Creating Sprite for fireball 1
fireball1 = pygame.sprite.Sprite()
fireball1.image = pygame.image.load("images/fireball.png")
fireball1.rect = fireball1.image.get_rect()
fireball1.rect.topleft = (-1000, -500)
# screen.blit(fireball1.image, fireball1.rect)

# Creating Sprite for fireball 2
fireball2 = pygame.sprite.Sprite()
fireball2.image = pygame.image.load("images/fireball.png")
fireball2.rect = fireball2.image.get_rect()
fireball2.rect.topleft = (-1000, -500)
# screen.blit(fireball2.image, fireball2.rect)

# Creating Sprite for fireball 3
fireball3 = pygame.sprite.Sprite()
fireball3.image = pygame.image.load("images/fireball.png")
fireball3.rect = fireball3.image.get_rect()
fireball3.rect.topleft = (-1000, -500)
# screen.blit(fireball3.image, fireball3.rect)

# Creating Sprite for stop sign
stop_sign = pygame.sprite.Sprite()
stop_sign.image = pygame.image.load("images/stop_sign.png")
stop_sign.rect = stop_sign.image.get_rect()
stop_sign.rect.topleft = (2000,800)

# Creating wolf health bar Sprite for Lives Counter
wolf_health_point = pygame.sprite.Sprite()
wolf_health_point.image = pygame.image.load("images/health_point.png")

# ----- Creating / Defining Variables -----

#  Defining Colour Variables
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 180, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
bg_colour = (51, 153, 255)  # background colour
bridge = (102, 51, 0)
grey = (160,160,160)

# Defining variables
begin = False
restart = False
map_change = 0
x = 25
y = 280
starting_x = 25
starting_y = 280
x_move = 0
y_move = 0
airship_x = 0
airship_y = 0
wolf_x = 600
wolf_y = 110
wolf_y_move = 1
enter_ship = False
gravity_true = True
enemy_alive = True
lives = 3
laser_shot = False
coins = 0
interact = False
left = 0
laser_x = x
laser_y = y
laser_velocity = 0
laser_vel_multiply = 1
ongoing_laser = False
if_laser = 0
fox_ground_y = 280
enemy_x = 460
enemy_y = 290
enemy_jump_loop = 0
enemy_jumping_up = True
enemy_hop = 0
direction = 1
laser_hit = False
slow_down = 0
secret_map = False
airship_stage_prep = False 
wolf_hit = False
wolf_hp = 10
obstacle_alive = True
obstacle_y = 800
obstacle_x = 600
obstacle_hit = False
obstacle_velocity = -1
continue_scene = True
during_scene = False
skip_scene = False
selection_stage = False
power_up = ("")
fireball1_y = 360
fireball2_y = 200
fireball3_y = 120
fireball1_y_move = -3
fireball2_y_move = -3
fireball3_y_move = -3
upwards1 = True
upwards2 = True
upwards3 = True
fireball_true = True
target_hit = False


# Creating string, font and text variables
title = ("Starfox 2D - Journey to the Landmaster")
font = pygame.font.SysFont("dejavusansmono", 20)
introFont = pygame.font.Font("fonts/Seaside.ttf", 35)  #pygame.font.Font("fonts/sea.ttf", 35) 
introFont2 = pygame.font.Font("fonts/Lobster.otf", 35) #pygame.font.Font("fonts/lob.otf", 35)
introText = introFont.render("STARFOX 2D", True, red)
introText2 = introFont2.render("Journey to the Landmaster!", True, red)
inst1 = font.render("Left        Right        Interact               Shoot Laser", True, black)
inst2 = font.render("<- or A     D or ->    Up Arrow / W                Space",True, white)
inst3 = font.render("  Press Tab to Begin  ", True, red, black)
inst4 = font.render("  Controls  ", True, white, black)
intro_stage = font.render("Collect Coins     Shoot Enemies (uses 1 coin)      ", True, black)
intro_stage1 = font.render("Climb ropes using Up Arrow or \"W\"", True, black)
go_text = font.render("Advance to the next level ", True, white)
go_text1 = font.render("by walking all the way right", True, white)
stage1_text = font.render("Watch out for Flying Enemies!", True, black)
stage1_text1 = font.render("If you get hit,", True, black)
stage1_text2 = font.render("you lose 1 heart and 1 coin!", True, black)
stage2_text = font.render("You might need to save your coins,", True, black)
stage2_text1 = font.render("so shoot your lasers wisely!", True, black)
stage4_text = font.render("This door can only be entered", True, black)
stage4_text1 = font.render("if you have 7 coins", True, black)
stage4_text2 = font.render("Press Interact button (W / Up Arrow)", True, red)
secret_stage_text = font.render("Nice job evading those enemies!", True, black)
secret_stage_text1 = font.render("Here is a MEGA coin!", True, red)
secret_stage_text2 = font.render("MEGA coins give you +10 coins!", True, white)
stage5_text = font.render("When in Airship, Shoot Wolf and his obstacles!", True, black)
stage5_text1 = font.render("Control Change Effective in airstage:", True, black)
stage5_text2 = font.render("W / Up Arrow - Move Up", True, black)
stage5_text3 = font.render("S / Down Arrow - Move Down", True, black)
stage5_text4 = font.render("Space Bar - Shoot Laser", True, black)
stage6_text = font.render("Looks like you have to climb the rope...", True, black)
stage6_text1 = font.render("Enter the castle and retrieve the key!", True, black)
stage7_text = font.render("Shoot the target to obtain the key...", True, white)
stage7_text1 = font.render("Make sure your lasers avoid the lava!", True, white)
airship_instruction = font.render("Shooting Obstacles will give you more coins!", True, red)
username = ("")
username_text = font.render(username, True, white)
wolf_name_text = font.render("Wolf O\'Donnell", True, white)
defeated_text = font.render("Wolf O\'Donnell is defeated!", True, red)
game_over_text = introFont.render("Game Over!", True, red)
game_over_text2 = introFont2.render("Better luck next time!", True, red)
game_won_text = introFont.render("HOORAY!", True, red)
game_won_text1 = introFont2.render("You defeated Wolf!", True, red)

#  ----- Defining Functions -------


# Defining Wall Sprite functions to display
def wall_display():
  wall.rect.topleft = (-10, 0)
  screen.blit(wall.image, wall.rect)
  advance_wall.rect.topleft = (800, 0)
  screen.blit(advance_wall.image, advance_wall.rect)

# Defining wall display for final boss level

def final_wall_display():
  top_wall.rect.topleft = 45, 0
  screen.blit(top_wall.image, top_wall.rect)
  bottom_wall.rect.topleft = 45, 390
  screen.blit(top_wall.image, bottom_wall.rect)


# Defining Background Scene
def background():
  screen.fill(bg_colour)
  # screen.blit(grass.image, grass.rect)
  pygame.draw.rect(screen, green, (0, 350, 800, 500))


#  Defining background of castle
def castle_bg():
  screen.fill((54, 52, 51))
  pygame.draw.rect(screen,grey, (0,213,620, 10))
  pygame.draw.rect(screen, bridge, (0, 213,220,20))
  pygame.draw.rect(screen, bridge, (30, 233,160,13))
  pygame.draw.rect(screen, bridge, (580, 213,220,20))
  pygame.draw.rect(screen, bridge, (610, 233,160,13))

# Defining Lava Floor 
def lava():
  pygame.draw.rect(screen, red, (0, 350, 800, 500))
  for i in range(15):  # Creating Lava triangles along floor 
    pygame.draw.polygon(screen,red,[(i*50, 350), (50+i*50, 325), (100+i*50, 350)])

# Defining Display function for character Fox
def fox_display():
  fox.rect.topleft = (x, y)
  screen.blit(fox.image, fox.rect)

# Defining Display and movement function for character Wolf
def wolf_display():
  global wolf_y
  global wolf_y_move
  global wolf_x
  global wolf_hit
  wolf.rect.topleft = (wolf_x, wolf_y)
  if wolf_hit:
    wolf.image = pygame.image.load("images/wolf-1.png")
  else:
    wolf.image = pygame.image.load("images/wolf.png")
  screen.blit(wolf.image, wolf.rect)
  wolf_y += wolf_y_move
  wolf_hit = False

  # if wolf reaches edges of screen, make him move in the opposite direction
  if (wolf_y > 292): 
    wolf_y_move = (wolf_y_move) * -1
  elif (wolf_y < 0):
    wolf_y_move = wolf_y_move * -1

# Defining Display function for airship (arwing)
def airship_display():
  airship.rect.topleft = (airship_x, airship_y)
  screen.blit(airship.image, airship.rect)

# Defining Lives and Heart counter Display
def heart_display():
  for i in range(lives):
    screen.blit(heart.image, (i * 35 + 5, 25))
  screen.blit(username_text, (3, 5))

# Defining Wolf Health Bar Display
def wolf_hp_display():
  if (wolf_hp > 0):
    screen.blit(wolf_name_text, (300, 5))
    pygame.draw.rect(screen, black, (270, 28, 228, 13))
  else:
    screen.blit(defeated_text,(240,5))
  for i in range(wolf_hp):
    screen.blit(wolf_health_point.image, ((i//2) * 45 + 274, 31))

# Defining Coins Counter
def coin_display():
  pygame.draw.circle(screen, black, (689, 22), 13)
  pygame.draw.circle(screen, yellow, (689, 22), 11)
  coin_txt = font.render(("x " + str(coins)), True, white)
  screen.blit(coin_txt, (710, 10))

# Defining display and movement function for obstacles
def obstacle_movement():
  global wolf_y
  global obstacle_x
  global obstacle_y
  global obstacle_velocity
  global obstacle_alive
  global ongoing_laser
  global obstacle_hit
  obstacle_velocity = -1
  if obstacle_alive == True:
      obstacle_x += obstacle_velocity
      obstacle.rect.topleft = (obstacle_x, (obstacle_y))
      screen.blit(obstacle.image, obstacle.rect)
  if (obstacle_x < 0) or obstacle_hit or not obstacle_alive:
    obstacle_y = wolf_y + 50
    obstacle_x = wolf_x 
    obstacle_alive = True
    obstacle_hit = False



# Defining enemy movement
def enemy_movement():
  global enemy_x
  global enemy_y
  global enemy_alive
  global enemy_jump_loop
  global enemy_jumping_up
  global enemy_hop
  global direction
  global slow_down

  if enemy_alive:
      if (slow_down % 3 == 0):  # Making code loop every 1 out of 3 times it is ran, slows down enemy speed without using time.sleep commands because that slows entire program down heavily
        if (enemy_jumping_up):
          enemy_x += -1 * (direction)
          enemy_y += -2
          enemy_jump_loop += 1
          if enemy_jump_loop == 30:
              enemy_jumping_up = False
        else:
          enemy_x += -1 * (direction)
          enemy_y += 2
          enemy_jump_loop -= 1
          if enemy_jump_loop == 0:
              enemy_jumping_up = True
              enemy_hop += 1
              if (enemy_hop %2 == 0):  #runs every twice hop, then turns around
                direction = direction * -1  #direction turns the negative of what it previously was
      slow_down += 1  # Increments by 1, so when it can reach the multiple of 3 to allow the movement code to run again
  else:
    slow_down = 0
    direction = 1

# Defining Fireball1 movement

def fireball1_movement():
  global fireball1_y
  global fireball1_y_move
  global upwards1
  # If fireball1 reaches bottom edge, make it go back up
  if (fireball1_y > 400): 
    fireball1_y_move = (fireball1_y_move) * -1
    upwards1 = True  # keeps track of which direction fireball is going
  elif (fireball1_y < 35):
    fireball1_y_move = fireball1_y_move * -1
    upwards1 = False  # keeps track of which direction fireball is going

  fireball1_y += fireball1_y_move 
  fireball1.rect.topleft = (230, fireball1_y)
  screen.blit(fireball1.image,fireball1.rect)


# Defining fireball2 movement
def fireball2_movement():
  global fireball2_y
  global fireball2_y_move
  global upwards2
  # If fireball2 reaches bottom edge, make it go back up
  if (fireball2_y > 400): 
    fireball2_y_move = (fireball2_y_move) * -1
    upwards2 = True  # keeps track of which direction fireball is going
  elif (fireball2_y < 35):
    fireball2_y_move = fireball2_y_move * -1
    upwards2 = False  # keeps track of which direction fireball is going

  fireball2_y += fireball2_y_move 
  fireball2.rect.topleft = (350, fireball2_y)
  screen.blit(fireball2.image,fireball2.rect)


# Defining fireball3 movement
def fireball3_movement():
  global fireball3_y
  global fireball3_y_move
  global upwards3
  # If fireball3 reaches bottom edge, make it go back up
  if (fireball3_y > 400): 
    fireball3_y_move = (fireball3_y_move) * -1
    upwards3 = True  # keeps track of which direction fireball is going
  elif (fireball3_y < 35):
    fireball3_y_move = fireball3_y_move * -1
    upwards3 = False  # keeps track of which direction fireball is going

  fireball3_y += fireball3_y_move 
  fireball3.rect.topleft = (480, fireball3_y)
  screen.blit(fireball3.image,fireball3.rect)




# Defining Laser shoot
def laser_shoot():
  global x
  global laser_x
  global laser_y
  global y
  global laser_shot
  global ongoing_laser
  global laser_hit
  if laser_shot == True:
      laser_x += laser_velocity
      laser.rect.topleft = (laser_x, (laser_y + 35))
      screen.blit(laser.image, laser.rect)
      ongoing_laser = True
  if (laser_x > 800) or (laser_x < 0) or laser_hit:
      laser_shot = 0
      ongoing_laser = False
      laser_hit = False


# Defining Intro Scene for when game starts
def intro():
  screen.fill(bg_colour)
  # screen.blit(grass.image, grass.rect)
  pygame.draw.rect(screen, green, (0, 350, 800, 500))
  pygame.draw.rect(screen, yellow, (180, 30, 400, 150))
  screen.blit(introText, (265, 55))
  screen.blit(introText2, (210, 105))
  screen.blit(inst1, (40, 310))
  screen.blit(inst2, (30, 275))
  screen.blit(inst3, (260, 210))
  screen.blit(inst4, (308, 355))
  screen.blit(fox_stationary.image, fox_stationary.rect)
  screen.blit(airship.image, airship_stationary.rect)

# Defining airship stage background function
def airstage():
  screen.fill((0, 21, 61))

# Defining Gravity function
def gravity():
  global gravity_true
  global y_move
  global fox_ground_y
  if gravity_true:
    if ( y < fox_ground_y):  #  bring fox down to level (if not already on ground)
        y_move = 2
    else:
        y_move = 0

done = False  # Loops until user closes program
clock = pygame.time.Clock()  # FPS counter
# -------- Main Program Loop -----------
while (not done):
  if not begin:  # While in intro screen (game has not begun)
    if not username:  # Get username of player
      intro()
      pygame.display.update()
      time.sleep(0.5)
      username = ("I" * 21)  # Initializing over 20 Characters, loops username code
      while (username is None) or ((len(username)) > 20):
        username = easygui.enterbox("What is your username?  (Maximum 20 Characters) \n(Stop and Run program if Text box does not allow you to type)",title)
        username_text = font.render(username, True, white)
    else:  # when username has a value , refresh screen with intro/instructions page
      intro()
      screen.blit(username_text, (3, 5))
  elif (map_change == 0):  # When game begins on map number 0 (beginning stage)
    fox_ground_y = 280
    starting_x = 25
    starting_y = 280
    background()
    screen.blit(intro_stage, (40, 210))
    screen.blit(go_text, (40, 110))
    screen.blit(go_text1, (40, 140))
    screen.blit(intro_stage1, (200, 60))
    wall_display()
    laser_shoot()
    screen.blit(rope.image, rope.rect)
    screen.blit(platform.image, platform.rect)
    fox_display()
    x = x + x_move
    y = y + y_move
    if not coin1_taken:    # Displays coin1 until collided with
        coin1.rect.topleft = (150, 300)
        screen.blit(coin1.image, coin1.rect)
    if not coin2_taken:    # Displays coin2 until collided with
        coin2.rect.topleft = (200, 300)
        screen.blit(coin2.image, coin2.rect)
    if not coin3_taken:    # Displays coin3 until collided with
        coin3.rect.topleft = (250, 300)
        screen.blit(coin3.image, coin3.rect)
    if enemy_alive:    # Allows enemy to move if not killed
        enemy_movement()
        enemy.rect.topleft = (enemy_x, enemy_y)
        screen.blit(enemy.image, enemy.rect)

    heart_display()
    coin_display()
    gravity()
  elif (map_change == 1):  #When character advances to map level 1
    starting_x = 25
    starting_y = 280 
    background()
    screen.blit(stage1_text, (350, 60))
    screen.blit(stage1_text1, (5, 180))
    screen.blit(stage1_text2, (5, 210))
    screen.blit(platform.image, platform.rect)
    screen.blit(rope.image, rope.rect)
    wall_display()
    laser_shoot()
    fox_display()
    if not coin1_taken:   # Displays coin1 until collided with
      coin1.rect.topleft = (280, 99)
      screen.blit(coin1.image, coin1.rect)
    if not coin2_taken:   # Displays coin2 until collided with
      coin2.rect.topleft = (330, 155)
      screen.blit(coin2.image, coin2.rect)
    if not coin3_taken:    # Displays coin3 until collided with
      coin3.rect.topleft = (360, 225)
      screen.blit(coin3.image, coin3.rect)
    if enemy_alive:   # Allows enemy to move if not killed
      enemy_movement()
      enemy.rect.topleft = (enemy_x, enemy_y)
      screen.blit(enemy.image, enemy.rect)
    x = x + x_move
    y = y + y_move
    heart_display()
    coin_display()
    gravity()
  elif (map_change == 2):   # Advances to map level 2
    starting_x = 25
    starting_y = 280  
    background()
    screen.blit(stage2_text, (300, 180))
    screen.blit(stage2_text1, (300, 210))
    screen.blit(platform.image, platform.rect)
    screen.blit(rope.image, rope.rect)
    wall_display()
    laser_shoot()
    fox_display()
    if not coin1_taken:   # Displays coin1 until collided with
      coin1.rect.topleft = (300, 75)
      screen.blit(coin1.image, coin1.rect)
    if not coin2_taken:    # Displays coin2 until collided with
      coin2.rect.topleft = (400, 75)
      screen.blit(coin2.image, coin2.rect)
    if not coin3_taken:    # Displays coin3 until collided with
      coin3.rect.topleft = (500, 75)
      screen.blit(coin3.image, coin3.rect)
    if enemy_alive:   # Allows enemy to move if not killed
      enemy_movement()
      enemy.rect.topleft = (enemy_x, enemy_y)
      screen.blit(enemy.image, enemy.rect)
    x = x + x_move
    y = y + y_move
    heart_display()
    coin_display()
    gravity()
  elif (map_change == 3): # Advances to map level 3
    background()
    wall_display()
    screen.blit(platform.image, platform.rect)
    screen.blit(rope.image, rope.rect)
    laser_shoot()
    fox_display()
    if not coin1_taken:   # Displays coin1 until collided with
      coin1.rect.topleft = (435, 200)
      screen.blit(coin1.image, coin1.rect)
    if not coin2_taken:    # Displays coin2 until collided with
      coin2.rect.topleft = (300,315)
      screen.blit(coin2.image, coin2.rect)
    if not coin3_taken:   # Displays coin2 until collided with
      coin3.rect.topleft = (700, 315)
      screen.blit(coin3.image, coin3.rect)
    if enemy_alive:  # Allows enemy to move if not killed
      enemy_movement()
      enemy.rect.topleft = (enemy_x, enemy_y)
      screen.blit(enemy.image, enemy.rect)
    x = x + x_move
    y = y + y_move
    heart_display()
    coin_display()
    gravity()
  elif (map_change == 4): # Advances to map level 4
    if not secret_map:    # If fox is not in the secret door, play normal map
      background()
      wall_display()
      screen.blit(platform.image, platform.rect)
      screen.blit(rope.image, rope.rect)
      door.rect.topleft = (168, 37)
      screen.blit(door.image,door.rect)
      screen.blit(stage4_text, (300,50))
      screen.blit(stage4_text1, (300,80))
      screen.blit(stage4_text2, (300, 110))
      laser_shoot()
      fox_display()
      if not coin1_taken:     # Displays coin1 until collided with
        coin1.rect.topleft = (200, 310)
        screen.blit(coin1.image, coin1.rect)
      if not coin2_taken:    # Displays coin2 until collided with
        coin2.rect.topleft = (400,310)
        screen.blit(coin2.image, coin2.rect)
      if not coin3_taken:    # Displays coin3 until collided with
        coin3.rect.topleft = (600, 310)
        screen.blit(coin3.image, coin3.rect)
      if enemy_alive:
        enemy_movement()
        enemy.rect.topleft = (enemy_x, enemy_y)
        screen.blit(enemy.image, enemy.rect)
      x = x + x_move
      y = y + y_move
      heart_display()
      coin_display()
      gravity()
    else:     # if fox enters secret door, use this map until user exits secret map
      background()
      wall_display()
      laser_shoot()
      enemy_alive = False
      coin1.rect.topleft = (-670, -100)       #Sending coin1 off screen 
      coin2.rect.topleft = (-670, -100)      # Sending coin2 off screen
      coin3.rect.topleft = (-670, -100)     # Sending coin3 off screen
      screen.blit(coin1.image, coin1.rect)
      screen.blit(coin2.image, coin2.rect)
      screen.blit(coin3.image, coin3.rect)
      screen.blit(platform.image, platform.rect)
      door.rect.topleft = (168, 37)
      screen.blit(door.image,door.rect)
      screen.blit(secret_stage_text, (300,50))
      screen.blit(secret_stage_text1, (300,80))
      screen.blit(secret_stage_text2, (10, 180))
      fox_display()

      if not mega_coin_taken:   #Display MEGA coin until collided with 
        mega_coin.rect.topleft = (450,200)
        screen.blit(mega_coin.image, mega_coin.rect)

      x = x + x_move
      y = y + y_move
      heart_display()
      coin_display()
      gravity()
  elif (map_change == 5):   # Advances to map level 5
    if (not enter_ship): # when fox has not entered the ship
      background()
      wall_display()
      screen.blit(stage5_text, (60, 100))
      screen.blit(airship_instruction, (60, 130))
      screen.blit(stage5_text1, (60, 160))
      screen.blit(stage5_text2, (60, 190))
      screen.blit(stage5_text3, (60, 210))
      screen.blit(stage5_text4, (60, 240))
      screen.blit(airship.image,airship.rect)
      laser_shoot()
      fox_display()
      x = x + x_move
      y = y + y_move
      heart_display()
      coin_display()
      gravity()
    else:     # When fox has entered the ship, start the airship stage
      if not airship_stage_prep:  # This code only plays once, to setup the airstage
        laser_hit = True
        laser_velocity = 0
        starting_x = 45
        starting_y = 140
        x = starting_x
        airship_x = starting_x
        airship_y = starting_y
        obstacle_y = wolf_y
        # Making sure enemy from previous stage does not appear in airstage
        enemy.rect.topleft = (-675, -675)
        enemy_alive = False
        laser.rect.topleft = (1000, 1000)
        ongoing_laser = False
        laser_hit = True
        screen.blit(airship.image,airship.rect)
        screen.blit(enemy.image, enemy.rect)
        screen.blit(laser.image, laser.rect)
        pygame.display.update()
        airship_stage_prep = True   # Finished preparing for airship stage
      final_wall_display()
      airstage()
      laser_shoot()
      airship_display()
      airship_y += y_move
      obstacle_movement()
      wolf_display()
      heart_display()
      coin_display()
      wolf_hp_display()
  elif (map_change == 6):   # When Fox enters map level 6 (After Boss Battle)
    starting_x = 25
    starting_y = 280
    background()
    wall_display()
    if not coin1_taken:     # Displays coin1 until collided with
      coin1.rect.topleft = (200, 310)
      screen.blit(coin1.image, coin1.rect)
    if not coin2_taken:    # Displays coin2 until collided with
      coin2.rect.topleft = (500,310)
      screen.blit(coin2.image, coin2.rect)
    if not coin3_taken:    # Displays coin3 until collided with
      coin3.rect.topleft = (700, 170)
      screen.blit(coin3.image, coin3.rect)
    screen.blit(platform.image, platform.rect)
    screen.blit(rope.image, rope.rect)
    stop_sign.rect.topleft = (760, 300)
    screen.blit(stop_sign.image, stop_sign.rect)
    screen.blit(castle.image, castle.rect)
    if enemy_alive:   # Allows enemy to move if not killed
      enemy_movement()
      enemy.rect.topleft = (enemy_x, enemy_y)
      screen.blit(enemy.image, enemy.rect)
    laser_shoot()
    screen.blit(stage6_text, (60, 100))
    screen.blit(stage6_text1, (60, 130))
    fox_display()
    x = x + x_move
    y = y + y_move
    heart_display()
    coin_display()
    gravity()
  elif (map_change == 7):   # When Fox enters map level 7 (Enters Castle)
    castle_bg()
    wall_display()
    laser_shoot()
    screen.blit(stage7_text, (170, 25))
    screen.blit(stage7_text1, (260, 50))
    fox_display()
    if fireball_true:  # fireballs continue to move until shot by target
      fireball1_movement()
      fireball2_movement()
      fireball3_movement()
    lava()
    screen.blit(target.image, target.rect)
    if not fireball_true:
      key.rect.topleft = (700,150)
      screen.blit(key.image,key.rect)
    x = x + x_move
    y = y + y_move
    heart_display()
    coin_display()
    gravity()

  # Change Left and Right Sprite depending on where character is facing
  if left:
      fox.image = pygame.image.load("images/fox_w2.png")
  else:
      fox.image = pygame.image.load("images/fox_w.png")

  # ---- Checking for collisions -------
  # If fox collides with wall, stop movement, move fox away from wall
  if (pygame.sprite.collide_rect(fox, wall)):
      x_move = 0
      x = x + 1
      y = y
      pygame.display.update()
  
  # If fox collides with barrier, stop sign, stop movement, move fox away from stop sign
  if (pygame.sprite.collide_rect(fox, stop_sign)):
      x_move = 0
      x = x - 1
      y = y
      pygame.display.update()

    # If fox collides with top wall, stop movement, move fox away from wall
  if (pygame.sprite.collide_rect(airship, top_wall)):
      airship_y += 1
      y_move = 0
      pygame.display.update()
  
  if (pygame.sprite.collide_rect(airship, bottom_wall)):
      airship_y -= 1
      y_move = 0
      pygame.display.update()

  # If fox collides with coin1, collect coin1 and make it disappear
  if (pygame.sprite.collide_rect(fox, coin1)):
      coins += 1
      coin1_taken = True
      coin1.rect.topleft = (-675, 10)
      screen.blit(coin1.image, coin1.rect)
      pygame.display.update()

  # If fox collides with coin2, collect coin2 and make it disappear
  if (pygame.sprite.collide_rect(fox, coin2)):
      coins += 1
      coin2_taken = True
      coin2.rect.topleft = (-675, 10)
      screen.blit(coin2.image, coin2.rect)
      pygame.display.update()

  # If fox collides with coin3, collect coin3 and make it disappear
  if (pygame.sprite.collide_rect(fox, mega_coin)):
      coins += 10
      mega_coin_taken = True
      mega_coin.rect.topleft = (-675, 10)
      screen.blit(mega_coin.image, mega_coin.rect)
      pygame.display.update()

  # If fox collides with MEGA Coin , collect MEGA coin and make it disappear
  if (pygame.sprite.collide_rect(fox, coin3)):
      coins += 1
      coin3_taken = True
      coin3.rect.topleft = (-675, 10)
      screen.blit(coin3.image, coin3.rect)
      pygame.display.update()

  # If laser collides with enemy,
  if (pygame.sprite.collide_rect(laser, enemy)):
      enemy.rect.topleft = (-675, -675)
      enemy_alive = False
      laser.rect.topleft = (1000, 1000)
      ongoing_laser = False
      laser_hit = True
      screen.blit(enemy.image, enemy.rect)
      screen.blit(laser.image, laser.rect)
      pygame.display.update()

  #    If laser collides with fireball 1 2 or 3
  if (pygame.sprite.collide_rect(laser, fireball1)):
    laser.rect.topleft = (1000, 1000)
    ongoing_laser = False
    laser_hit = True
    screen.blit(laser.image, laser.rect)
    pygame.display.update()
  
  if (pygame.sprite.collide_rect(laser, fireball2)):
    laser.rect.topleft = (1000, 1000)
    ongoing_laser = False
    laser_hit = True
    screen.blit(laser.image, laser.rect)
    pygame.display.update()
   
  if (pygame.sprite.collide_rect(laser, fireball3)):
      laser.rect.topleft = (1000, 1000)
      ongoing_laser = False
      laser_hit = True
      screen.blit(laser.image, laser.rect)
      pygame.display.update()

  # If laser collides with target
  if (pygame.sprite.collide_rect(laser, target)):
      laser.rect.topleft = (1000, 1000)
      ongoing_laser = False
      laser_hit = True
      screen.blit(laser.image, laser.rect)
      fireball_true = False
      target_hit = True
      target.rect.topleft = (1000,1000)
      fireball1.rect.topleft = (1000,1000)
      fireball2.rect.topleft = (1000,1000)
      fireball3.rect.topleft = (1000,1000)
      screen.blit(target.image,target.rect)
      screen.blit(fireball1.image,fireball1.rect)
      screen.blit(fireball1.image,fireball2.rect)
      screen.blit(fireball1.image,fireball3.rect)

      # Spawning Key on bridge
      screen.blit(key.image,key.rect)
      pygame.display.update()

  # If fox collects key
  if (pygame.sprite.collide_rect(fox, key)):
    img = "images/landmaster.png"
    text = "Congratulations on collecting the key, The Landmaster (image below) is now back in your hands!"
    restart_list = ["Restart Game", "End Game"]
    restart_end = ("")
    while not restart:
      restart_end = easygui.buttonbox(text, title, image = img, choices = restart_list)
      pygame.display.update()
      if restart_end == "Restart Game":
        airship_stage_prep = False
        stop_sign.rect.topleft = (800,800)
        screen.blit(stop_sign.image,stop_sign.rect)
        map_change = 0
        wolf_hp = 10
        wolf_x = 600
        wolf_y = 110
        wolf_y_move = 1
        fox_ground_y = 280
        key.rect.topleft = (800,800)
        screen.blit(key.image,key.rect)
        obstacle.rect.topleft = (2000,800)
        screen.blit(obstacle.image,obstacle.rect)
        target.rect.topleft = (2000,800)
        screen.blit(target.image,target.rect)
        lives = 3
        enemy_x = 460
        enemy_y = 270
        x = 25
        y = 280
        fireball_true = True
        target_hit = False
        platform.rect.topleft = (510, 110)
        rope.rect.topleft = (670, 115)
        enemy_alive = True
        coin1_taken = False
        coin2_taken = False
        coin3_taken = False
        coins = 0
        direction = 1
        fox.rect.topleft = (x, y)
        screen.blit(fox.image, fox.rect)
        wall_display()
        heart_display()
        coin_display()
        pygame.display.update()
        laser_vel_multiply = 1
        break
      elif restart_end == "End Game":
          pygame.quit()
      else:
          restart_end = ("")

  # If fox collides with enemy, lose 1 heart, lose 1 coins, set fox to starting position
  if (pygame.sprite.collide_rect(fox, enemy)):
      x_move = 0
      lives -= 1
      if coins <1:  # Makes sure that coins value does not go into negatives
        coins = 0
      else:
        coins -= 1
      x = starting_x
      y = starting_y
      pygame.display.update()

      # If fox collides with obstacle, lose 1 heart, lose 1 coins, set fox to starting position
  if (pygame.sprite.collide_rect(fox, obstacle)):
      x_move = 0
      lives -= 1
      if coins <1:  # Makes sure that coins value does not go into negatives
        coins = 0
      else:
        coins -= 1
      x = starting_x
      y = starting_y
      pygame.display.update()

    # If airship collides with obstacle, lose 1 heart, set airship to a different y value
  if (pygame.sprite.collide_rect(obstacle, airship)):
      obstacle_x = -100
      lives -= 1
      if airship_y > 200:
        airship_y -= 100
      else:
        airship_y += 100
      screen.blit
      pygame.display.update()

 # If fox collides with fireball1, lose 1 heart, lose 1 coins, set fox to starting position
  if (pygame.sprite.collide_rect(fox, fireball1)):
      x_move = 0
      lives -= 1
      if coins <1:  # Makes sure that coins value does not go into negatives
        coins = 0
      else:
        coins -= 1
      x = starting_x
      y = starting_y
      pygame.display.update()

 # If fox collides with fireball2, lose 1 heart, lose 1 coins, set fox to starting position
  if (pygame.sprite.collide_rect(fox, fireball2)):
      x_move = 0
      lives -= 1
      if coins <1:  # Makes sure that coins value does not go into negatives
        coins = 0
      else:
        coins -= 1
      x = starting_x
      y = starting_y
      pygame.display.update()

 # If fox collides with fireball3, lose 1 heart, lose 1 coins, set fox to starting position
  if (pygame.sprite.collide_rect(fox, fireball3)):
      x_move = 0
      lives -= 1
      if coins <1:  # Makes sure that coins value does not go into negatives
        coins = 0
      else:
        coins -= 1
      x = starting_x
      y = starting_y
      pygame.display.update()
  # If laser collides with boss battle enemy (Wolf),
  if (pygame.sprite.collide_rect(laser, wolf)):
      laser.rect.topleft = (-1000, -1000)
      ongoing_laser = False
      laser_hit = True
      wolf_hit = True
      wolf_hp -= 1
      screen.blit(enemy.image, enemy.rect)
      screen.blit(laser.image, laser.rect)
      pygame.display.update()

#   If airship shoots a laser at an obstacle, user gains 2 coins
  if (pygame.sprite.collide_rect(laser, obstacle)):
    laser.rect.topleft = (800,800)
    ongoing_laser = False
    laser_hit = True
    obstacle_hit = True
    if enter_ship:
      coins += 2
    pygame.display.update()

  # If fox is colliding with rope, and interacting with it
  if (pygame.sprite.collide_rect(fox, rope)):
      gravity_true = False
      if interact:
        y_move = -1
      else:
        y_move = 0
        # if x<280:
        #   y_move = 1
  else:
      gravity_true = True

  # If fox is colliding with platform
  if (pygame.sprite.collide_rect(fox, platform)):
    if interact and (pygame.sprite.collide_rect(fox, rope)):
      gravity_true = False
      y_move = -1
    elif (fox.rect.bottom - 4 > platform.rect.top):
      y_move = -1
    else:
      y_move = 0
  else:
    gravity_true = True


  # If fox collides with door, and interacting with it (and has 7 coins)
  if (pygame.sprite.collide_rect(fox, door)):
    if interact and (coins >= 7):
      secret_map = True
      door.image = pygame.image.load("images/door_open.png")
      enemy.rect.topleft = (1075, -675)
      screen.blit(enemy.image, enemy.rect)
    pygame.display.update()


  #  If fox collides with the airship, start the airstage level (enter_ship = True)
  if (pygame.sprite.collide_rect(fox, airship)): 
   x = -300
   y = -300
   obstacle_alive = True
   laser.image = pygame.image.load("images/laser_airship.png")
   fox.rect.topleft = (x,y)
   enter_ship = True
   laser_hit = True
   laser_velocity = 0


  # If fox collides with the map advancing wall, refresh screen with new level
  if (pygame.sprite.collide_rect(fox, advance_wall)):
    background()
    map_change += 1
    enemy_alive = True
    coin1_taken = False
    coin2_taken = False
    coin3_taken = False
    direction = 1
    x = 25
    y = y  # 280 is floor level
    fox.rect.topleft = (x, y)
    screen.blit(fox.image, fox.rect)
    wall_display()
    heart_display()
    coin_display()
    if (map_change == 1):   # Setting up some variables for next map (1) change
      platform.rect.topleft = (-80, 110)
      rope.rect.topleft = (800,800)
      laser_hit = True
      laser_velocity = 0
      enemy_x = 600
      enemy_y = 280
    elif (map_change == 2): # Setting up some variables for next map (2) change
      platform.rect.topleft = (250, 110)
      laser_hit = True
      laser_velocity = 0
      enemy_x = 360
      enemy_y = 25
      rope.rect.topleft = (250, 115)
    elif (map_change == 3): # Setting up some variables for next map (3) change
      platform.rect.topleft = (470, 110)
      laser_hit = True
      laser_velocity = 0
      enemy_x = 480
      enemy_y = 180
      rope.rect.topleft = (470, 115)
    elif (map_change == 4): # Setting up some variables for next map (3) change
      platform.rect.topleft = (-80, 110)
      rope.rect.topleft = (800,800)
      laser_hit = True
      laser_velocity = 0
      enemy_x = 210
      enemy_y = 60
    elif (map_change == 5):
      if not enter_ship:    # Setting up variables for before fox gets into airship
        laser_hit = True
        laser_velocity = 0
        enemy_alive = False
        enemy_x = 800
        enemy_y = 800
        screen.blit(enemy.image, enemy.rect)
        airship.rect.topleft = (600, 280)
    elif (map_change == 7): #setting up variables for map 7
      enemy_alive = False
      laser_hit = True
      laser_velocity = 0
      fox_ground_y = 141
      starting_x = 5
      starting_y = 141
      y = starting_y
      enemy.rect.topleft = (800,800)
      screen.blit(enemy.image,enemy.rect)
      target.rect.topleft = (753, 150)


  if (lives == 0):   # Game over text when lives are gone
    background()
    screen.blit(game_over_text, (120,270))
    screen.blit(game_over_text2, (400,280))
    pygame.display.update()
    while not restart:
      restart = easygui.ynbox("Would you like to restart the game?", title)
      pygame.display.update()
      if restart:
        map_change = 0
        stop_sign.rect.topleft = (800,800)
        screen.blit(stop_sign.image,stop_sign.rect)
        wolf_hp = 10
        wolf_x = 600
        wolf_y = 110
        wolf_y_move = 1
        fox_ground_y = 280
        key.rect.topleft = (800,800)
        screen.blit(key.image,key.rect)
        obstacle.rect.topleft = (2000,800)
        screen.blit(obstacle.image,obstacle.rect)
        target.rect.topleft = (2000,800)
        screen.blit(target.image,target.rect)
        fireball_true = True
        target_hit = False
        lives = 3
        coins = 0
        enemy_x = 460
        enemy_y = 270
        x = 25
        y = 280
        airship_stage_prep = False
        platform.rect.topleft = (510, 110)
        rope.rect.topleft = (670, 115)
        enemy_alive = True
        coin1_taken = False
        coin2_taken = False
        coin3_taken = False
        direction = 1
        fox.rect.topleft = (x, y)
        screen.blit(fox.image, fox.rect)
        wall_display()
        heart_display()
        coin_display()
        pygame.display.update()
      else:
        pygame.quit()
    restart = False

  #  When wolf (Boss) runs out of hp, spawn into next level with power up
  if (wolf_hp == 0):
    selection_stage = True
    airstage()
    wolf_x = 100000
    wolf_y = 800
    obstacle_x = 100000
    obstacle_y = 0
    wolf.rect.topleft = (wolf_x, wolf_y)
    obstacle.rect.topleft = (obstacle_x, obstacle_y)
    screen.blit(wolf.image, wolf.rect)
    screen.blit(obstacle.image, obstacle.rect)
    screen.blit(airship.image, airship.rect)
    screen.blit(game_won_text, (200,250))
    screen.blit(game_won_text1, (430, 280))
    pygame.display.update()
    while not power_up or (power_up is None):
      msg = ("Congratulations on beating Wolf! You unlocked a Power Up; Speed Lasers!")
      power_up = easygui.msgbox(msg, title, ok_button = ("Great!"))
    if power_up:
      enter_ship = False
      laser.image = pygame.image.load("images/laser.png")
      map_change = 6
      wolf_hp = 1
      laser_vel_multiply = 3
      # Setting up variables for after boss battle finishes (locations, enemies, etc.)
      platform.rect.topleft = (580, 110)
      rope.rect.topleft = (500,200)
      airship_x = 800
      airship_y = 800
      airship.rect.topleft = (airship_x, airship_y)
      screen.blit(airship.image, airship.rect)
      rope.rect.topleft = (670, 215)
      platform.rect.topleft = (510, 210)
      laser_hit = True
      enemy_alive = True
      laser_velocity = 0
      enemy_x = 540
      enemy_y = 160
      x = 25
      y = 280
      starting_x = 5
      fox.rect.topleft = (x,y)
      screen.blit(fox.image, fox.rect)

  pygame.display.update()

  # --- Main event loop
  event = pygame.event.poll()
  if (event.type == pygame.QUIT):  # Quits Game if closed
    done = True
  elif (event.type == pygame.KEYDOWN):  # Key is pressed
    if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
      x_move = 1
      left = False

    elif (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
      x_move = -1
      left = True

    elif (event.key == pygame.K_TAB):
      begin = True
      if during_scene:
        skip_scene = True
        

    elif (event.key == pygame.K_UP) or (event.key == pygame.K_w):
      if not enter_ship:  #if fox has not entered ship (normal map levels)
        interact = True
      else:
        y_move = -2
    elif (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
      if enter_ship:   # Checking to see if airship stage is currently running
        y_move = 2
    elif (event.key == pygame.K_SPACE):
      if begin:
        if (coins > 0) and (not ongoing_laser) and (not laser_hit):  # If you have coins and there is no laser currently ongoing, you will be able to shoot
            coins -= 1  # Takes away  a coin per laser blast
            laser_shot = True
            laser_x = x
            laser_y = y
            if left:
              laser_velocity = -2 * laser_vel_multiply # Laser goes left if facing left (goes faster if user has a laser velocity multiplier)
            else:
              laser_x += 50
              laser_velocity = 2 * laser_vel_multiply  # Laser goes right if facing right (goes faster if user has a laser velocity multiplier)
            if enter_ship:
              laser_y = airship_y - 6
              laser_velocity = 3
            
        elif laser_hit:   
          laser_hit = False
  elif (event.type == pygame.KEYUP):  # When key is let go of
      y_move = 0
      x_move = 0
      interact = False
      skip_scene = False
  clock.tick(100)
pygame.quit()

