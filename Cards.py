# importing modules
'''
import pygame #necessary for using game logic
from pygame.locals import* #allows for all the pygame constraints to be brought in
from sys import exit #allows us to exit our program even with loops
from random import randint #allows the cards to be random
'''
import pygame
from pygame.locals import*
from sys import exit
from random import randint

#Start Pygame
pygame.init()

#Creating the screen 400x400
screen = pygame.display.set_mode(400,400),0,32) #(width, height, flags, depth)

#Setting font
font = pygame.font.SysFont("Arial", 50)

#Dictionary of all images
IMAGESDICT = {'background': pygame.image.load(filename).convert(),
              'win_screen': pygame.image.load(filename).convert_alpha(),
              'lose_screen': pygame.image.load(filename).convert_alpha(),
              }

#Setting the title
pygame.display.set_caption('Alpha Card Game Test')

#Setting the Clock
clock = pygame.time.Clock()

#Generating initial cards, concatening and loading the images
#Figure out how to add to IMAGESDICT
card0 = randint(1, 23)
sprite_card0 = 'Card' + str(card0) + '.png'
card00 = pygame.image.load(sprite_card0).convert_alpha()
card1 = randint(1, 23)
sprite_card1 = 'Card' + str(card1) + '.png'
card01 = pygame.image.load(sprite_card1).convert_alpha()
card2 = randint(1, 23)
sprite_card2 = 'Card' + str(card2) + '.png'
card02 = pygame.image.load(sprite_card2).convert_alpha()
card3 = randint(1, 23)
sprite_card3 = 'Card' + str(card3) + '.png'
card03 = pygame.image.load(sprite_card3).convert_alpha()
card4 = randint(1, 23)
sprite_card4 = 'Card' + str(card4) + '.png'
card04 = pygame.image.load(sprite_card4).convert_alpha()
card5 = randint(1, 23)
sprite_card5 = 'Card' + str(card5) + '.png'
card05 = pygame.image.load(sprite_card5).convert_alpha()

#Hitpoints
my_life = 4000
enemy_life = 4000

#Setting coordinates for cards
#Check to see if this is correct
x0 = 30
y0 = 304
x1 = 97
x2 = 164

#Generating a null image in battle
pixel = 'pixel.png'

#Card is not in field at start
our_field = False
enemy_field = False

#Damage Variable
#Why do I need this?
dmg = 0

#Main loop:
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            #exit command
            exit()
    
    #setting the card in battle field
    card_in_battle = pygame.image.load(pixel).convert_alpha()
