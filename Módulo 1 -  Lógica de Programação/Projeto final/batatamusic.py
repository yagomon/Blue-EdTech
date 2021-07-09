

def musica():
    import pygame

    pygame.init()

    pygame.mixer.music.load('batatamusic.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)

    clock = pygame.time.Clock()
    clock.tick(10)

    
