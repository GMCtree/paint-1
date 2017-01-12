from pygame import *
import math
from random import*


init()      # need to initialize the font module before using it.
fnt = font.SysFont("Papyrus",24)

screen = display.set_mode((1024,768))
background=image.load("LayoutFinal.png")
screen.blit(background,(0,0))

#drawSpace=Rect(33,52,711,486)
drawSpace=Rect(44,62,693,467)
screen.fill((255,255,255),drawSpace)
#canvas=draw.rect(screen,(255,255,255), drawSpace)

#Other varibules
c = (0,0,0)
mx,my = 0,0
cyan = (0,255,255)
r = 10
point = []

#Tool Rectangles
pencilRect = Rect(800,40,40,40)
paintRect = Rect(800,190,40,40)


#boxThickness
boxThick = 1

#----------------Line Choice-----
lineThick=1


#-----------------------------

boxRect = Rect(877,90,40,40)


#colourbox rect
colourRect = Rect(600,679,40,40)
draw.rect(screen,c,colourRect)

#import colour bar
#pic = image.load("colors.png")
#screen.blit(pic,(40,600))
picRect = Rect(40,600,403,119)

Stamps = image.load("Stamps.png")
#-----------------------------
stamp1 = Rect(515,589,32,29)
stamp2 = Rect(579,589,32,29)
stamp3 = Rect(638,589,107,28)
stamp4 = Rect(514,626,35,32)
stamp5 = Rect(557,624,35,32)
stamp6 = Rect(597,626,167,28)
stamp = ""
#----------------Stamp Load---------------
stampA = image.load("A.png")
stampB = image.load("B.png")
stampC = image.load("C.png")
stampD = image.load("D.png")
stampE = image.load("E.png")
stampF = image.load("F.png")

clearRect = Rect(862,360,62,21)
saveRect = Rect (786,360,48,20)
loadRect = Rect(942,361,53,20)
#set screen clip
#--------------
tool = ""
stamp = None
points = []
running=True

while running:
    for evnt in event.get():
        if evnt.type==QUIT:
            running=False
        #for drawline tool   
        if evnt.type == MOUSEBUTTONDOWN:
            omx2 = mx
            omy2 = my
            Copy = screen.copy()

    #Trace Mouse events
    omx,omy = mx,my
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    draw.rect(screen,cyan,saveRect,3)
    draw.rect(screen,cyan,loadRect,3)

    #if mb[0] == 1:
        #print mx,my
    
    #brush Thickness
    
    #colour choose
    draw.rect(screen,c,colourRect)
    if mb[0] == 1 and picRect.collidepoint(mx,my):
        c = screen.get_at((mx, my))
        draw.rect(screen,c,colourRect)


    # SELECT TOOL
    if mb[0]==1 and pencilRect.collidepoint(mx,my) and tool != "pencil":
        tool = "pencil"
        screen.blit(background,(0,0))
        draw.rect(screen,cyan,pencilRect,3)


    if mb [0] == 1 and boxRect.collidepoint(mx,my) and tool != "box":
        tool = "box"
        screen.blit(background,(0,0))
        draw.rect(screen,cyan,boxRect,3)
#-------------------Saving-------------------------
    if mb [0] == 1 and saveRect.collidepoint(mx,my):
        savename = raw_input("Enter the Full name with the extension <end to exit>\n")
        if savename.lower() == "end":
            print "Keep using paint"
        canvascopy=screen.subsurface(drawSpace).copy() #takes copy of canvas
        image.save(canvascopy,savename)
#---------Opening--------------------
    if mb [0] == 1 and loadRect.collidepoint(mx,my):
        loadname=raw_input("Enter the full name of the files you want to load\n with the extension<end to exit>\n")
        if loadname.lower() == "end":
            print "Keep using paint"
        loadpic=image.load(loadname) #loads image 
        screen.blit(loadpic,(44,62)) #blits image at canvas' top left corner
#---Stamps--------------------------------------------
    if mb[0] == 1 and paintRect.collidepoint(mx,my) and tool != "stamps":
        tool = "stamps"
        screen.blit(background,(0,0))
        draw.rect(screen,cyan,paintRect,3)

    if tool == "stamps":
        screen.blit(Stamps,(500,580))
        if stamp1.collidepoint(mx,my) and mb[0] == 1:
            stamp = "stamp1"

        if stamp2.collidepoint(mx,my) and mb[0] == 1:
            stamp = "stamp2"

        if stamp3.collidepoint(mx,my) and mb[0] == 1:
            stamp = "stamp3"

        if stamp4.collidepoint(mx,my) and mb[0] == 1:
            stamp = "stamp4"

        if stamp5.collidepoint(mx,my) and mb[0] == 1:
            stamp = "stamp5"

        if stamp6.collidepoint(mx,my) and mb[0] == 1:
            stamp = "stamp6"
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        if stamp == "stamp1":
            screen.blit(Stamps,(500,580))
            draw.rect(screen,cyan,stamp1,3)

        if stamp == "stamp2":
            screen.blit(Stamps,(500,580))
            draw.rect(screen,cyan,stamp2,3)

        if stamp == "stamp3":
            screen.blit(Stamps,(500,580))
            draw.rect(screen,cyan,stamp3,3)

        if stamp == "stamp4":
            screen.blit(Stamps,(500,580))
            draw.rect(screen,cyan,stamp4,3)

        if stamp == "stamp5":
            screen.blit(Stamps,(500,580))
            draw.rect(screen,cyan,stamp5,3)

        if stamp == "stamp6":
            screen.blit(Stamps,(500,580))
            draw.rect(screen,cyan,stamp6,3)
#---------------------End of Stanm------------------------
    

    # DRAW ON CANVAS
    if mb[0]==1 and drawSpace.collidepoint(mx,my):
        #Set clip
        screen.set_clip(drawSpace)

        if tool == "pencil":
            draw.line(screen, c ,(omx,omy),(mx,my),lineThick)

        if tool == "box":
            screen.blit(Copy,(0,0))
            draw.rect(screen, c , (omx2,omy2, mx - omx2 , my-omy2), boxThick)
    #----------------Drawing Stamps-------------------------
        if tool == "stamps":
            if stamp == "stamp1":
                screen.blit(Copy,(0,0))
                screen.blit(stampA,(mx-60,my-50))

            if stamp == "stamp2":
                screen.blit(Copy,(0,0))
                screen.blit(stampB,(mx-645,my-185))

            if stamp == "stamp3":
                screen.blit(Copy,(0,0))
                screen.blit(stampC,(mx-142,my-57))

            if stamp == "stamp4":
                screen.blit(Copy,(0,0))
                screen.blit(stampD,(mx-65,my-67))

            if stamp == "stamp5":
                screen.blit(Copy,(0,0))
                screen.blit(stampE,(mx-76,my-83))

            if stamp == "stamp6":
                screen.blit(Copy,(0,0))
                screen.blit(stampF,(mx-120,my-94))
    #---------------Done Drawing Stamps---------------------------


        #Remove Clip when off canvas
        screen.set_clip(None)
            

            

    
    display.flip()
time.wait(10)

quit()












        
