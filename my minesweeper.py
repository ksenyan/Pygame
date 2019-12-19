import random
import pygame
pygame.init()

size = (500,600)
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()
font = pygame.font.SysFont("Papyrus",70)
fontsmall = pygame.font.SysFont("Papyrus",40)
fonttiny = pygame.font.SysFont("Papyrus",30)

fontx = 0
fonty = 0

mouse_state = 0
mouse_x = 0
mouse_y = 0

Columns = 0
Rows = 0
Mines = 0

FPS = 30
playtime = 0.0
gameState = 'title'

all_sprites = pygame.sprite.Group()

spritex = 25
spritey = 125

bombx = 125
bomby = 175

flags = 23



class greybox(pygame.sprite.Sprite):
    def __init__(self, spritex, spritey):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill((50,40,50))
        self.rect = self.image.get_rect()
        self.rect.center = (spritex, spritey)
        

class bombs(pygame.sprite.Sprite):
    def __init__(self, bombx, bomby):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (bombx, bomby)

def number1():
    text = fonttiny.render("1",True,(225,225,225))
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((textx - (text_x / 2)),(texty - (text_y / 2))))
def number0():
    text = fonttiny.render("0",True,(225,225,225))
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((textx - (text_x / 2)),(texty - (text_y / 2))))
def number2():
    text = fonttiny.render("2",True,(225,225,225))
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((textx - (text_x / 2)),(texty - (text_y / 2))))
def number3():
    text = fonttiny.render("3",True,(225,225,225))
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((textx - (text_x / 2)),(texty - (text_y / 2))))
def number4():
    text = fonttiny.render("4",True,(225,225,225))
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((textx - (text_x / 2)),(texty - (text_y / 2))))

def game():
    screen.fill((117, 127, 117))
    all_sprites.update()
    all_sprites.draw(screen)
    
    
def menu():
    screen.fill((127, 157, 127))
    text = font.render("MINE",True,(0,0,0))
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((250 - (text_x / 2)),(100 - (text_y / 2))))
    text = font.render("SWEEPER",True,(0,0,0))
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((250 - (text_x / 2)),(200 - (text_y / 2))))
    text = font.render("--------------",True,(0,0,0))
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((250 - (text_x / 2)),(250 - (text_y / 2))))
    textsmall = fontsmall.render("Press button to start",True,(0,0,0))
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(textsmall,((250 - (text_x / 2)),(350 - (text_y / 2))))
    
def topBar():
    pygame.draw.rect(screen, (0,0,0), (0,0,500,100))
    text = fontsmall.render((str(int(playtime))), True, (255,255,255))
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((50 - (text_x / 2)),(50 - (text_y / 2))))
    text = fontsmall.render((str(int(flags))+ "  Flags remaining"), True, (255,255,255))
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((300 - (text_x / 2)),(25 - (text_y / 2))))
    text = fonttiny.render(("Reset"), True, (255,255,255))
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((300 - (text_x / 2)),(70 - (text_y / 2))))  
    
while not done:
    
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    milliseconds = clock.tick(30)
    playtime += milliseconds / 1000.0
    text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
    pygame.display.set_caption(text)
    
    pygame.display.flip()
    pygame.display.update()
    
    

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    gameState = 'quit'
                    done = True
        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse_state = event.button
            pygame.mouse.set_pos(mouse_x,mouse_y + 1)

    if gameState == 'game':
        game()
        topBar()
        
        for event in pygame.event.wait():   
            if event.type == MOUSEBUTTONUP:
                x,y = event.pos
                for greybox in boxes:
                    if greybox.rect.collidepoint(x,y):
                        print ('yay!')
            else:
                mouse_state = 0       
        for steps in range (10):
            for steps in range (10):
                newbox = greybox(spritex, spritey)
                spritex +=50
                all_sprites.add(newbox)
            
            spritex = 25
            spritey += 50
        for steps in range (2):
            newbomb = bombs(bombx, bomby)
            bombx += 50
            all_sprites.add(newbomb)
        def placeone():
            newbomb = bombs(bombx, bomby)
            all_sprites.add(newbomb)
        bombx += 50
        placeone()
        bombx += 150
        placeone()
        bombx += 50
        placeone()
        bomby = 275
        bombx = 75
        placeone()
        bombx += 250
        placeone()
        bomby += 50
        bombx = 175
        placeone()
        bombx += 200
        placeone()
        bomby += 50
        bombx = 25
        placeone()
        bombx += 250
        placeone()
        bombx += 50
        placeone()
        bomby += 50
        bombx = 25
        for steps in range (2):
            placeone()
            bombx += 50
        bombx = 475
        placeone()
        bomby += 50
        bombx = 175
        for steps in range (2):
            placeone()
            bombx += 50
        bomby += 50
        bombx = 175
        placeone()
        bombx += 150
        for steps in range (2):
            placeone()
            bombx += 50
        bomby += 50
        bombx = 75
        placeone()
        bombx += 150
        placeone()
        bombx += 100
        placeone()
        bomby = 175
        bombx = 125
        spritex = 25
        spritey = 125

        textx = 25
        texty = 125
        number0()
        textx += 50
        number1()
        for steps in range (3):
            textx += 50
            number2()
        for steps in range (3):
            textx += 50
            number1()
        for steps in range (2):
            textx += 50
            number2()
        texty = 175
        textx = 25
        number0()
        textx += 50
        number1()
        textx += 150
        number2()
        textx += 100
        for steps in range (2):
            number1()
            textx += 50
        texty += 50
        textx = 25
        number1()
        textx += 50
        number2()
        textx += 50
        number3()
        for steps in range (7):
            textx += 50
            number2()
        textx = 25
        texty += 50
        number1()
        textx += 100
        number2()
        for steps in range (3):
            textx += 50
            number1()
        textx += 100
        number2()
        textx += 50
        number1()
        textx += 50
        number0()
        textx = 25
        texty += 50
        for steps in range (3):
            number2()
            textx += 50
        textx += 50
        number2()
        textx += 50
        number3()
        textx += 50
        number4()
        textx += 100
        number1()
        textx += 50
        number0()
        texty += 50
        textx = 75
        number3()
        textx += 50
        number2()
        textx += 50
        number1()
        textx += 50
        number2()
        textx += 150
        for steps in range (2):
            number2()
            textx += 50
        number1()
        texty += 50
        textx = 125
        for steps in range (2):
            number2()
            textx += 50
        for steps in range (2):
            number3()
            textx += 50
        number2()
        for steps in range (2):
            textx += 50
            number1()
        textx = 25
        texty += 50
        for steps in range (2):
            number2()
            textx += 50
        number3()
        textx += 150
        for steps in range (4):
            number2()
            textx += 50
        number1()
        textx = 25
        texty += 50
        for steps in range(2):
            number1()
            textx += 50
        number3()
        textx += 100
        for steps in range (2):
            number4()
            textx += 50
        textx += 100
        number1()
        textx += 50
        number0()
        textx = 25
        texty += 50
        number1()
        textx += 100
        for steps in range (2):
            number2()
            textx += 50
        textx += 50
        number3()
        textx += 100
        number3()
        textx +=50
        number1()
        textx += 50
        number0()
            
        if mouse_x > 300 and mouse_x < 350 and mouse_y > 70 and mouse_y < 100 : 
            if event.type == pygame.MOUSEBUTTONUP:
                playtime = 0.0
                
    elif gameState == 'title':
        playtime = 0.00
        menu()
        if mouse_x > 120 and mouse_x < 370 and mouse_y > 400 and mouse_y < 500 : 
            pygame.draw.rect(screen, (50,50,50), (120,400,250,100))
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONUP:
                print ("Game Starts Now")
                game()
                gameState = 'game'
        else:
            pygame.draw.rect(screen, (0,0,0), (120,400,250,100))

        
pygame.quit()
