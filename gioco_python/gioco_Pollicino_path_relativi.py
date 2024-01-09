import pygame #libreria
from sys import exit #necessario per chiudere il programma senza problemi
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('immagini/player/player_camminata1.png').convert_alpha()
        player_walk_2 = pygame.image.load('immagini/player/player_camminata2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('immagini/player/player_salto.png').convert_alpha()
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('suoni/jump.mp3')
        self.jump_sound.set_volume(0.6)
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 304:
            self.jump_sound.play()
            self.gravity = -20
    def apply_gravity(self):
        self.gravity += 1
        self.rect.bottom += self.gravity
        if self.rect.bottom >= 304:
            self.rect.bottom = 304
    def animations(self):
        if self.rect.bottom < 304:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animations()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'fly':
            fly_1 = pygame.image.load('immagini/mosca/mosca.png').convert_alpha()
            fly_2 = pygame.image.load('immagini/mosca/mosca2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load('immagini/Lumaca/Lumaca.png').convert_alpha()
            snail_2 = pygame.image.load('immagini/Lumaca/Lumaca2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def animations(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    
    def destroy(self):
        if self.rect.right <= -10:
            self.kill()

    def update(self, speed):
        self.animations()
        self.rect.right -= speed
        self.destroy()

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f"Punteggio:{current_time}", False, (255,140,0))
    score_rectangle = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rectangle)
    #print(current_time)
    return current_time

'''def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.right -= 5
            if obstacle_rect.bottom == 304:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.right > -100]#elimina tutti gli elementi usciti dallo schermo
        return obstacle_list
    else:
        return []'''

'''def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True'''
pygame.mixer.init()
fail_sound = pygame.mixer.Sound('suoni/Fail.mp3')
def collisions_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        fail_sound.play()
        obstacle_group.empty()
        return False
    else:
        return True
    
'''def player_animation():
    global player_surface, player_index

    if player_rectangle.bottom < 304:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]'''
        
pygame.init() #necessario per ogni programma che usa pygame
screen = pygame.display.set_mode((800, 400)) #schermo
pygame.display.set_caption("Pollicino's game") #cambia il nome della finestra
clock = pygame.time.Clock()
test_font = pygame.font.Font('Font/Gumball.TTF', 50) #font
game_active = False
start_time = 0
score = 0
#obstacles = 1
speed = 5

bg_music = pygame.mixer.Sound('suoni/BgMusic.mp3')
bg_music.set_volume(0.6)
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()
'''test_surface = pygame.Surface((100, 200)) #creo una superficie
test_surface.fill('Red') #la coloro'''

sky_surface = pygame.image.load('immagini/Test_cielo_corretto.xcf').convert()
ground_surface = pygame.image.load('immagini/Terreno.png').convert()

#score_surface = test_font.render('il mio gioco', False, 'Black')
'''score_surface = test_font.render('il mio gioco', False, (255,140,0))
score_rectangle = score_surface.get_rect(center = (400, 50))'''

#ostacoli
'''snail_frame_1 = pygame.image.load('D:\sistemi_e_reti\python\giochi\immagini\Lumaca\Lumaca.png').convert_alpha()
snail_frame_2 = pygame.image.load('D:\sistemi_e_reti\python\giochi\immagini\Lumaca\Lumaca2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]'''
#snail_rectangle = snail_surface.get_rect(midbottom = (770, 304))
#snail_x_pos = 600

'''fly_frame_1 = pygame.image.load('D:\sistemi_e_reti\python\giochi\immagini\mosca\mosca.png').convert_alpha()
fly_frame_2 = pygame.image.load('D:\sistemi_e_reti\python\giochi\immagini\mosca\mosca2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]'''

#obstacle_rect_list = []

'''player_walk_1 = pygame.image.load('D:\sistemi_e_reti\python\giochi\immagini\player\player_camminata1.png').convert_alpha()
player_walk_2 = pygame.image.load('D:\sistemi_e_reti\python\giochi\immagini\player\player_camminata2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('D:\sistemi_e_reti\python\giochi\immagini\player\player_salto.png').convert_alpha()
player_surface = player_walk[player_index]
player_rectangle = player_surface.get_rect(midbottom = (80, 304))'''

#player_gravity = 0 #simula la gravità

#menù iniziale
player_stand = pygame.image.load('immagini/player/player_fermo.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2) #ingrandisce l'immagine
player_stand_rectangle = player_stand.get_rect(center = (400, 200)) #creo il rettangolo
#nome del videogioco
game_name = test_font.render('Snail Jumper', False, '#ffff00')
game_name_rectangle = game_name.get_rect(center = (400, 80))
#messaggio che spiega come iniziare a giocare
game_message = test_font.render('Premi lo spazio per giocare', False, '#ffff00')
game_message = pygame.transform.rotozoom(game_message, 0, 0.7) #rimpiciolisco la scritta per farcela stare
game_message_rectangle = game_message.get_rect(center = (400, 340))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)
speed_timer = pygame.USEREVENT + 2
pygame.time.set_timer(speed_timer, 8000)
'''obstacle_number = pygame.USEREVENT + 3
pygame.time.set_timer(obstacle_number, 15000)'''
'''snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)
fly_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(fly_animation_timer, 200)'''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #chiude la finestra
            exit() #chiude il programma
        if game_active:
            
            '''if event.type == pygame.KEYDOWN: #controlla se premo il tasto
                if event.key == pygame.K_SPACE: #controlla se è lo spazio
                    if player.rect.bottom == 304:#controlla se è per terra per non permettere lo spam del salto
                        player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN: #controlla se si clicca un tasto del mouse
                if player.rect.collidepoint(event.pos): #controlla se il mouse è sul personaggio
                    if player.rect.bottom == 304:
                        player_gravity = -20'''
            '''if event.type == obstacle_number:
                obstacles += 1'''
            if event.type == speed_timer:
                speed += 1
            if event.type == obstacle_timer:
                #for _ in range (0, obstacles):
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail']))) #aumento la probabilità che compaia una lumaca al posto di una mosca
                '''if randint(0, 2):
                    obstacle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900, 1100), 304)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(midbottom = (randint(900, 1100), 210)))'''
            '''if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]
            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]'''
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                bg_music.play(loops = -1)
                #snail_rectangle.right = 810
                start_time = int(pygame.time.get_ticks() / 1000)

        '''if event.type == pygame.MOUSEMOTION: #se si muove il mouse
            print(event.pos) #stampa la posizione del mouse'''
        '''if event.type == pygame.MOUSEBUTTONUP:
            print(event.pos)'''
        '''if event.type == pygame.MOUSEMOTION:
            if player_rectangle.collidepoint(event.pos):
                print(1)'''
        
        
    #gioco
    if game_active:
        screen.blit(sky_surface, (0, 0)) #disegno il cielo
        screen.blit(ground_surface, (0, 300)) #disegno il terreno
        '''pygame.draw.rect(screen, '#c0e8ec', score_rectangle)
        pygame.draw.rect(screen, "#c0e8ec", score_rectangle, 10)
        screen.blit(score_surface, score_rectangle)'''
        score = display_score()
        #pygame.draw.line(screen, 'Gold', (0, 0), (800, 400), 10) #diagonale
        #pygame.draw.line(screen, 'Gold', (0, 0), pygame.mouse.get_pos(), 10) #linea che segue il mouse
        #pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50, 200, 100, 100)) #disegna un cerchio
        
        #screen.blit(snail_surface, snail_rectangle)
        #player_rectangle.left += 1
        '''player_gravity += 1
        player.rect.bottom += player_gravity
        if player.rect.bottom >= 304:
            player.rect.bottom = 304
        screen.blit(player_surface, player_rectangle)'''
        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update(speed)
        #movimento degli ostacoli
        #obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        #collisioni
        game_active = collisions_sprite()
        #game_active = collisions(player_rectangle, obstacle_rect_list)
        #snail_x_pos -= 4 #sposta a sinistra
        '''if snail_x_pos < -100:
            snail_x_pos = 800 #rimetto la tartaruga a destra'''
        '''snail_rectangle.right -= 5
        if snail_rectangle.right <= 0:
            snail_rectangle.right = 810'''

        '''if player_rectangle.colliderect(snail_rectangle):#controlla le collisioni
            game_active = False'''

        '''keys = pygame.key.get_pressed() #salva la situazione di tutti i tasti
        if keys[pygame.K_SPACE]:#controlla se lo spazio è premuto
            print('jump')'''
        
        '''mouse_pos = pygame.mouse.get_pos()
        if player_rectangle.collidepoint(mouse_pos): #vedere se si punta sul giocatore
            print(pygame.mouse.get_pressed()) #vedere i tasti premuti'''
    else:
        #obstacle_rect_list.clear()#cancella la lista degli ostacoli impedendo a vari bug di avvenire
        #player_rectangle.midbottom = (80, 304)
        #player_gravity = 0
        speed = 5
        bg_music.stop()
        screen.fill('#4c9141')
        screen.blit(player_stand, player_stand_rectangle)
        score_message = test_font.render(f'Il tuo ultimo punteggio: {score}', False, '#ffff00')
        score_message = pygame.transform.rotozoom(score_message, 0, 0.75)
        score_message_rectangle = score_message.get_rect(center = (400, 340))
        screen.blit(game_name, game_name_rectangle)
        if score == 0:
            screen.blit(game_message, game_message_rectangle)
        else:
            screen.blit(score_message, score_message_rectangle)


    pygame.display.update() #aggiorna lo schermo facendo i cambiamenti necessari
    clock.tick(60) #limite 60 fps