from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

'''
estudante - Meriely Eline Lima Gaia
matrícula - 201633840047

'''

# ------- função para definir o fundo da tela com um quadrado ------- #
def square():
    glBegin(GL_QUADS) # inicio do esboço
    glVertex2f(-10, -10)
    glVertex2f(10, -10)
    glVertex2f(15, 15)
    glVertex2f(-15, 15)    
    glEnd() # fim do esboço


# A luz é dividida em quatro componentes que juntas formam o modelo de iluminação( Ambiente, Difusa, Especular e a Emissiva )
def setMaterial( ambientR, ambientG, ambientB, diffuseR, diffuseG, diffuseB, specularR, specularG, specularB, shininess ):
    ambient = [ ambientR, ambientG, ambientB ] # luz que vem de todas as direções
    diffuse = [ diffuseR, diffuseG, diffuseB ] # luz que vem de uma direção, atinge a superfície e é refletida em todas as direções
    specular = [ specularR, specularG, specularB ] # luz que vem de uma direção e tende a ser refletida numa única direção
    
#glMaterialfv( Quais faces do objeto estão sendo especificadas, Propriedade do material a ser especificada, Vetor Glfloat com os valores da propriedade especificada)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, ambient) # GL_AMBIENT - Cor ambiente do material 
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, diffuse) # GL_DIFFUSE - Cor difusa do material (COR)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specular) # GL_SPECULAR - Cor especular do material ( Cor do BRILHO)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, shininess)  # GL_SHININESS - Expoente especular (brilho na superfície)

# ------- função para definir quais objetos e onde serão mostrados na tela ------- #    
def showScreen():

    glClear(GL_COLOR_BUFFER_BIT) # Limpa a janela de visualização com a cor de fundo definida previamente.
    glMatrixMode(GL_MODELVIEW) # Aplica operações de matriz subsequentes à pilha de matriz modelview.
    
    glPushMatrix() # empurra a pilha da matriz atual para baixo em um
    glPushMatrix() # empurra a pilha da matriz atual para baixo em um
    glPushMatrix() # empurra a pilha da matriz atual para baixo em um
    glPushMatrix() # empurra a pilha da matriz atual para baixo em um
    glPushMatrix() # empurra a pilha da matriz atual para baixo em um
    
# ------- Fundo ------- #
    glTranslatef(0.0, 0.0, -15.0) # translação em (x, y, z)
    setMaterial(1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 50) # valores de (ambientR, ambientG, ambientB, diffuseR, diffuseG, diffuseB, specularR, specularG, specularB, shininess)
    square() # desenha um quadrado
    glPopMatrix() # exibe a pilha da matriz atual, substituindo a matriz atual pela que está abaixo dela na pilha.
    
# ------- Cubo esquerda ------- #
    glTranslatef(-5.0, 0.0, -10.0) 
    glRotatef(-50.0, 5.0, 0.0, 0.0)
    setMaterial(0, 0.5, 1, 0, 0.5, 1, 1.0, 1.0, 1.0, 50)
    glutSolidCube(2) # desenha um cubo
    glPopMatrix() 
      
# ------- Cubo direita ------- #
    glTranslatef(5, 0, -10) 
    glRotatef(50, -5, 0, 0)
    setMaterial(0, 0.5, 1, 0, 0.5, 1, 1.0, 1.0, 1.0, 50)
    glutSolidCube(2) # desenha um cubo
    glPopMatrix() 

# ------- Esfera ------- #
    glTranslatef(0, 0, -10)
    setMaterial(0, 0.5, 1, 0, 0.5, 1, 1.0, 1.0, 1.0, 50)
    glutSolidSphere(2, 50, 2) # desenha uma esfera
    glPopMatrix() 
    
# ------- Cone ------- # 
    glTranslatef(0, 0, -10) # (por escolha, não coloquei o desenho cobrindo o outro, apenas em cima)
    glRotatef(45, -1, 0, 0) # rotaciona
    setMaterial(0, 1.0, 0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1)
    glutSolidCone(1, 3, 100, 100) # desenha um cone
    glPopMatrix()
    
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800,600) # tamanho da janela
glutInitWindowPosition(0,0) # posição da janela
wind = glutCreateWindow("Visualização Objetos OGL") # Tírulo da janela
glEnable(GL_DEPTH_TEST) 
glutDisplayFunc(showScreen)

glEnable(GL_LIGHTING) # Habilita o uso de iluminação
glEnable(GL_LIGHT0) # Habilita a luz 
glLightfv(GL_LIGHT0, GL_POSITION, (0, 1.5, 1, 0)) # Fonte de Luz 
glutIdleFunc(showScreen)

glMatrixMode(GL_PROJECTION) # Aplica operações de matriz subsequentes à pilha de matriz de projeção.
glLoadIdentity()
gluPerspective(45, float(800/600), 0.1, 25.0) # Camera 

glMatrixMode(GL_MODELVIEW) # Aplica operações de matriz subsequentes à pilha de matriz modelview.
glLoadIdentity()
gluLookAt(0.0, 0.0, 5.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0) # Camera 

glutMainLoop() # chamará, conforme necessário, todos os retornos de chamada que foram registrados.

