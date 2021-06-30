import pygame
import random
from pygame.locals import *

# retorna a maçã na tela em uma grade divisível por 10


def on_grid():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x // 10 * 10, y // 10 * 10)

# colisão da cobra com a maçã


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def restart_game():
    global snake, pontos, mydirect
    snake = []
    pontos = len(snake)
    mydirect = LEFT
    on_grid()

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
x = 200
y = 200

# inicia o evento game em tela
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Killer worm')

font = pygame.font.SysFont('arial', 20, True, True)

# musica_fundo = pygame.mixer.music.play(-1)


snake = [(x, y), (x, y), (x,y)]
snake_skin = pygame.Surface((8, 8))
snake_skin.fill((0, 255, 0))

apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))
apple_pos = on_grid()

pontos = len(snake)
apple_point = 1

mydirect = LEFT
velocidade = 15

clock = pygame.time.Clock()

while True:

    clock.tick(velocidade)
    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)

    mensagem = f'Pontos: {pontos}'
    textformat = font.render(mensagem, True,(255,255,255))
    screen.blit(textformat, (450,30))

    mensagem2 = f'velox: {velocidade}'
    textformat2 = font.render(mensagem2, True,(255,255,255))
    screen.blit(textformat2, (450,60))

    mensagem3 = f'apple: {apple_point}'
    textformat3 = font.render(mensagem3, True,(255,255,255))
    screen.blit(textformat3, (450,90))
    
    

    for pos in snake:
        screen.blit(snake_skin, pos)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()



        if event.type == KEYDOWN:
            if event.key == K_UP:
                mydirect = UP
            if event.key == K_DOWN:
                mydirect = DOWN
            if event.key == K_LEFT:
                mydirect = LEFT
            if event.key == K_RIGHT:
                mydirect = RIGHT

            if event.key == K_r:
                restart_game()
            if event.key == K_d:
                apple_point = apple_point + 1
            if event.key == K_s:
                apple_point = apple_point - 1
            if event.key == K_x:
                velocidade = velocidade + 5
            if event.key == K_z:
                velocidade = velocidade - 5

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if collision(snake[0], apple_pos):
        apple_pos = on_grid()
        for ok in range(apple_point):
            ok= snake.append((610, 610))
        pontos = len(snake)
        

    if snake.count(snake) > 1:
        break

    if mydirect == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
        # event.key (K_DOWN): False
    if mydirect == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if mydirect == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if mydirect == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    # if snake[0][0] <= 0:
    #     snake[0][0] = 590
    # elif snake[0][0] >=600:
    #     snake[0][0] = 0

    # if snake[0][1] <= 10:
    #     snake[0][1] = 590
    # elif snake[0][1] >=600:
    #     snake[0][1] = 0
    




    

    pygame.display.update()