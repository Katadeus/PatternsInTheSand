import math
points = []
clicked = False

def setup():
    size(640,640)
    background(0,0,0)

def draw():
    global points
    global clicked
    if clicked:
        a = random(360)
        d = math.sqrt(1)
        x = sin(a)*d*mx+320
        y = cos(a)*d*my+320
        points.append([x,y,a,400])
        stroke(255,255,255)
        for i in range(0,len(points)):
            if points[i][3] > 0:
                #fill(points[i][0]/2,points[i][1]/2,points[i][2])
                #stroke(points[i][0]/2,points[i][1]/2,points[i][2])
                ellipse(points[i][0],points[i][1],1,1)
                d = math.sqrt(math.pow(x-320,2)+math.pow(y-320,2))
                points[i] = [points[i][0]+sin(points[i][2])*(200-d)*1,points[i][1]+cos(points[i][2])*(200-d)*1,points[i][2],points[i][3]-1]

def mouseClicked():
    global clicked
    global mx
    global my
    if clicked == False:
        mx = mouseX
        my = mouseY
        clicked = True;
