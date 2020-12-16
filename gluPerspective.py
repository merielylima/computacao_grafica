from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



# ---Section 1---
def square():
# We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_QUADS) # Begin the sketch
    glVertex2f(-5, -5) # Coordinates for the bottom left point
    glVertex2f(5, -5) # Coordinates for the bottom right point
    glVertex2f(5, 5) # Coordinates for the top right point
    glVertex2f(-5, 5) # Coordinates for the top left point
    glEnd() # Mark the end of drawing

# This alone isn't enough to draw our square



# Add this function before Section 2 of the code above i.e. the showScreen function
def iterate():

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(0, 0, 500,500)   
    

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, float(500/500), 0.1, 25.0) # gluPerspective 

# ---Section 2---

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glLoadIdentity() # Reset all graphic/shape's position
    iterate()
    
    glTranslatef(-10, -10, -25) # translação em (x, y, z)
    glColor3f(1.0, 0.0, 0.0) # Set the color to red

    square() # Draw a square using our function
    glutSwapBuffers()

#---Section 3---

glutInit()
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(500, 500)   # Set the w and h of your window
glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = glutCreateWindow("OpenGL Coding Practice") # Set a window title

glutDisplayFunc(showScreen)
glutIdleFunc(showScreen) # Keeps the window open

glutMainLoop()  # Keeps the above created window displaying/running in a loop

