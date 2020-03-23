import pygame
import random
from time import sleep

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()

largura = 320
altura = 320

fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("TicTacToe")

def texto(msg, cor, tam, x, y):
    fonte = pygame.font.SysFont(None, tam)
    texto1 = fonte.render(msg, True, cor)
    fundo.blit(texto1, [x, y])

def circulo(centro):
    if centro == 0 or centro == 1 or centro == 2:
        if centro == 0:
            centro = 53*(centro+1)
        if centro == 1:
            centro = 53*(centro+2)
        if centro == 2:
            centro = 53*(centro+3)
        pos_circulo = (centro, 53)
    if centro == 3 or centro == 4 or centro == 5:
        if centro == 3:
            centro = 53*(centro-2)
        if centro == 4:
            centro = 53*(centro-1)
        if centro == 5:
            centro = 53*centro
        pos_circulo = (centro, 160)
    if centro == 6 or centro == 7 or centro == 8:
        if centro == 6:
            centro = 53*(centro-5)
        if centro == 7:
            centro = 53*(centro-4)
        if centro == 8:
            centro = 53*(centro-3)
        pos_circulo = (centro, 266)
    pygame.draw.circle(fundo, black, pos_circulo, 30)

def cruz(cruzx, cruzy):
    pygame.draw.line(fundo, black, (cruzx, cruzy), (cruzx+35, cruzy+35))
    pygame.draw.line(fundo, black, (cruzx+35, cruzy), ( cruzx, cruzy+35))

def cerca():
    pygame.draw.line(fundo, black,(106, 0), (106, altura))
    pygame.draw.line(fundo, black,(212, 0), (212, altura))
    pygame.draw.line(fundo, black,(0, 106), (largura, 106))
    pygame.draw.line(fundo, black,(0, 212), (largura, 212))

def endgame():
    global fimdejogo
    global resultado
    global trava
    if matriz[0] == 1 and matriz[1] == 1 and matriz[2] == 1 or matriz[0] == 2 and matriz[1] == 2 and matriz[2] == 2:
        fimdejogo = True
        trava = False
        if matriz[0] == 1:
            resultado = 1
        else:
            resultado = 2
    if matriz[3] == 1 and matriz[4] == 1 and matriz[5] == 1 or matriz[3] == 2 and matriz[4] == 2 and matriz[5] == 2:
        fimdejogo = True
        trava = False
        if matriz[3] == 1:
            resultado = 1
        else:
            resultado = 2
    if matriz[6] == 1 and matriz[7] == 1 and matriz[8] == 1 or matriz[6] == 2 and matriz[7] == 2 and matriz[8] == 2:
        fimdejogo = True
        trava = False
        if matriz[6] == 1:
            resultado = 1
        else:
            resultado = 2
    if matriz[0] == 1 and matriz[3] == 1 and matriz[6] == 1 or matriz[0] == 2 and matriz[3] == 2 and matriz[6] == 2:
        fimdejogo = True
        trava = False
        if matriz[6] == 1:
            resultado = 1
        else:
            resultado = 2
    if matriz[1] == 1 and matriz[4] == 1 and matriz[7] == 1 or matriz[1] == 2 and matriz[4] == 2 and matriz[7] == 2:
        fimdejogo = True
        trava = False
        if matriz[1] == 1:
            resultado = 1
        else:
            resultado = 2
    if matriz[2] == 1 and matriz[5] == 1 and matriz[8] == 1 or matriz[2] == 2 and matriz[5] == 2 and matriz[8] == 2:
        fimdejogo = True
        trava = False
        if matriz[2] == 1:
            resultado = 1
        else:
            resultado = 2
    if matriz[0] == 1 and matriz[4] == 1 and matriz[8] == 1 or matriz[0] == 2 and matriz[4] == 2 and matriz[8] == 2:
        fimdejogo = True
        trava = False
        if matriz[0] == 1:
            resultado = 1
        else:
            resultado = 2
    if matriz[2] == 1 and matriz[4] == 1 and matriz[6] == 1 or matriz[2] == 2 and matriz[4] == 2 and matriz[6] == 2:
        fimdejogo = True
        trava = False
        if matriz[2] == 1:
            resultado = 1
        else:
            resultado = 2

    vaziu = 0
    for c in range(0, len(matriz)):
        if matriz[c] == 0:
            vaziu +=1
    if vaziu == 0:
        if resultado != 1 and resultado != 2:
            fimdejogo = True
            resultado = 3
    vaziu = 0

game = True
fimdejogo = False
evento = True
trava = True
resultado = 0
mousex = -1
mousey = 0
fundo.fill(white)
cerca()
matriz = [0, 0, 0, 0, 0, 0, 0, 0, 0]
pygame.display.update()
while game:
    while fimdejogo:
        sleep(0.5)
        fundo.fill(white)
        texto('Fim de Jogo', red, 50, 65, 30)
        if resultado == 1:
            texto('Vitoria!!!', black, 30, 70, 80)
        if resultado == 3:
            texto('Velha', black, 30, 70, 80)
        if resultado == 2:
            texto('Derrota!!', black, 30, 70, 80)
        pygame.draw.rect(fundo, black, [45, 120, 135, 27])
        texto('Continuar(C)', white, 30, 50, 125)
        pygame.draw.rect(fundo, black, [190, 120, 75, 27])
        texto('Sair(S)', white, 30, 195, 125)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                fimdejogo = False
                trava = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                        game = True
                        fimdejogo = False
                        evento = True
                        trava = True
                        resultado = 0
                        mousex = -1
                        mousey = 0
                        fundo.fill(white)
                        cerca()
                        matriz = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                        pygame.display.update()
                if event.key == pygame.K_s:
                    game = False
                    fimdejogo = False
                    evento = False
                    trava = False


    while evento:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                evento = False
                trava = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex = pygame.mouse.get_pos()[0]
                mousey = pygame.mouse.get_pos()[1]
                evento = False

    evento = True
            
    if mousex < 106 and mousey < 106 and mousex != -1 and matriz[0] == 0:
        cruz(35, 35)
        matriz[0] = 1
    if mousex < 212 and mousex > 106 and mousey < 106 and matriz[1] == 0:
        cruz(141, 35)
        matriz[1] = 1
    if mousex < 320 and mousex > 212 and mousey < 106 and matriz[2] == 0:
        cruz(247, 35)
        matriz[2] = 1
    if mousex < 106 and mousey > 106 and mousey < 212 and matriz[3] == 0:
        cruz(35, 141)
        matriz[3] = 1
    if mousex < 212 and mousex > 106 and mousey < 212 and mousey > 106 and matriz[4] == 0:
        cruz(141, 141)
        matriz[4] = 1
    if mousex < 320 and mousex > 212 and mousey < 212 and mousey > 106 and matriz[5] == 0:
        cruz(247, 141)
        matriz[5] = 1
    if mousex < 106 and mousey < 320 and mousey > 212 and matriz[6] == 0:
        cruz(35, 247)
        matriz[6] = 1
    if mousex < 212 and mousex > 106 and mousey < 320 and mousey > 212 and matriz[7] == 0:
        cruz(141, 247)
        matriz[7] = 1
    if mousex < 320 and mousex > 212 and mousey < 320 and mousey > 212 and matriz[8] == 0:
        cruz(247, 247)
        matriz[8] = 1

    endgame()

    pygame.display.update()

    sleep(0.5)
    if trava:
        while True:
            jogada = random.randint(0, 8)
            if matriz[jogada] == 0:
                circulo(jogada)
                matriz[jogada] = 2
                break
            else:
                if 0 in matriz:
                    jogada = random.randint(0, 8)
                else:
                    break

    endgame()
    
    pygame.display.update()

pygame.display.update()
