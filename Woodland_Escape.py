import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        hero_walk_1 = pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/Character/walking22.png').convert_alpha()
        hero_walk_2 = pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/Character/walking8.png').convert_alpha()
        self.hero_walk = [hero_walk_1,hero_walk_2]
        self.player_index = 0
        self.hero_jump = pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/Character/Jump1.png').convert_alpha()
        
        self.image = self.hero_walk[self.player_index]
        self.rect = self.image.get_rect(topleft = (150,550))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 850:
            self.gravity = -28

    def apply_gravity(self):
        self.gravity += 0.8
        self.rect.y += self.gravity
        if self.rect.bottom >= 850:
            self.rect.bottom = 850

    def animation_state(self):
        if self.rect.bottom < 850:
            self.image = self.hero_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.hero_walk):self.player_index = 0
            self.image = self.hero_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'goblin':
            goblin_1 = pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/Enemy/Orc0.png').convert_alpha()
            goblin_2 = pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/Enemy/Orc1.png').convert_alpha()
            self.frames = [goblin_1,goblin_2]
            y_pos = 300
        else:
            Ogre_1= pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/Enemy/ogre0 copy.png').convert_alpha()
            Ogre_2= pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/Enemy/)gre_1_copy.png').convert_alpha()
            self.frames = [Ogre_1,Ogre_2]
            y_pos = 575

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(topleft = (randint(2000,2300),y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 11
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
                self.kill()

def display_score():
    current_time = int(pygame.time.get_ticks() / 100) - start_time
    score_surf = test_font.render(f'Score: {current_time}', True, (64,64,64))
    score_rect = score_surf.get_rect(topleft = (720,135))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 9

            if obstacle_rect.top == 575: screen.blit(Ogre_surf,obstacle_rect)
            else: screen.blit(goblin_surf,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def collision_sprite():
        if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
            obstacle_group.empty()
            return False
        else: return True


def hero_animation():
    global hero_surface, player_index

    if hero_rect.bottom < 850:
        hero_surface = hero_jump
    else:
        player_index += 0.1
        if player_index >= len(hero_walk):player_index = 0
        hero_surface = hero_walk[int(player_index)]


pygame.init()
screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 135)
game_active = False
start_time = 0
score = 0

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

start_screen = pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/background_1.png').convert_alpha()
sky_surface = pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/sky.png').convert_alpha()
ground_surface = pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/ground.png').convert_alpha()

# Intro Screen
hero_stand = pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/Character/start_pic.png').convert_alpha()
hero_stand = pygame.transform.scale(hero_stand,(325,450))
hero_stand_rect = hero_stand.get_rect(center = (960,465))

score_surf = test_font.render('                    ', True, 'Black')
score_rect = score_surf.get_rect(topleft = (700,135))

#Ogre
Ogre_frame_1= pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/Enemy/ogre0 copy.png').convert_alpha()
Ogre_frame_2= pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/Enemy/)gre_1_copy.png').convert_alpha()
Ogre_frames = [Ogre_frame_1,Ogre_frame_2]
Ogre_frame_index = 0
Ogre_surf = Ogre_frames[Ogre_frame_index]

#goblin
goblin_frame_1 = pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/Enemy/Orc0.png').convert_alpha()
goblin_frame_2 = pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/Enemy/Orc1.png').convert_alpha()
goblin_frames = [goblin_frame_1,goblin_frame_2]
goblin_frame_index = 0
goblin_surf = goblin_frames[goblin_frame_index]

obstacle_rect_list = []

#Hero
hero_walk_1 = pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/Character/walking22.png').convert_alpha()
hero_walk_2 = pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/Character/walking8.png').convert_alpha()
hero_walk = [hero_walk_1,hero_walk_2]
player_index = 0
hero_jump = pygame.image.load('/Users/mitchcampos/Documents/Python Projects/Runner/Graphics/Character/Jump1.png').convert_alpha()
hero_surface = hero_walk[player_index]
hero_rect = hero_surface.get_rect(topleft = (150,550))
player_grav = 0


game_name = test_font.render('Woodland Escape',True, 'Black')
game_name_rect = game_name.get_rect(center = (960,135))

game_message = test_font.render('Press space to run', True, 'Black')
game_message_rect = game_message.get_rect(center = (960,800))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,2200)

ogre_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(ogre_animation_timer,500)

goblin_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(goblin_animation_timer,200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
         
        if game_active:
            if event.type == pygame.KEYDOWN and hero_rect.bottom >= 850:
                if event.key == pygame.K_SPACE:
                    player_grav = -20
        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 100)

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['goblin','Ogre','Ogre','Ogre'])))
            if event.type == ogre_animation_timer: 
                if Ogre_frame_index == 0: Ogre_frame_index = 1
                else: Ogre_frame_index = 0
                Ogre_surf = Ogre_frames[Ogre_frame_index]

            if event.type == goblin_animation_timer: 
                if goblin_frame_index == 0: goblin_frame_index = 1
                else: goblin_frame_index = 0
                goblin_surf = goblin_frames[goblin_frame_index]

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,730))
        screen.blit(score_surf,score_rect)
        pygame.draw.rect(screen, 'white', score_rect)
        pygame.draw.rect(screen, 'white', score_rect,10)
        screen.blit(score_surf,score_rect)
        score = display_score()
    
    # Hero
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

    #Collision  
        game_active = collision_sprite()

    else:
        screen.blit(start_screen,(0,0))
        screen.blit(hero_stand,hero_stand_rect)
        obstacle_rect_list.clear()
        hero_rect.topleft = (220,650)
        player_grav = 0

        score_message = test_font.render(f'Your Score: {score}', True, 'Black')
        score_message_rect = score_message.get_rect(center = (960,800))
        screen.blit(game_name,game_name_rect)

        if score == 0:
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(score_message,score_message_rect)

    pygame.display.update()
    clock.tick(60)