import pygame
import time

def run_intro():
    # Initialize pygame
    pygame.init()

    # Screen dimensions
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mr. CrackBot AI Nano")

    # Colors
    black = (0, 0, 0)
    blue = (0, 0, 255)

    # Load image (ensure image is in the correct folder)
    image = pygame.image.load("docs/screenshots/mrcatbar2.webp")  # Updated with your file
    image = pygame.transform.scale(image, (screen_width, screen_height))

    # Font
    font = pygame.font.Font(None, 74)

    # Text
    text = font.render("Mr. CrackBot AI Nano", True, blue)
    text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2 + 50))

    # Animation loop
    running = True
    alpha = 0
    fade_in = True

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw background
        screen.fill(black)

        # Draw image
        screen.blit(image, (0, 0))

        # Animate text
        if fade_in:
            alpha += 5
            if alpha >= 255:
                fade_in = False
        else:
            alpha -= 5
            if alpha <= 0:
                fade_in = True

        # Apply alpha to text
        text_surface = text.copy()
        text_surface.set_alpha(alpha)

        # Blit text
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(30)

        # End intro after a certain time
        if time.time() - pygame.time.get_ticks() / 1000 > 10:  # 10 seconds
            running = False

    pygame.quit()

if __name__ == "__main__":
    run_intro()