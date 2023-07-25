import pygame


pygame.mixer.init()

# интерфейс
screen_path = 'sound/locations/intro.mp3'
screen_mp3 = pygame.mixer.Sound(screen_path)
button_path = 'sound/sound_effects/button.wav'
button_wav = pygame.mixer.Sound(button_path)

# музыка на локациях
room_1_mp3_path = 'sound/locations/room_1.wav'
room_1_mp3 = pygame.mixer.Sound(room_1_mp3_path)
room_2_mp3_path = 'sound/locations/room_2.wav'
room_2_mp3 = pygame.mixer.Sound(room_2_mp3_path)
room_1_again_path = 'sound/locations/room_1_again.mp3'
room_1_2 = pygame.mixer.Sound(room_1_again_path)

# музыка на видениях
sight_1_path = 'sound/locations/sight_1.mp3'
sight_1 = pygame.mixer.Sound(sight_1_path)
sight_2_path = 'sound/locations/sight_2.mp3'
sight_2 = pygame.mixer.Sound(sight_2_path)
sight_3_path = 'sound/locations/sight_3.mp3'
sight_3 = pygame.mixer.Sound(sight_3_path)

# обвал и смерть
dd_mp3_path = 'sound/locations/danger_death.wav'
dd_mp3 = pygame.mixer.Sound(dd_mp3_path)

# музыка в эпилогах
best_final_path = 'sound/endings/best.mp3'
best_final = pygame.mixer.Sound(best_final_path)
neutral_1_final_path = 'sound/endings/neutral_1.mp3'
neutral_1_final = pygame.mixer.Sound(neutral_1_final_path)
neutral_2_final_path = 'sound/endings/neutral_2.mp3'
neutral_2_final = pygame.mixer.Sound(neutral_2_final_path)
neutral_3_final_path = 'sound/endings/neutral_3.mp3'
neutral_3_final = pygame.mixer.Sound(neutral_3_final_path)
worst_final_path = 'sound/endings/worst.mp3'
worst_final = pygame.mixer.Sound(worst_final_path)
