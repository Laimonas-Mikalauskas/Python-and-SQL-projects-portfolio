# Main menu for Sci-fi FPS game

import pygame
pygame.init()


# Set up display
surface = pygame.display.set_mode((2560, 1600))
pygame.display.set_caption('Sci-fi FPS Main Menu')
font = pygame.font.SysFont(None, 95)
clock = pygame.time.Clock()

# Menu options
menu_options = ['The Story', 'Campaign Mode', 'Multiplayer Mode', 'Settings', 'Rate Us', 'Follow Us', 'Exit']
selected_option = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        running = False
        

def draw_menu():
    surface.fill((1, 1, 1))
    for i, option in enumerate(menu_options):
        gap = 1900
        color = (0, 0, 255) if i == selected_option else (255, 255, 255)
        text = font.render(option, True, color)
        surface.blit(text, (300, 150 + i * 60))
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        print(f'Selected: {menu_options[selected_option]}')
    
    draw_menu()
    clock.tick(30)

    

            

