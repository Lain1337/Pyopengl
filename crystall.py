import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
phi = (1+math.sqrt(5))/2
verticies = (
   (phi, 1, 0),
   (phi, -1, 0),
   (-phi ,-1, 0),
   (-phi, 1, 0),
   (0, phi, 1),
   (0, -phi, 1),
   (0, -phi, -1),
   (0, phi, -1),
   (1, 0, phi),
   (1, 0, -phi),
   (-1, 0, -phi),
   (-1, 0, phi),
   )
edges = (
     (0,7),
     (0,9),
     (0,8),
     (0,3),
     (0,4),
     (1,2),
     (1,5),
     (1,8),
     (1,9),
     (1,6),
     (2,5),
     (2,11),
     (2,10),
     (2,6),
     (3,4),
     (3,10),
     (3,7),
     (3,11),
     (4,8),
     (4,5),
     (4,11),
     (5,11),
     (5,8),
     (6,7),
     (6,9),
     (6,10),
     (7, 10),
     (7, 9),
     (8,9),
     (10,11)
     )
def Iqosaedr():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
def main():
    pygame.init()
    display = (1000,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -8)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Iqosaedr()
        pygame.display.flip()
        pygame.time.wait(10)
if __name__ == "__main__":
   main()
