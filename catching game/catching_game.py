import pygame
import random
import time

pygame.init()
WIN = pygame.display.set_mode((500,400))
ICON = pygame.image.load('groceries.png')
pygame.display.set_icon(ICON)
pygame.display.set_caption("Catch them All")
BACKGROUND = (230,230,230)
OBJECT_SIZE = (50,50)
FONT = pygame.font.SysFont(None, 25)
FONT2 = pygame.font.SysFont(None, 50)
BASKET_PLAYER = pygame.transform.scale(pygame.image.load("wicker-basket.png"),(60,60))
BREAD = pygame.transform.scale(pygame.image.load("bread.png"),(OBJECT_SIZE))
APPLE = pygame.transform.scale(pygame.image.load("apple.png"),(OBJECT_SIZE))
SHOE = pygame.transform.scale(pygame.image.load("shoe-1.png"),(OBJECT_SIZE))
BALL = pygame.transform.scale(pygame.image.load("soccer-ball-variant.png"),(OBJECT_SIZE))
object_list = [BREAD,APPLE,BALL,SHOE]


VEL = 5
VEL_OBJ = 1
FPS = 60


def draw_end():
    WIN.fill(BACKGROUND)
    text = FONT2.render("YOU WON!!!!",1,(0,0,0))
    WIN.blit(text,(150,170))
    pygame.display.update()

def draw_things(BACKGROUND,player,food_list,food):
    WIN.fill(BACKGROUND)
    text = FONT.render("Score: "+ str(score),1,(0,0,0))
    WIN.blit(text,(5,5))
    player.draw(WIN)
    n = 0

    for food in food_list:
        food.draw(WIN)
        n += 1

    pygame.display.update()

class Player():
    def __init__(self,x,y,image):
        self.x = x
        self.y = y
        self.VEL = 5
        self.image = image
        self.mask = pygame.mask.from_surface(image)

    def draw(self,WIN):
        WIN.blit(self.image, (self.x,self.y))

    def move(self,VEL):
        if keys_pressed[pygame.K_d] and self.x < 440:
            self.x += VEL
        if keys_pressed[pygame.K_a] and self.x > 0:
            self.x -= VEL


class Food():
    def __init__(self,x,y,image):
        self.x = x
        self.y = y
        self.image = image
        self.mask = pygame.mask.from_surface(image)


    def draw(self,WIN):
        WIN.blit(self.image, (self.x,self.y))

    def move(self):
        self.y += VEL_OBJ

    def collision(self,player,food_list,score):
        offset = (int(self.x - player.x), (int(self.y - player.y)))
        collide = self.mask.overlap(player.mask,offset)
        if collide:
            food_list.remove(self)
            score_check.append("n")


def main():
    clock = pygame.time.Clock()

    global  food_list,score_check,score

    player = Player(250,300,BASKET_PLAYER)

    food_list = []
    score_check = []
    score = 0
    foods = 15

    for i in range(foods):
        food = Food(random.randint(0, 400),random.randint(-600,0), random.choice(object_list))
        food_list.append(food)


    run = True
    while run:

        x = 0
        while x <= len(score_check):
            score = len(score_check)
            x += 1

        if len(food_list) == 0:
            draw_end()
            time.sleep(3)
            break

        for food in food_list:
            food.move()
            food.collision(player,food_list,score)



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

        global keys_pressed
        keys_pressed = pygame.key.get_pressed()
        draw_things(BACKGROUND,player,food_list,food)
        player.move(VEL)

        clock.tick(FPS)

    pygame.quit()

if __name__=="__main__":
    main()