import pygame, time, random, math

class vector:

    def __init__ (self, i, j):
        self.i = i
        self.j = j

    def __mul__(self, other):
        if (type(other) == int):
            return vector(self.i * other, self.j * other)

    def __str__(self):
        return str(self.i) + ", " + str(self.j)

    def unit(self):
        m = ( self.i ** 2 + self.j ** 2 ) ** 0.5
        if m == 0:
            return (0, 0)
        return  vector(self.i / m, self.j / m)

class denemy:
    def __init__(self, vector):
        self.vector = vector

    def __str__(self):
        return '(' + str(selenemiesf.vector.i) + ', ' + str(self.vector.j) + ')'
        
def ship_movement(image, x, y):
    game_display.blit(image, (x, y))

def unit_vector(pt1, pt2):
    m = ((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2) ** 0.5
    if m < 1:
        return (0, 0)
    return  ((pt2[0] - pt1[0]) / m, (pt2[1] - pt1[1]) / m)

def scale_vector(pt1, pt2, scale):
    scale = 60/scale
    
    if scale < 1:
        return (0, 0)
    return  (pt2[0] - pt1[0]) / scale, (pt2[1] - pt1[1]) / scale

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(game_display, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(game_display, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    game_display.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(game_display, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(game_display, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    game_display.blit(textSurf, textRect)

def waves_surived(count, color):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Waves survived: "+str(count), True, color)
    game_display.blit(text,(0,0))
    
def user_movement(ship, x, y):
    mouse_location = pygame.mouse.get_pos()

    i, j = unit_vector((x, y), mouse_location)
    #i,j = scale_vector((x, y), mouse_location, 2)
    #print(i, j vector(mouse_location[0] - x, mouse_location[1] - y).unit())
    x, y = x + i, y + j

    game_display.blit(ship, ((x - ship.get_width() / 2,
                              y - ship.get_width() / 2 )))

    return x, y

def enemy_movement(ship, user_location, enemy_location):
    i, j = unit_vector(enemy_location, user_location)
    x, y = enemy_location[0] + i, enemy_location[1] + j

    game_display.blit(ship, ((x - ship.get_width() / 2,
                              y - ship.get_width() / 2)))

    return (x, y)

def bullet_movement(bullet, bullet_location, direction):
    x, y = bullet_location[0] + direction[0], bullet_location[1] + direction[1]
    game_display.blit(bullet, ((x - bullet.get_width() / 2,
                              y - bullet.get_width() / 2)))

    return (x, y)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        game_display.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Spaceone", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        game_display.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        button("Memory", 350, 450, 100, 50, blue, bright_blue, memory_game)
        
        pygame.display.update()
        clock.tick(15)

def memory_game():
    x = display_width / 2
    y = display_height / 2

    unit_count = 1
    speed = 3
    
    enemies = {}
    bullets = {}

    to_del = {'bullets': '', 'enemies': ''}

    dead = False

    while not dead:

        if len(enemies) == 0:

            for num in range(0, unit_count):
                randnum = random.randint(1, 4)
                if randnum == 1:
                    enemies[num] = (random.randint(-100, 900), random.randint(-100, -50))
                elif randnum == 2:
                    enemies[num] = (random.randint(900, 1000), random.randint(-100, 700))
                elif randnum == 3:
                    enemies[num] = (random.randint(-100, 900), random.randint(600, 650))
                else:
                    enemies[num] = (random.randint(-100, -50), random.randint(-100, 700))
            unit_count += 1

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_location = pygame.mouse.get_pos()
                bullets[unit_vector((x, y), mouse_location)] = (x, y)
            
        game_display.fill(black)

        for bul in bullets:
            game_display.blit(bullet, bullets[bul])

            for enemy in enemies:

                #if (math.sqrt((enemies[enemy][0] - bullets[bul][0])**2) <  enemy_ship.get_width() and math.sqrt((enemies[enemy][1] - bullets[bul][1])**2) > enemy_ship.get_width()):
                if enemies[enemy][0] - bullets[bul][0] < 1 and enemies[enemy][1] - bullets[bul][1] < 1:

                    to_del['bullets'] = bul
                    to_del['enemies'] = enemy


        if len(to_del) != 1:
            if len(to_del['bullets']) > 0:                    
                del bullets[to_del['bullets']]
                to_del['bullets'] = ''
            if len(str(to_del['enemies'])) > 0:
                del enemies[to_del['enemies']]
                to_del['enemies'] = ''

##
##        bullets = {key:bullets[key] for key in bullets if key != 'deleted'}
##        enemies = {key:enemies[key] for key in enemies if key != 'deleted'}
##        
        x, y = user_movement(user_ship, x, y)
        
        for enemy in enemies:
            enemies[enemy] = enemy_movement(enemy_ship, (x, y), enemies[enemy])
            if y < enemies[enemy][1] < y + 50:
                if x > enemies[enemy][0] and x < enemies[enemy][0] + user_ship.get_width() or x+user_ship.get_width() > enemies[enemy][0] and x + user_ship.get_width() < enemies[enemy][0]+user_ship.get_width():
                    dead = True

        waves_surived(unit_count - 2, white)
        pygame.display.update()
        clock.tick(60)
        
def game_loop():
    x = display_width / 2
    y = display_height / 2

    unit_count = 1
    speed = 3
    
    enemies = {}
    bullets = {}

    to_del = {'bullets': '', 'enemies': ''}

    dead = False

    while not dead:

        if len(enemies) == 0:

            for num in range(0, unit_count):
                randnum = random.randint(1, 4)
                if randnum == 1:
                    enemies[num] = (random.randint(-100, 900), random.randint(-100, -50))
                elif randnum == 2:
                    enemies[num] = (random.randint(900, 1000), random.randint(-100, 700))
                elif randnum == 3:
                    enemies[num] = (random.randint(-100, 900), random.randint(600, 650))
                else:
                    enemies[num] = (random.randint(-100, -50), random.randint(-100, 700))
            unit_count += 1

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_location = pygame.mouse.get_pos()
                vector = unit_vector((x, y), mouse_location)
                bullets[vector[0] * 4, vector[1] * 4] = (x, y)
            
        game_display.fill(white)

        for bul in bullets:
            bullets[bul] = bullet_movement(bullet, bullets[bul], bul)
            if bullets[bul][0] < 0 or bullets[bul][0] > 800 or bullets[bul][1] < 0 or bullets[bul][1] > 600:
                to_del['bullets'] = bul

            for enemy in enemies:

                #if (math.sqrt((enemies[enemy][0] - bullets[bul][0])**2) <  enemy_ship.get_width() and math.sqrt((enemies[enemy][1] - bullets[bul][1])**2) > enemy_ship.get_width()):
                if enemies[enemy][0] - bullets[bul][0] < 1 and enemies[enemy][1] - bullets[bul][1] < 1:

                    
                    to_del['enemies'] = enemy

        if len(to_del) != 1:
            if len(to_del['bullets']) > 0:                    
                del bullets[to_del['bullets']]
                to_del['bullets'] = ''
            if len(str(to_del['enemies'])) > 0:
                del enemies[to_del['enemies']]
                to_del['enemies'] = ''
##
##        bullets = {key:bullets[key] for key in bullets if key != 'deleted'}
##        enemies = {key:enemies[key] for key in enemies if key != 'deleted'}
##        
        x, y = user_movement(user_ship, x, y)
        
        for enemy in enemies:
            enemies[enemy] = enemy_movement(enemy_ship, (x, y), enemies[enemy])
            if y < enemies[enemy][1] < y + 50:
                if x > enemies[enemy][0] and x < enemies[enemy][0] + user_ship.get_width() or x+user_ship.get_width() > enemies[enemy][0] and x + user_ship.get_width() < enemies[enemy][0]+user_ship.get_width():
                    dead = True

        waves_surived(unit_count - 2, black)
        pygame.display.update()
        clock.tick(60)

display_width = 800
display_height = 600
 
black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)
blue = (0, 0, 200)

bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0, 0, 255)            

pygame.init()

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Spaceone')
clock = pygame.time.Clock()

user_ship = pygame.image.load('spaceship.png')
enemy_ship = pygame.image.load('otherspaceship.png')
bullet = pygame.image.load('bullet.png')

pygame.display.set_icon(enemy_ship)

game_intro()
pygame.quit()
quit()
