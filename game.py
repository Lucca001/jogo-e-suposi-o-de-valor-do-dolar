import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo de Chutes ao Gol")

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

# Posição e tamanho do gol
goal_x = screen_width // 2 - 50
goal_y = screen_height - 50
goal_width = 100
goal_height = 20

# Posição e tamanho da bola
ball_radius = 15
ball_x = random.randint(ball_radius, screen_width - ball_radius)
ball_y = ball_radius + 20
ball_speed_x = 5
ball_speed_y = 5

# Posição e tamanho do jogador
player_width = 100
player_height = 20
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10

# Loop do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 20
            elif event.key == pygame.K_RIGHT:
                player_x += 20
            elif event.key == pygame.K_SPACE and ball_speed_y == 0:
                ball_speed_y = -5
    
    # Mover a bola
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Verificar colisões com as bordas
    if ball_x <= ball_radius or ball_x >= screen_width - ball_radius:
        ball_speed_x *= -1
    
    if ball_y <= ball_radius:
        ball_speed_y *= -1
    
    # Verificar colisão com o gol
    if ball_x >= goal_x and ball_x <= goal_x + goal_width and ball_y >= goal_y:
        print("Gol!")
        ball_speed_y *= -1
        ball_y = goal_y - ball_radius
    
    # Verificar colisão com o jogador
    if (ball_y + ball_radius >= player_y) and (ball_y + ball_radius <= player_y + player_height) and (ball_x >= player_x) and (ball_x <= player_x + player_width):
        ball_speed_y *= -1
    
    # Limpar a tela
    screen.fill(white)
    
    # Desenhar o gol
    pygame.draw.rect(screen, black, (goal_x, goal_y, goal_width, goal_height))
    
    # Desenhar a bola
    pygame.draw.circle(screen, black, (ball_x, ball_y), ball_radius)
    
    # Desenhar o jogador do Barcelona
    pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))
    
    # Atualizar a tela
    pygame.display.update()
    
    # Controlar a taxa de atualização
    pygame.time.delay(20)

# Encerrar o Pygame
pygame.quit()
sys.exit()