import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Definir constantes
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colores para usar
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Configurar la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego con Menús")

# Definir fuente
font = pygame.font.Font(None, 36)

class Player(pygame.sprite.Sprite):
    def __init__(self,size):
        super().__init__()
        imagen = pygame.image.load('player.png').convert_alpha()
        self.image = pygame.transform.scale(imagen, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.rect.x += 5
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pygame.K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += 5

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            # Reiniciar en la parte superior cuando el enemigo sale de la pantalla
            self.rect.y = 0
            self.rect.x = random.randint(0, WIDTH)

# Crear grupo de sprites para el jugador
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player(50)
all_sprites.add(player)

# Configurar el reloj
clock = pygame.time.Clock()
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
        
        draw_text("Menú Principal", WIDTH // 2, HEIGHT // 4)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Botón Jugar
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 100, 200, 200, 50))
        if WIDTH // 2 - 100 <= mouse_x <= WIDTH // 2 + 100 and 200 <= mouse_y <= 250:
            pygame.draw.rect(screen, (200, 200, 200), (WIDTH // 2 - 100, 200, 200, 50))
            if pygame.mouse.get_pressed()[0]:
                difficulty_menu()
                print("Jugar")
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
        print("Dificultad")
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
        draw_text("Fácil", WIDTH // 2, 225)

        # Botón Medio
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 100, 300, 200, 50))
        if WIDTH // 2 - 100 <= mouse_x <= WIDTH // 2 + 100 and 300 <= mouse_y <= 350:
            pygame.draw.rect(screen, (200, 200, 200), (WIDTH // 2 - 100, 300, 200, 50))
            if mouse_pressed:
                start_game(2)
        draw_text("Medio", WIDTH // 2, 325)

        # Botón Difícil
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 100, 400, 200, 50))
        if WIDTH // 2 - 100 <= mouse_x <= WIDTH // 2 + 100 and 400 <= mouse_y <= 450:
            pygame.draw.rect(screen, (200, 200, 200), (WIDTH // 2 - 100, 400, 200, 50))
            if mouse_pressed:
                start_game(3)
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

        screen.fill(ORANGE)
        draw_text("Controles", WIDTH // 2, HEIGHT // 4)
        draw_text("Mover Arriba: W", WIDTH // 2, HEIGHT // 2)
        draw_text("Mover Abajo: S", WIDTH // 2, HEIGHT // 2+30)
        draw_text("Mover Derecha: D", WIDTH // 2, HEIGHT // 2+60)
        draw_text("Mover Izquierda: A", WIDTH // 2, HEIGHT // 2+90)
        draw_text("Atras: ESC", WIDTH - 80 , HEIGHT - 20) 

        pygame.display.flip()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return  # Volver al menú principal

# Función para iniciar el juego
def start_game(difficulty):
    # Aquí se implementaría el código del juego con la dificultad seleccionada
    print(f"Iniciar juego con dificultad: {difficulty}")
    start_time = pygame.time.get_ticks()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if random.randint(0, 100) < 1:
            enemy = Enemy(random.randint(0, WIDTH), 0, difficulty * 1)
            all_sprites.add(enemy)
            enemies.add(enemy)
        
        # Actualizar sprites
        all_sprites.update()
        enemies.update()
        
        score = (pygame.time.get_ticks() - start_time) // 1000 
        
        score_text = font.render(f"Puntaje: {score}", True, (0, 255, 255))
        screen.blit(score_text, (10, 10))
        
        if pygame.sprite.spritecollide(player, enemies, False):
            print("¡Has perdido!")
                        
            screen.fill((0, 0, 0))
            
            # Dibujar el puntaje en la pantalla
            score_text = font.render(f"Puntaje: {score}", True, (255, 255, 255))
            screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - score_text.get_height() // 2))

            # Actualizar la pantalla
            pygame.display.flip()

            pygame.time.wait(4000)
            
            running = False
        
        
        # Limpiar pantalla
        screen.fill((0, 0, 0))


        # Dibujar sprites en la pantalla
        all_sprites.draw(screen)


        score_text = font.render(f"Puntaje: {score}", True, (0, 255, 255))
        screen.blit(score_text, (10, 10))
        
        # Actualizar la pantalla
        pygame.display.flip()

        # Establecer límite de FPS
        clock.tick(FPS)

    return

# Bucle principal del menú principal
main_menu()
