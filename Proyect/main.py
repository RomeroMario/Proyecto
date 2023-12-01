import pygame
import sys
import random
from variables import *
from jugador import Player
from enemigo import Enemy

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego con Menús")

# Definir fuente
font = pygame.font.Font(None, 36)

# Crear grupo de sprites para el jugador
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player(50)
all_sprites.add(player)

# Configurar el reloj
clock = pygame.time.Clock()
max_score = 0

# Función para mostrar texto en la pantalla
def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Función para mostrar el menú principal
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(ORANGE)
        
        draw_text("Atras: ESC", WIDTH - 80 , HEIGHT - 20) 
        draw_text(f"MaxScore: {max_score}",  80 ,  20) 
        draw_text("Menú Principal", WIDTH // 2, HEIGHT // 4)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Botón Jugar
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 100, 200, 200, 50))
        if WIDTH // 2 - 100 <= mouse_x <= WIDTH // 2 + 100 and 200 <= mouse_y <= 250:
            pygame.draw.rect(screen, (200, 200, 200), (WIDTH // 2 - 100, 200, 200, 50))
            if pygame.mouse.get_pressed()[0]:
                difficulty_menu()
        draw_text("Jugar", WIDTH // 2, 225)

        # Botón Ayuda
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 100, 300, 200, 50))
        if WIDTH // 2 - 100 <= mouse_x <= WIDTH // 2 + 100 and 300 <= mouse_y <= 350:
            pygame.draw.rect(screen, (200, 200, 200), (WIDTH // 2 - 100, 300, 200, 50))
            if pygame.mouse.get_pressed()[0]:
                show_controls()
        draw_text("Ayuda", WIDTH // 2, 325)

        # Botón Salir
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 100, 400, 200, 50))
        if WIDTH // 2 - 100 <= mouse_x <= WIDTH // 2 + 100 and 400 <= mouse_y <= 450:
            pygame.draw.rect(screen, (200, 200, 200), (WIDTH // 2 - 100, 400, 200, 50))
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()
        draw_text("Salir", WIDTH // 2, 425)

        pygame.display.flip()

# Función para mostrar el menú de dificultad
def difficulty_menu():
    mouse_pressed = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = True

        screen.fill(ORANGE)
        draw_text("Atras: ESC", WIDTH - 80 , HEIGHT - 20) 
        draw_text("Selecciona Dificultad", WIDTH // 2, HEIGHT // 4)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Botón Fácil
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 100, 200, 200, 50))
        if WIDTH // 2 - 100 <= mouse_x <= WIDTH // 2 + 100 and 200 <= mouse_y <= 250:
            pygame.draw.rect(screen, (200, 200, 200), (WIDTH // 2 - 100, 200, 200, 50))
            if mouse_pressed:
                start_game(1)
                return
        draw_text("Fácil", WIDTH // 2, 225)

        # Botón Medio
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 100, 300, 200, 50))
        if WIDTH // 2 - 100 <= mouse_x <= WIDTH // 2 + 100 and 300 <= mouse_y <= 350:
            pygame.draw.rect(screen, (200, 200, 200), (WIDTH // 2 - 100, 300, 200, 50))
            if mouse_pressed:
                start_game(2)
                return
        draw_text("Medio", WIDTH // 2, 325)

        # Botón Difícil
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 100, 400, 200, 50))
        if WIDTH // 2 - 100 <= mouse_x <= WIDTH // 2 + 100 and 400 <= mouse_y <= 450:
            pygame.draw.rect(screen, (200, 200, 200), (WIDTH // 2 - 100, 400, 200, 50))
            if mouse_pressed:
                start_game(3)
                return
        draw_text("Difícil", WIDTH // 2, 425)

        pygame.display.flip()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return  # Volver al menú principal

# Función para mostrar los controles
def show_controls():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.update()  # Llama a la función update de la clase Player

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            return  # Volver al menú principal

        screen.fill(ORANGE)
        draw_text("Controles", WIDTH // 2, HEIGHT // 4)
        draw_text("Mover Arriba: W", WIDTH // 2, HEIGHT // 2)
        draw_text("Mover Abajo: S", WIDTH // 2, HEIGHT // 2+30)
        draw_text("Mover Derecha: D", WIDTH // 2, HEIGHT // 2+60)
        draw_text("Mover Izquierda: A", WIDTH // 2, HEIGHT // 2+90)
        draw_text("Atras: ESC", WIDTH - 80 , HEIGHT - 20) 

        # Dibujar sprites en la pantalla
        all_sprites.draw(screen)
        
        pygame.display.flip()
        
        clock.tick(FPS)

# Función para iniciar el juego
def start_game(difficulty):
    # Aquí se implementaría el código del juego con la dificultad seleccionada
    print(f"Iniciar juego con dificultad: {difficulty}")
    start_time = pygame.time.get_ticks()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        
        if random.randint(0, 100) < 2.5*difficulty:
            enemy = Enemy(random.randint(0, WIDTH), 0, difficulty * 1)
            all_sprites.add(enemy)
            enemies.add(enemy)
        
        # Actualizar sprites
        all_sprites.update()
        enemies.update()
        
        if pygame.sprite.spritecollide(player, enemies, False):
            print("¡Has perdido!")
                        
            screen.fill((0, 0, 0))
            
            # Dibujar el puntaje en la pantalla
            score_text = font.render(f"Puntaje: {score}", True, (255, 255, 255))
            screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - score_text.get_height() // 2))

            print(f"Puntiaje: {score}")
            global max_score
            if score > max_score:
                max_score = score
            #Quitamos todos los enemigos
            for e in enemies:
                e.kill()
            
            #Reiniciamos el jugador
            player.rect.center = (WIDTH // 2, HEIGHT // 2)
            
            # Actualizar la pantalla
            pygame.display.flip()

            # Esperar 4 segundos antes de salir
            pygame.time.wait(4000)
            
            break
        
        
        # Limpiar pantalla
        screen.fill((0, 0, 0))

        # Dibujar sprites en la pantalla
        all_sprites.draw(screen)

        score = (pygame.time.get_ticks() - start_time) // 1000 
        score_text = font.render(f"Puntaje: {score}", True, GREEN)
        screen.blit(score_text, (10, 10))
        
        # Actualizar la pantalla
        pygame.display.flip()

        # Salir del juego si se presiona ESC
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            break  # Volver al menú principal
        
        # Establecer límite de FPS
        clock.tick(FPS)

    return

# Bucle principal del menú principal
main_menu()
