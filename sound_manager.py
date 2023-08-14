import pygame


pygame.mixer.init()

# интерфейс
screen_path = 'sound/locations/intro.mp3'
screen_mp3 = pygame.mixer.Sound(screen_path)
button_path = 'sound/sound_effects/button.ogg'
button_wav = pygame.mixer.Sound(button_path)

# музыка на локациях
room_1_mp3_path = 'sound/locations/room_1.ogg'
room_1_mp3 = pygame.mixer.Sound(room_1_mp3_path)
room_2_mp3_path = 'sound/locations/room_2.ogg'
room_2_mp3 = pygame.mixer.Sound(room_2_mp3_path)
room_1_again_path = 'sound/locations/room_1_again.ogg'
room_1_2 = pygame.mixer.Sound(room_1_again_path)

# музыка на видениях
sight_1_path = 'sound/locations/sight_1.ogg'
sight_1 = pygame.mixer.Sound(sight_1_path)
sight_2_path = 'sound/locations/sight_2.ogg'
sight_2 = pygame.mixer.Sound(sight_2_path)
sight_3_path = 'sound/locations/sight_3.ogg'
sight_3 = pygame.mixer.Sound(sight_3_path)

# обвал и смерть
dd_mp3_path = 'sound/locations/danger_death.ogg'
dd_mp3 = pygame.mixer.Sound(dd_mp3_path)

# музыка в эпилогах
best_final_path = 'sound/endings/best.ogg'
best_final = pygame.mixer.Sound(best_final_path)
neutral_1_final_path = 'sound/endings/neutral_1.ogg'
neutral_1_final = pygame.mixer.Sound(neutral_1_final_path)
neutral_2_final_path = 'sound/endings/neutral_2.ogg'
neutral_2_final = pygame.mixer.Sound(neutral_2_final_path)
neutral_3_final_path = 'sound/endings/neutral_3.ogg'
neutral_3_final = pygame.mixer.Sound(neutral_3_final_path)
worst_final_path = 'sound/endings/worst.ogg'
worst_final = pygame.mixer.Sound(worst_final_path)
