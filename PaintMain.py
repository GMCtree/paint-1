from pygame import *
import math
from math import *
from random import *

screen = display.set_mode((1024,768))
background=image.load("LayoutFinal.png")
screen.blit(background,(0,0))

#Polygon tool variables
done = False
polygon_start = False
points = []
snap_x = 0
snap_y = 0

drawSpace=Rect(44,62,693,467)
screen.fill((255,255,255),drawSpace)

#Other varibules
c = (0,0,0)
mx,my = 0,0
cyan = (0,255,255)
r = 10
point = []

#Clear Rect
clearRect = Rect(862,360,62,21)
saveRect = Rect (786,360,48,20)
loadRect = Rect(942,361,53,20)
paintRect = Rect(800,190,40,40)

#Tool Rectangles
pencilRect = Rect(800,40,40,40)
eraserRect = Rect(877,40,40,40)
lineRect = Rect(950,40,40,40)
ellipseRect = Rect(877,140,40,40)
polygonRect = Rect(950, 140, 40, 40)

#brush Thickness
brushThick = 5
cRect1 = Rect(533,600,10,10)
cRect2 = Rect(523,633,30,30)
cRect3 = Rect(515,690,50,50)

#boxThickness
boxThick = 0
box1 = Rect(500,700,80,30)

#----------------Line Choice-----
lineThick=1
line1 = Rect(500,580,80,30)
line2 = Rect(500,620,80,30)
line3 = Rect(500,660,80,30)

#%%%%%%%%%%%%%%%%%%%%%%%Stamps#################################

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
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#-----------------------------
brushRect = Rect(800,90,40,40)
boxRect = Rect(877,90,40,40)
sprayRect = Rect(950,90,40,40)
eyeRect = Rect (800,140,40,40)

#colourbox rect
colourRect = Rect(600,679,40,40)
draw.rect(screen,c,colourRect)

#colour bar
picRect = Rect(40,600,403,119)


tool = ""
running=True

while running:
    #Trace Mouse events
    omx,omy = mx,my
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    
    for evnt in event.get():
        if evnt.type==QUIT:
            running=False
        #for drawline tool   
        if evnt.type == MOUSEBUTTONDOWN:
            omx2 = mx
            omy2 = my
            if tool == "line" and drawSpace.collidepoint(mx,my):
                draw.line(screen,c,(omx2,omy2),(mx,my),lineThick)
            if tool == "polygon" and drawSpace.collidepoint(mx, my):
                if done == True:
                    #polygon_start = False
                    points = []
                    done = False
                    #tool = ""
                elif polygon_start == True:
                    points.append((mx, my))
                    if len(points) >= 1:
                        draw.line(screen, c, points[len(points) - 1], (mx, my),lineThick)
            Copy = screen.copy()

    draw.rect(screen,cyan,saveRect,3)
    draw.rect(screen,cyan,loadRect,3)
    draw.rect(screen,cyan,clearRect,3)

    #colour choose
    draw.rect(screen,c,colourRect)
    if mb[0] == 1 and picRect.collidepoint(mx,my):
        c = screen.get_at((mx, my))
        draw.rect(screen,c,colourRect)

    if mb[0] == 1 and clearRect.collidepoint(mx,my):
        screen.blit(background,(0,0))
        draw.rect(screen,(255,255,255),drawSpace,0)

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


    # SELECT TOOL
    if mb[0]==1 and pencilRect.collidepoint(mx,my) and tool != "pencil":
        tool = "pencil"
        screen.blit(background,(0,0))
        draw.rect(screen,cyan,pencilRect,3)

    if mb[0]==1 and eraserRect.collidepoint(mx,my) and tool != "eraser":
        tool = "eraser"
        screen.blit(background,(0,0))
        draw.rect(screen,cyan,eraserRect,3)

    if mb[0] == 1 and lineRect.collidepoint(mx,my) and tool != "line":
        tool = "line"
        screen.blit(background,(0,0))
        draw.rect(screen,cyan,lineRect,3)

    if mb[0] == 1 and brushRect.collidepoint(mx,my) and tool != "brush":
        tool = "brush"
        screen.blit(background,(0,0))
        draw.rect(screen,cyan,brushRect,3)

    if mb [0] == 1 and boxRect.collidepoint(mx,my) and tool != "box":
        tool = "box"
        screen.blit(background,(0,0))
        draw.rect(screen,cyan,boxRect,3)

    if mb [0] == 1 and sprayRect.collidepoint(mx,my) and tool != "spray":
        tool = "spray"
        #screen.blit(background,(0,0))
        draw.rect(screen,cyan,sprayRect,3)

    if mb [0] == 1 and colourRect.collidepoint(mx,my):
        draw.rect(screen,c,colourRect)

    if mb [0] == 1 and eyeRect.collidepoint(mx,my) and tool != "eyedropper":
        tool = "eyedropper"
        screen.blit(background,(0,0))
        draw.rect(screen,cyan,eyeRect,3)

    if mb[0] == 1 and ellipseRect.collidepoint(mx,my) and tool != "ellipse":
        tool = "ellipse"
        screen.blit(background,(0,0))
        draw.rect(screen,cyan,ellipseRect,3)

    if mb[0] == 1 and polygonRect.collidepoint(mx,my) and tool != "polygon":
        tool = "polygon"
        points = []
        polygon_start = True
        screen.blit(background,(0,0))
        draw.rect(screen,cyan,polygonRect,3)

    #------ Eyedropper ------------
    if tool == "eyedropper" and drawSpace.collidepoint(mx,my) and mb[0] == 1:
        c = screen.get_at((mx,my))
        draw.rect(screen,c,colourRect)
    #--- Eye Dropper End -----

    #-Drawline thicknesses----
    if tool == "line":
        #Line Thicknessess
        draw.rect(screen,(0,255,255),line2,2)
        draw.rect(screen,(0,255,255),line1,2)
        draw.rect(screen,(0,255,255),line3,2)
      #------------------------------------------------        
        draw.line(screen,(0,255,255),(510,595),(570,595),5)
        draw.line(screen,(0,255,255),(510,635),(570,635),3)
        draw.line(screen,(0,255,255),(510,675),(570,675),1)

    if tool == "box" or tool == "ellipse" or tool == "polygon":
        #Line Thicknessess
        draw.rect(screen,(0,255,255),line2,2)
        draw.rect(screen,(0,255,255),line1,2)
        draw.rect(screen,(0,255,255),line3,2)
        #box fill
        draw.rect(screen,(0,255,255),box1,1)
        draw.rect(screen,(0,255,255),(510,710,60,10),0)
        #box fill end          
        draw.line(screen,(0,255,255),(510,595),(570,595),5)
        draw.line(screen,(0,255,255),(510,635),(570,635),3)
        draw.line(screen,(0,255,255),(510,675),(570,675),1)

    #-----------------Brush Thickness-------------
    if tool == "brush" or tool == "spray":
        draw.ellipse(screen,cyan,cRect1,1)
        draw.ellipse(screen,cyan,cRect2,1)
        draw.ellipse(screen,cyan,cRect3,1)

    #--Brush Thiskness Choose-----------
    if mb[0] == 1 and cRect1.collidepoint(mx,my):
        brushThick = 5
        r = 5
    if mb[0] == 1 and cRect2.collidepoint(mx,my):
        brushThick = 15
        r = 15
    if mb[0] == 1 and cRect3.collidepoint(mx,my):
        brushThick = 25
        r = 25
        
    #Choose Line Thickness
    if mb[0] == 1 and line1.collidepoint(mx,my):
        lineThick = 5
        boxThick = 5
    if mb[0] == 1 and line2.collidepoint(mx,my):
        lineThick = 3
        boxThick = 3
    if mb[0] == 1 and line3.collidepoint(mx,my):
        lineThick = 1
        boxThick = 1
    if mb[0] == 1 and box1.collidepoint(mx,my):
        boxThick = 0

    # DRAW ON CANVAS
    if mb[0]==1 and drawSpace.collidepoint(mx,my):
        #Set clip
        screen.set_clip(drawSpace)

        if tool == "pencil":
            draw.line(screen, c ,(omx,omy),(mx,my),1)

        if tool == "eraser":
            dist = math.hypot((mx-omx),(my-omy))
            if dist == 0: dist = 1
            sx = (mx-omx)/dist
            sy = (my-omy)/dist
            for i in range(int(dist)):
                draw.circle(screen,(255,255,255),(int(omx+sx*i),int(omy+sy*i)),20)

        if tool == "line":
            screen.blit(Copy,(0,0))
            draw.line(screen,c,(omx2,omy2),(mx,my),lineThick)

        if tool == "brush":
            dist = math.hypot((mx-omx),(my-omy))
            if dist == 0: dist = 1
            sx = (mx-omx)/dist
            sy = (my-omy)/dist
            for i in range(int(dist)):
                draw.circle(screen,c,(int(omx+sx*i),int(omy+sy*i)),brushThick)

        if tool == "box":
            screen.blit(Copy,(0,0))
            draw.rect(screen, c , (omx2,omy2, mx - omx2 , my-omy2), boxThick)

        if tool == "spray":
            for i in range(10):
                x = randint(-1*r,r)
                ydist = int((r**2 - x**2)**(0.5))
                y = randint((-1)*ydist,ydist)
                xpos = x + mx
                ypos = y + my
                screen.set_at((xpos,ypos),c)


        if tool == "ellipse":
            screen.blit(Copy,(0,0))
            if abs(omx2-mx)>1 and abs(omy2-my)>1:
                if boxThick == 0:
                    draw.ellipse(screen,c,(min(mx,omx2),min(my,omy2),abs(omx2-mx),(abs(omy2-my))))
                if boxThick == 1:
                    draw.ellipse(screen,c,(min(mx,omx2),min(my,omy2),abs(omx2-mx),(abs(omy2-my))),1)
                if boxThick == 3:
                    try:
                        draw.ellipse(screen,c,(min(mx,omx2),min(my,omy2),abs(omx2-mx),(abs(omy2-my))),5)
                    except ValueError:
                        pass
                if boxThick == 5:
                    try:
                        draw.ellipse(screen,c,(min(mx,omx2),min(my,omy2),abs(omx2-mx),(abs(omy2-my))),10)
                    except ValueError:
                        pass
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
            
    if tool == "polygon" and drawSpace.collidepoint(mx, my):
        if len(points) >= 1:
            screen.blit(Copy, (0, 0))
            snap_x, snap_y = points[0]
            if hypot(snap_x - mx, snap_y - my) < 10:
                omx, omy = snap_x, snap_y
                if len(points) >= 3:
                    done = True
                    if boxThick == 0:
                        draw.polygon(screen, c, points, 0)
            draw.line(screen, c, points[len(points) - 1], (omx, omy),lineThick)
            

    
    display.flip()
time.wait(10)    
quit()
