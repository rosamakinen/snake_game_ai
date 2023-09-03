import pygame
import time
import random
 
window_x = 720
window_y = 480
 
green = pygame.Color(80, 255, 80)
pink = pygame.Color(255, 150, 150)
background = pygame.Color(100, 40, 40)
 
pygame.init()
pygame.display.set_caption('snakey snake')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()
 
#first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 
#default snake position
snake_position = [100, 50]

#default starting direction
direction = 'RIGHT'
change_to = direction
 
#score at start
score = 0

def show_score(choice, color, font, size):
   
    score_font = pygame.font.SysFont('comic sans', size)
    score_surface = score_font.render('Score : ' + str(score), True, pink)
    score_rect = score_surface.get_rect()   
    # displaying text with blit
    game_window.blit(score_surface, score_rect)
 
def game_over():
   
    my_font = pygame.font.SysFont('comic sans', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, pink)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # displaying text with blit
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()
 
 
#main
while True:
     
    #key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 'UP'
            if event.key == pygame.K_DOWN:
                direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
 
    # preventing going up and pressing down
    # snake crashes onto itself
#    if change_to == 'UP' and direction != 'DOWN':
#      direction = 'UP'
#    if change_to == 'DOWN' and direction != 'UP':
#        direction = 'DOWN'
#    if change_to == 'LEFT' and direction != 'RIGHT':
#        direction = 'LEFT'
#    if change_to == 'RIGHT' and direction != 'LEFT':
#        direction = 'RIGHT'
 
    # moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(background)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, pink, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
 
    # game over
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    # touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    show_score(1, pink, 'comic sans', 20)
    pygame.display.update()
    fps.tick(20)