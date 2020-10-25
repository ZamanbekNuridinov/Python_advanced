import pygame 
import math
pygame.init()

size = (1000, 400)
black=(0,0,0)
white=(255,255,255)
gray=(128,128,128)
green=(0,255,0)

fps=20
screen = pygame.display.set_mode(size)
clock =pygame.time.Clock()
pygame.display.set_caption('Graph')

# f1=pygame.font.Font(None, 32)
# text1=f1.render('Hello world', True, black)

# f2=pygame.font.SysFont('arial', 20)
# text2=f2.render('Hello world!!!', True, black)

# screen.blit(text1, (100, 50))
# screen.blit(text2, (10, 100))
# pygame.display.update() 

def drawGrid(): 
    height = 69
    width = 100
    x,y = 50,45

    x_Axis_left=[x+25,y+height*2]
    x_Axis_right=[925,y+height*2]
    y_Axis_up=[x*2+width*4,y-20]
    y_Axis_down=[x*2+width*4,y+25+height*4]
    pygame.draw.line(screen, black, x_Axis_left, x_Axis_right, 2)
    pygame.draw.line(screen, black, y_Axis_up, y_Axis_down, 2)
    for i in range(9):
        for j in range(5):
            line_y_up=[x*2+width*i,y]
            line_y_down=[x*2+width*i,y+25+height*j] 
            pygame.draw.line(screen, gray, line_y_up, line_y_down, 1)
            line_x_left=[x+25,y+height*j]
            line_x_right=[925,y+height*j]
            pygame.draw.line(screen, gray, line_x_left, line_x_right, 1)

def drawSin():
    for x in range(75,size[0]-75):
        y=int(138*math.sin((x+500-step)/400*2*math.pi))+183
        pygame.draw.line(screen, green, [x,y],[x,y], 2)
#     for x in range(20, size[0]-20):
#         y = int((size[1]/2) + a*math.sin(f*((float(x)/size[0])*(2*math.pi) + (s*time.time()))))
#         #surface.set_at((x, y), color_of_graph)
#         pygame.draw.line(surface, color_of_graph, [x, y], [x, y], 3)
#         pygame.draw.line(surface, color_of_Axes, [x, int(size[1]/2)], [x, int(size[1]/2)], 1)

done = False
step=0
while not done:
    step+=1
    drawGrid()
    drawSin()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True  
    pygame.display.flip()
    clock.tick(fps)
    screen.fill(white)

pygame.quit()