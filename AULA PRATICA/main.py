import pygame
from pygame import Surface, Rect

W_WIDTH = 576
W_HEIGHT = 324
# Inicializar o modulo Pygame
pygame.init()
print('setup start')
# Criação janela pygame
window : Surface = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))

# carregar imagem e gerar uma superfície
bg_surf: Surface = pygame.image.load('./assents/bg.png').convert_alpha()
player_surf: Surface = pygame.image.load('./assents/player1.png').convert_alpha()

#Obter retângulo da superfície
bg_rect: Rect = bg_surf.get_rect(left=0, top=0)
player_rect: Rect = player_surf.get_rect(left=100, top=100)

# Desenhar na janela
window.blit(source=bg_surf, dest=(bg_rect))
window.blit(source=player_surf, dest=(player_rect))

#Atualizar a janela
pygame.display.flip()

# Carregar som e deixar tocando
pygame.mixer_music.load('./assents/fase1.mp3')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.7)

# Colocar um relogio no jogo

clock = pygame.time.Clock()
print('setup end')
print('loop start')

while True:
    clock.tick(140) # Limitado o FPS no Loop
    # print(f'{clock.get_fps() :.0f}') #Print para verificar o valor do FPS
    window.blit(source=bg_surf, dest=(bg_rect))
    window.blit(source=player_surf, dest=(player_rect))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        player_rect.centery -= 1
    if pressed_key[pygame.K_s]:
        player_rect.centery += 1
    if pressed_key[pygame.K_d]:
        player_rect.centerx += 1
    if pressed_key[pygame.K_a]:
        player_rect.centerx -= 1
        pass
