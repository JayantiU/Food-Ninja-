#Border city hacks program
#Game; fruit ninja
from pygame import *
from os import environ 
#---Screen Setup---#
init()
inf = display.Info()
cen=(inf.current_w-1200)/2 #finds the x coordinate so that the screen can be centered (this is how much distance there'll be from the left and right corner of computer screen to the left and right corner (respectively)of the paint program screen)
environ['SDL_VIDEO_WINDOW_POS'] = '%d,25'%cen 
screen=display.set_mode((800,600))
display.set_caption('Food Ninja')
display.set_icon(image.load('logo.jpg'))
running=True
while running:
  mb=mouse.get_pressed()
  mx,my=mouse.get_pos()
  draw.rect(screen,(0,255,255),(200,200,400,400),20)




#---Displaying---#
  display.flip()

